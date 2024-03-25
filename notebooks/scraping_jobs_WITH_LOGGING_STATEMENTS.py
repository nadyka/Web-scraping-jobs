#! /usr/bin/env python3
# coding: utf-8

import os
import datetime
import json, csv
import pandas as pd 
import numpy as np
import requests
from bs4 import BeautifulSoup
import iso3166
from geopy.geocoders import Nominatim
from functools import partial
import numpy as np
import webbrowser
import datetime
from datetime import date
import logging

# Configure logging
log_filename = f"run_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')

# Global variable
LI_AT_COOKIE = "ENTER YOUR LI AT COOKIE"

# Displaying the full text of a pandas DataFrame (with none of its values truncated).
pd.set_option("display.max_colwidth", -1)

# ... (rest of your import statements and global variables)

def convert_csv2json(csv_filename, json_filename):
    logging.info('Starting convert_csv2json function')
    # ... (rest of your function code)
    logging.info('Finished convert_csv2json function')

# ... (rest of your functions)

def scrape_jobs(jobs_parameters):
    logging.info('Starting scrape_jobs function')
    # ... (rest of your function code)
    logging.info('Finished scrape_jobs function')
    return df_jobs

# ... (rest of your functions)

if __name__ == "__main__":
    logging.info('Starting main execution')

    # Clean and create processed geoId csv file
    geoId_csv = "../../data/raw/geoId.csv"
    geoId_csv_processed = geoId_csv.replace('raw', 'processed')

    if not os.path.isfile(geoId_csv_processed):
        df_geoId = clean_data_geoId(geoId_csv)
        logging.info('Finished cleaning and creating processed geoId csv file')
    else:
        logging.info('Processed geoId csv file already exists')
        df_geoId = read_data(geoId_csv_processed)

    # Scraping parameters
    json_jobs_parameters = "../../data/jobs_parameters_user_request.json"
    jobs_parameters = read_jobs_parameters(json_jobs_parameters)
    logging.info('Finished reading jobs parameters user request')

    df_jobs = scrape_jobs(jobs_parameters)

    # Save jobs as csv file
    filename_csv = "../../data/jobs.csv"
    save_df2csv(df_jobs, filename_csv)
    logging.info('Finished saving jobs as csv file')

    # Save jobs as json file
    csv_filename = filename_csv
    json_filename = filename_csv.replace("csv","json")
    convert_csv2json(csv_filename, json_filename)
    logging.info('Finished saving jobs as json file')

    logging.info('Finished main execution')