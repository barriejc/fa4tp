# Files: Financial Analysis for Technical Professionals

## Sheet

The presentation model was created in Google Sheets and exported to the .xlsx file you see here.  It should be a simple matter to import back into your Google Sheets account, but do please contact me if you run into any issues.  I did notice that importing it back to Mac Numbers, for one thing, did not preserve a few formulas, and the chart looks really weird. If the Montserrat font is not already installed locally, that may also be an issue.

## Python

These scripts assume certain libraries are installed, so running it in the supplied virtual environment is recommended unless you prefer to install them yourself.  

1. Clone the git archive from the directory on your machine where you want these files to reside:

```
    git clone git@github.com:barriejc/faftp.git
```

2. cd to that directory, activate the venv, and install according to the requirements:

```
    python3 -m venv virt
    source virt/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
```
