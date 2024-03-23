import sys

# Construct an absolute path to the script
script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'scraping_jobs.py')

# Call the script using the Python interpreter
subprocess.call([sys.executable, script_path])

"""
    
     instead of subprocess.call("../../notebooks/scraping_jobs.py", shell=True)
    """
 
""" os.path.dirname(__file__) gets the directory containing 
the current script, and os.path.join constructs the path to scraping_jobs.py 
relative to that."""
