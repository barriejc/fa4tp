# Files: Financial Analysis for Technical Professionals

## Sheet

The presentation model was created in Google Sheets and can be viewed (and downloaded for your reference) here:

[N96 FA4TP Example Sheet](https://docs.google.com/spreadsheets/d/1ANT_R3B1NYzPFVfDnPtmJveB-kTi0xej5_E-n1X8ptI)

There are also exports to .xlsx and .ods here that may or may not work well. Importing the .xlsx back to Mac Numbers, for one thing, did not preserve a few formulas, and the chart looks really weird. If the Montserrat font is not already installed locally, that may also be an issue for both the linked sheet and the exports.

## Python

These scripts assume certain libraries are installed, so running it in the supplied virtual environment is recommended unless you prefer to install them yourself.  

1. Clone the git archive from the directory on your machine where you want these files to reside:

```
    git clone git@github.com:barriejc/fa4tp.git
```

2. cd to that directory, activate the venv, and install according to the requirements:

```
    python3 -m venv virt
    source virt/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
```
