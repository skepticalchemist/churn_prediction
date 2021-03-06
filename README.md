# The importance of customer churn prediction

According to the Leo Vegas CEO, Gustaf Hagman (see the picture below), in 2018 the overall revenue of the company was around €360 million. Considering that online gambling is only 10% of the total gambling and that there is an increasing trend in everything going online the perspective of growing is promising.

![cassino revenue source H2CG](assets/revenues.jpg)

In this growing market keeping customers satisfied is paramount so they continue using the product. In this scenario, customer churn prediction is a very reasonable alternative to approach customer retention based on its past behavior.


# Task

From a dataset containing daily aggregations for around 10k customers who signed up during a calendar year define the prediction target and
create a predictive model that you would be comfortable sharing with a hypothetical stakeholder. 

# Solution
After an initial exploratory data analysis and feature engineering, the probabilities generated by the model BG-NBD were used to define the target variable (churn/not churn). To predict customer churn 5 models were build, compared and evaluated. The final criteria to choose the model was a trade-off between performance and explainability. 

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

# Execution sequence

The notebooks should be executed in the following order:
1. _eda.ipynb_: 
   - performs an exploratory data analysis    
2. _feature_eng.ipynb_:
   - performs feature engineering
3. _bg-nbd_model.ipynb_:
   - implements the model BG-NBD
4. _target_definition.ipynb_:
   - uses the results from the model BG-NBD to define the target variable
5. _model_building.ipynb_:
   - build, select and evaluate the model
6. _model_building_reduced_features.ipynb_:
   - remove some features, build, select and evaluate the model



# Directory structure or the repository

```bash
.
├── assets
├── data
├── .ipynb_checkpoints
├── models
├── notebooks
├── README.md
├── references
├── reports
├── requirements.txt
└── src
```
