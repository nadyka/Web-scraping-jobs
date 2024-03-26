import requests
from bs4 import BeautifulSoup

# URL to Indeed's search result page
url = "https://www.indeed.com/q-python-jobs.html"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all job cards
    job_cards = soup.find_all("div", class_="job_seen_beacon")

    for job in job_cards:
        # Extracting job information
        title = job.find("h2", {"class": "jobTitle"}).text.strip() if job.find("h2", {"class": "jobTitle"}) else "N/A"
        company_name = job.find("span", {"class": "companyName"}).text.strip() if job.find("span", {"class": "companyName"}) else "N/A"
        location = job.find("div", {"class": "companyLocation"}).text.strip() if job.find("div", {"class": "companyLocation"}) else "N/A"
        zip_code = "N/A" # Indeed does not typically list zip codes directly
        remote_check = "Remote" if "remote" in location.lower() else "On-site"
        type_of_employment = job.find("div", {"class": "job-snippet"}).text.strip() if job.find("div", {"class": "job-snippet"}) else "N/A"
        benefits = job.find("h2", {"id": "benefitsSectionTitle"}).find_next_sibling(text=True).strip() if job.find("h2", {"id": "benefitsSectionTitle"}) else "N/A"
        # The hiring manager's name is typically not listed on Indeed
        hiring_manager_name = "N/A"
        job_url = job.find("a", {"class": "jobtitle turnstileLink"})['href'] if job.find("a", {"class": "jobtitle turnstileLink"}) else "N/A"
        # Add other details following similar structure and checks
        
        # Printing extracted information
        print(f"Job Title: {title}")
        print(f"Company Name: {company_name}")
        print(f"Location: {location}")
        print(f"Zip Code: {zip_code}")
        print(f"Remote Check: {remote_check}")
        print(f"Type of Employment: {type_of_employment}")
        print(f"Benefits: {benefits}")
        print(f"Hiring Manager Name: {hiring_manager_name}")
        print(f"URL of the Job Posting: {job_url}")
        # Print other details as needed
        print("----")
else:
    print("Failed to retrieve the webpage")

#