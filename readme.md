# Project Description:

Telco has elevated levels of customers canceling their services or churning. It has tasked us with identifying the drivers of customer churn and producing recommendations on how to reduce it. 

# Goals:
	•	Find drivers for customer churn at Telco.
	•	Construct a ML classification model that accurately predicts customer churn.
	•	Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?
	•	Develop recommendations to reduce churn.

# Initial Thoughts:
	⁃	My initial hypothesis is that churn will be related to higher monthly costs. 
	⁃	The contract length could also be a driver.

# Project Planning (lay out your process through the data science pipeline)
	1.	Aquire data from the Codeup SQL database.
	2.	Prepare data
		⁃	Create calculated columns from existing data:
            ⁃ tenure
            - churn
	3.	Explore data in search of drivers.
		⁃	Answer the following initial questions:
			⁃	Does higher monthly costs contribute to more customer churn?
			⁃	Does any individual customer attribute contribute more to customer churn?
	4.	Develop a Model to predict if a customer will churn
		⁃	Use drivers identified in explore to build predictive models of different types.
		⁃	Evaluate models on train and validate data.
		⁃	Select the best model based on highest accuracy.
		⁃	Evaluate the best model on test data.
	5.	Draw Conclusions.


# Data Dictionary:

| Feature |	Definition |
| paperless_billing | Indicates 1 if the customer subscribe to paperless_billing. |
| senior_citizen | Indicates 1 if the customer is described as a senior citizen. Cutoff age is unknown. |
| partner | Indicates 1 if the customer has a spouse. |
| dependents | Indicates 1 if the customer is relied upon by another human for financial support. |
| monthly_charges | Total charges on a monthly basis for all the services a customer is subscribed to.|
| total_charges | This is a sum of all the monthly charges a customer has paid during their tenure.|
| churn | Indicates 1 if the customer has cancelled all their subscriptions with Telco. |
| tenure | The amount of time in months that a customer has been subscribed for services. |


# Steps to Reproduce:
1. Copy this repo.
2. Get credentials from Codeup to query their telco_churn dataset.
3. Run the notebook.

# Takeaways:

- The customers table appears to be created from the other existing tables. The data in the customers.tenure column is suspicious when compared to a calculation of total_charges/monthly_charges. For this reason I did not use the customers table and created a new tenure column by dividing total_charges by monthly_charges.
- It appears the data was retrieved on 2022-01-31.
- Creating DataFrame of just churned customers and another of not churned customers was very useful. Comparing it to the baseline indicated which categorical features might be drivers of churn. I focused on the top four.

# Conclusions:

Churn occurs at 26.5% in the Telco dataset. The drivers of churn are: 
- having a month-to-month contract 
- having fiber optic internet 
- low tenure/being a new customer

# Recommendations:

- Incentivize Month-to-month and fiber optic customers to stay.
- Consider lowering prices for newer customers.
- Once churn decreases, evaluate pricing power on phone services and possibly raise rates.