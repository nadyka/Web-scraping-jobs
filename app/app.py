import os
import json
import subprocess
import datetime
import logging
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import desc

# Configure logging
log_filename = f"run_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db) # Initialize Flask-Migrate here


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_ranking = db.Column(db.String(100))
    job_index = db.Column(db.Integer)
    job_rating = db.Column(db.Integer)
    job_website = db.Column(db.String(100))
    job_title = db.Column(db.String(100))
    job_company = db.Column(db.String(100))
    job_company_type = db.Column(db.String(100))
    job_company_sector = db.Column(db.String(100))
    job_country = db.Column(db.String(100))
    job_country_code = db.Column(db.String(100))
    job_city = db.Column(db.String(100))
    job_summary = db.Column(db.String(300))
    job_date = db.Column(db.String(100))
    job_url = db.Column(db.String(100))

def get_sorting_values():
    sorting_values = request.form.get("sort")
    return sorting_values

def get_website():
    website_list = request.form.getlist("website")
    return website_list

def get_query():
    query = request.form.get("query")
    return query

def get_location():
    location_list = request.form.get("location")
    location_list = location_list.split(';')
    return location_list

def get_distance():
    distance = request.form.get("distance")
    return distance

def get_title_keywords_must():
    title_keywords_must = request.form.get("title_keywords_must")
    title_keywords_must = title_keywords_must.split(';')
    return title_keywords_must

def get_title_keywords_excluded():
    title_keywords_excluded = request.form.get("title_keywords_excluded")
    title_keywords_excluded = title_keywords_excluded.split(';')
    return title_keywords_excluded

def get_pages():
    pages = request.form.get("pages")
    return pages

# Preferences
def get_title_keywords_ordered():
    title_keywords_ordered = request.form.get("title_keywords_ordered")
    title_keywords_ordered = title_keywords_ordered.split(';')
    return title_keywords_ordered

def get_company_size_type():
    company_size_type_bool = request.form.getlist("company_size_type")
    Large_bool, Intermediate_bool, Medium_bool, Small_bool, Startup_bool = False, False, False, False, False
    for size in company_size_type_bool:
        if size == "Large":
            Large_bool = True
        elif size == "Intermediate":
            Intermediate_bool = True
        elif size == "Medium":
            Medium_bool = True
        elif size == "Small":
            Small_bool = True
        elif size == "Startup":
            Startup_bool = True
    
    if (Large_bool is False) and (Intermediate_bool is False) and (Medium_bool is False) and (Small_bool is False) and (Startup_bool is False):
        Large_bool = True
        Intermediate_bool = True
        Medium_bool = True
        Small_bool = True
        Startup_bool = True

    company_size_type = {"Large Enterprise (+5000 employees)":Large_bool,
                    "Intermediate-sized Enterprise (251-5000 employees)":Intermediate_bool,
                    "Medium-sized Enterprise (51-250 employees)":Medium_bool,
                    "Small-sized Enterprise (11-50 employees)":Small_bool,
                    "Startup (1-10 employees)":Startup_bool
                    }
    return company_size_type
    

def get_all_information_about_jobs_request():
    website = get_website()
    query = get_query()
    location = get_location()
    distance = get_distance()
    title_keywords_must = get_title_keywords_must()
    title_keywords_excluded = get_title_keywords_excluded()
    pages = get_pages()
    title_keywords_ordered = get_title_keywords_ordered()
    company_size_type = get_company_size_type()
    dic = {'website':website,
        'query':query,
        'location':location,
        'distance':distance,
        'title_keywords_must':title_keywords_must,
        'title_keywords_excluded':title_keywords_excluded,
        'pages':pages,
        'title_keywords_ordered':title_keywords_ordered,
        'company_size_type':company_size_type
        }
    return dic



@app.route("/")
def home():
    logging.info('Starting home function')
    heads = ["ID", "JOB RATING", "WEBSITE", "TITLE", "COMPANY", "COMPANY TYPE", "COMPANY SECTOR", "COUNTRY", "CITY", "JOB SUMMARY", "DATE", "JOB URL"]
    jobs = Job.query.all()
    
    print("\n\nJOBS IN TABLE:'{}'\n\n".format(jobs))
    for job in jobs:
        db.session.delete(job)
        db.session.commit()
    return render_template("base.html", jobs=jobs, heads=heads)

    logging.info('Finished querying jobs')
    logging.info('Finished home function')
    return render_template("base.html", jobs=jobs, heads=heads)


