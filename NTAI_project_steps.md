# Jobs Finder Webcraper Project Planning

## Project Action Items TBD (Next Steps): 
### Document the Webscrapers project steps:

TODO: add other people from the AI-powered training group. 

TODO: Fix error: when pressing 
    route: http://127.0.0.1:5000/add shows error on page: 
    Internal Server Error
    The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.

TODO: Do not delete jobs from the jobs table before every run.  
TODO: Verify if a job has already been added to the jobs table and keep it. Only add new jobs, do not delete existing ones. 

TODO: add logging to scraping_jobs.py and app.py
#### {Phind Prompt} It looks like data are not being retrieved by the scraper, because the db.sqlite database is empty, and the jobs.csv file and other files are not being created.  We need to add Python logging, or turn on Flask logging if it is already available (please advise).  The entire application (app.py, scraping_jobs.py, etc) must log to a file named "run_log_{datetime}.log" so that we can check all operations as they happen, and persist them for each run.  Please add complete logging statements to the app.py file and the scraping_jobs.py file.  Please add complete logging statements for every CRUD operation, e.g., where any data files or objects are created, read, updated, or deleted, and every other operation.  We need to be able to analyze the run_log to see what actually happens when the program runs.  

TODO: {Phind Prompt}: 
#### Please try again, but this time read the docstrings or in-line comments of each function or CRUD operation and then provide appropriate entry and exit logging statements with targeted logging message for each specific function or data object CRUD operation.  DO THIS FOR THE ENTIRE FILE, NOT JUST THE SCRAPING FUNCTIONS.  Please rewrite the complete file, and do not just show examples.  I want a complete file that I can test immediately.  

TODO: The file requests headers file "data\jobs_parameters_user_request.json" is not being created properly on line 187 of app.py.  

## Using git and Github for Collaboration and Source Control:
- 1. Create a new repository on GitHub by forking the original repository.
- 2. Clone the repository to your local machine using Github Desktop, git command line, or another tool.
     This creates a new local branch (git repository) for your own project work.
     (This step can be done using the local git command line [ git init, ]).
- 3. Create new file(s) or modify existing files in the local project folder (local git repository).
- 4. Use the "Source Control" tool (built-in to VSCode) to add the files to the staging area.
- 5. Commit the new or changed file(s) to the LOCAL git repository.
- 6. Push the file(s) to your remote Github repository.
- 7. If you want the original repo owner to merge (pull) your changes or additions into the main branch, then you must create a pull request (if you don't have privileges granted by the main branch owner.)

Download the packages: 

(base) C:\Windows\System32>cd C:\Users\Nadia Stoyanova

(base) C:\Users\Nadia Stoyanova>conda activate webscrapers

## Create Conda Virtual Environment:  
### (see below or file named "conda_commands_to_create_updated_jobs_webscrapers_env.txt")

    # conda command history extract manually from the history file located at c:\programdata\anaconda3\env\webscrapers\conda-meta

    create -n webscrapers -c conda-forge python beautifulsoup4 requests selenium pandas requests geopy bs4 flask sqlalchemy iso3166 Flask-SQLAlchemy Flask-Migrate Werkzeug 

    conda install -c conda-forge google-api-python-client 

    conda install -c pytorch pytorch torchvision torchaudio 

    # To update the package named "conda" in the CURRENTLY ACTIVATED conda environment.  
    # In this case, the environment is called "webscrapers.  Use this command: 

    conda update --channel conda-forge conda --name webscrapers

    # To update the "conda" package in the "base" conda environment:
    conda update --name base --channel conda-forge conda 


TODO: FUTURE - to add and use Pytorch for machine learning (features to be added)
  You can install PyTorch using pip or conda. Here's how you can do it:

    Using pip: pip install torch torchvision torchaudio

    Using conda: conda install pytorch torchvision torchaudio -c pytorch

    These commands will install PyTorch along with torchvision (a package with popular datasets, model architectures, and common image transformations for computer vision) and torchaudio (similar to torchvision, but for audio).

  Remember to activate your virtual environment before installing, if you're using one. 
  Also, ensure that your Python and pip versions are up-to-date.
  # All requested packages already installed.

  (webscrapers) C:\Users\Nadia Stoyanova>conda install pytorch torchvision torchaudio -c pytorch
  Channels:
  - pytorch
  - conda-forge
  - defaults
  Platform: win-64
  Collecting package metadata (repodata.json): done
  Solving environment: done

  ## Package Plan ##

    environment location: C:\ProgramData\Anaconda3\envs\webscrapers

    added / updated specs:
      - pytorch
      - torchaudio
      - torchvision

# PROBLEMS SOLVED:
TODO: DONE:  
###I received the following error: (webscrapers) C:\Users\Nadia Stoyanova>conda install -c conda-forge BeautifulSoup Channels:

    conda-forge
    defaults Platform: win-64 Collecting package metadata (repodata.json): done Solving environment: failed
    PackagesNotFoundError: The following packages are not available from current channels:

    beautifulsoup
    Current channels:

    https://conda.anaconda.org/conda-forge
    defaults
    To search for alternate channels that may provide the conda package you're looking for, navigate to
    https://anaconda.org
    and use the search bar at the top of the page.

    The error message indicates that the package BeautifulSoup cannot be found in the conda channels you are using. The correct package name for BeautifulSoup in conda is beautifulsoup4, not BeautifulSoup.

    You can install it using the following command:

    ```conda install -c conda-forge beautifulsoup4```

    This command tells conda to install the beautifulsoup4 package from the conda-forge channel.
