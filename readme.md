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
		⁃ Create calculated columns from existing data:
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
|:--------|:-----------|
|phone_service| Indicates if a customer is subscribed for phone service |
|multiple_lines| If a customer subscribed for phone service has multiple lines.|
|online_security| If a customer is subscribed for online security service |
|online_backup|  If a customer is subscribed for online backup service |
|device_protection|  If a customer is subscribed for device protection service |
|tech_support|  If a customer is subscribed for technical support service |
|streaming_tv|  If a customer is subscribed for streaming TV service |
|streaming_movies|  If a customer is subscribed for streaming movie service |
|churn_month|  If a customer has churned, this is the month they cancelled their service |
|paperless_billing| Indicates 1 if the customer subscribe to paperless_billing. |
|gender| The customer's biological sex |
|senior_citizen| Indicates 1 if the customer is described as a senior citizen. Cutoff age is unknown. |
|partner| Indicates 1 if the customer has a spouse. |
|dependents| Indicates 1 if the customer is relied upon by another human for financial support. |
|monthly_charges| Total charges on a monthly basis for all the services a customer is subscribed to.|
|total_charges| This is a sum of all the monthly charges a customer has paid during their tenure.|
|signup_date| The date on which the customer first signed up for services. |
|contract_type| Month-to-month, yearly and two-year contracts|
|internet_service_type| None, DSL and fiber optic |
|payment_type| Mailed check, electronic check, bank transfer and credit card. |
|churn (target)| Indicates 1 if the customer has cancelled all their subscriptions with Telco. |
|tenure| The number of months that a customer has been subscribed for services. |


# Steps to Reproduce:
1. Copy this repo.
2. Get credentials from Codeup to query their telco_churn dataset.
3. Ensure the acquire.py, prepare.py, env.py and telco_functions.py are in the same folder as the final notebook.
3. Run the final notebook.

# Takeaways:

- The customers table appears to be created from the other existing tables. The data in the customers.tenure column is suspicious when compared to a calculation of total_charges/monthly_charges. For this reason I did not use the customers table and created a new tenure column by dividing total_charges by monthly_charges.
- It appears the data was retrieved on 2022-01-31. This is also the date for all churn customers.
- Creating DataFrame of just churned customers and another of not churned customers was very useful. It shows the rate at which each feature occured in both groups. I focused on the top and bottom four.

# Conclusions:

Churn occurs at 27% in the Telco dataset. The drivers of churn are: 
- Having a month-to-month contract
- Not having tech support
- Not having online security
- Having fiber optic internet
- Low tenure/being a new customer
- Higher monthly charges

# Recommendations

- Evaluate pricing and quality of fiber optic internet service.
- Evaluate pricing and impact of tech support and online security.
- Incentivize Month-to-month and fiber optic customers to stay.
- Consider lowering prices for newer customers.
- Once churn decreases, evaluate pricing power on phone services and two year contracts.

# Next Steps
- Do statistical testing on the monthly_charges and total_charges features
- Create a way to automatically compare churn for continuous features
- Dig in deeper on features which have greater than 10% indication of churn.
- Evaluate fiber optic internet type to identify focus areas.