@app.route("/add", methods=["POST"])
def add():
    """
    Retrieves job data from a database, user request, and JSON files.
    Deletes existing job data from the database.
    Creates and updates JSON files with job data.
    Loads and displays job data on the user interface.
    
    Returns:
        A redirect to the home page.
    """

    logging.info('Starting add function')

    # Remove existing job data from the database
    jobs = Job.query.all()
    
    for job in jobs:
        logging.info(f"Deleting job '{job.id}'")
        print(f"Job '{job.id}' deleted")        # for debugging, print message to console.
        db.session.delete(job)
        db.session.commit()
    logging.info('Finished deleting jobs')

    # Retrieve user request
    dic_info = get_all_information_about_jobs_request()
    print('\nJobs parameters user request sent', dic_info,'\n')      # for debugging, print message to console.
    logging.info('Finished retrieving user request')
    
    # Check if the file exists, and create it if not
    json_test = os.path.join('..', '..', 'data', 'jobs_parameters_user_request.json')
    json_test = os.path.abspath(json_test)
    print(f" json_test: '{json_test}' file is located at: '{os.path.abspath(json_test)}'")
    if not os.path.exists(json_test):
        with open(json_test, "w") as outfile:
            outfile.write('{}') # Write an empty JSON object
    logging.info('Finished checking and creating JSON file')

    # Now you can write to the file
    with open(json_test, "w") as outfile:
        json.dump(dic_info, outfile, indent=4, separators=(', ', ': '))
    logging.info('Finished writing to JSON file')

    # # Create and update a JSON file with user request data
    # json_test = "../../data/jobs_parameters_user_request.json"
    # with open(json_test, "w") as outfile:
    #     json.dump(dic_info, outfile, indent=4, separators=(', ', ': ')) 
    
    # Run a Python script for scraping jobs
    # TODO: not sure why this script is located in the "notebooks" folder.  Should be in "scripts" or "src" folder.
    subprocess.call("../../notebooks/scraping_jobs.py", shell=True)
    logging.info('Finished running scraping script')

    # Load and display data from a JSON file on the user interface
    json_filename = "../../data/jobs.json"
    with open(json_filename, "r") as json_file:
        data = json.load(json_file)
    logging.info('Finished loading data from JSON file')

    print("\n",data[0],"\n")  # for debugging, print message to console. Remove for production
    for i in range(len(data)):
        job = data[i]
        new_job = Job(job_ranking="id",
                    job_index=job['index'],
                    job_rating=job['General rating'],
                    job_website=job['Website'],
                    job_title=job['Title'],
                    job_company=job['Company'],
                    job_company_type=job['Company_type'],
                    job_company_sector=job['Company_sector'],
                    job_country=job['Country'],
                    job_country_code=job['Country_code'],
                    job_city=job['City'],
                    job_summary=job['Summary'],
                    job_date=job['Date'],
                    job_url=job['Job_url']
                    )
        db.session.add(new_job)
        db.session.commit()

    logging.info('Finished adding new jobs to database')
    logging.info('returning from add function')    
    return redirect(url_for("home"))


# @app.route("/update/<int:job_id>")
# def update(job_id):
#     job = Job.query.filter_by(id=job_id).first()
#     job.complete = not job.complete
#     db.session.commit()
#     return redirect(url_for("home"))


@app.route("/delete", methods=["POST"])
def delete():
    jobs = Job.query.all()
    for job in jobs:
        db.session.delete(job)
        db.session.commit()
    return redirect(url_for("home"))



@app.route("/sort", methods=["POST"])
def sort():
    sorting_values = get_sorting_values()
    print(f"\nsorting_values: '{sorting_values}'\n")
    jobs = Job.query.all()
    for job in jobs:
        job.job_ranking = sorting_values
        db.session.commit()

    # new_jobs = Job.query.order_by(sorting_values).all()
    # print("\n\n(SORT) JOBS ORDERED -> new_jobs:'{}'\n\n".format(new_jobs))

    return redirect(url_for("home"))



if __name__ == "__main__":
    db.create_all()
    migrate.init_app(app, db)
    app.run(debug=True)


# https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
# https://jinja.palletsprojects.com/en/3.0.x/templates/#jinja-filters.groupby
# https://stackoverflow.com/questions/9109915/how-can-i-switch-two-fields-of-a-unique-row-within-one-commit-using-sqlalchemy
# https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables
