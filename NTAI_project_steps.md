# Jobs Finder Webcraper Project Planning

## Project Action Items TBD (Next Steps): 
### Document the Webscrapers project steps:

TODO: add other people from the AI-powered training group. 



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
