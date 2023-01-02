Project Description:

Telco has elevated levels of customers canceling their services or churning. It has tasked us with identifying the drivers of customer churn and producing recommendations on how to reduce it. 

Goals:
	•	Find drivers for customer churn at Telco.
	•	Construct a ML classification model that accurately predicts customer churn.
	•	Deliver a report that a non-data scientist can read through and understand what steps were taken, why and what was the outcome?
	•	Develop recommendations to reduce churn.

Initial Thoughts:
	⁃	My initial hypothesis is that churn will be related to higher monthly costs. 
	⁃	The contract length could also be a driver.

Project Planning (lay out your process through the data science pipeline)
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


Data Dictionary:
Feature					Definition
churn                   1 or 0 for if the customer has churned or not.
tenure                  Time in months that services have been rendered. Calucated by total_charges/monthly_charges and rounded to a whole number.


Steps to Reproduce:

Takeaways and Conclusions:

- The customers table appears to be created from the other existing tables. The customers.tenure column data integrity is suspicious when compared to a calculation of total_charges/monthly_charges. For this reason I did not use the customers table.
- It appears the data was retrieved on 2022-01-31.

Recommendations:
