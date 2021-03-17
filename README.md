_____
# Case

## Introduction

Customer churn is a problem that concerns arguably all customer-oriented
businesses. Gambling operators are not an exception. In the effort of improving
retention, it is needed to identify players who are likely to leave soon so that
the CRM team can try to keep them engaged by sending relevant offers.

## Task

At your disposal, there is a dataset containing daily aggregations for around
10k customers who signed up during a calendar year.

Define the prediction target however you see fit and illustrate your workflow of
creating a predictive model that you would be comfortable sharing with a
hypothetical stakeholder. Feel free to use any tools and packages that you
consider appropriate for the job.

You are not supposed to spend more than a few hours. Make justified trade-offs
so that you complete in a reasonable time. The solution might not be ideal. The
most important is that it is functional and adequate for the time given.
___________________________

# The importance of customer churn prediction

According to the Leo Vegas CEO, Gustaf Hagman (see the picture below), in 2018 the overall revenue of the company was around €360 million. Considering that online gambling is only 10% of the total gambling and that there is an increasing trend in everything going online the perspective of growing is promising.

![cassino revenue source H2CG](assets/revenues.jpg)

In this growing market keeping customers satisfied is paramount so they continue using the product. In this scenario, customer churn prediction is a very reasonable alternative to approach customer retention based on its past behavior.


# Setup

## Setup a conda environment

Create and activate a conda environment of your choice, here I call it churn_lv:

```python
conda create --name churn_lv python==3.8
conda activate churn_lv
```


## Install the packages through the command

```python
pip install -r requirements.txt
```

# Directory structure or the repository

```bash
.
├── assets
│   └── revenues.jpg
├── data
│   └── data.csv
├── .gitignore
├── .ipynb_checkpoints
│   ├── eda-checkpoint.ipynb
│   ├── README-checkpoint.md
│   └── requirements-checkpoint.txt
├── models
├── notebooks
│   ├── eda.ipynb
│   ├── .ipynb_checkpoints
│   │   ├── eda-checkpoint.ipynb
│   │   └── tests-checkpoint.ipynb
│   └── tests.ipynb
├── README.md
├── references
│   ├── 2010_Braverman_behavioral_markers.pdf
│   └── 2013_Coussement_churn_prediction.pdf
├── reports
│   ├── eda_report.html
│   ├── gender_report.html
│   └── .ipynb_checkpoints
└── requirements.txt
```
