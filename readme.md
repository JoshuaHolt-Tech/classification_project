# 📞 Project Overview: Unraveling the Mystery of Customer Churn at Telco 📊

Telco has elevated levels of customers canceling their services or churning. I am tasked with identifying the drivers of customer churn and producing recommendations on how to reduce it. 

**🚀 The Challenge**: Telco, a leading telecommunications company, is grappling with an increasing rate of customer churn. They've turned to me to unravel the mystery behind this trend and devise strategies to curb it. 

**🎯 Mission**: To identify the key factors driving customer churn at Telco and build a machine learning model that accurately predicts customer churn. I aim to present the findings in a comprehensive report that anyone, even those without a data science background, can understand and act upon.

**💡 Hypothesis**: I suspect that churn might be linked to higher monthly costs and the length of the contract. But let's dive in and see what the data tells us!

# 📋 Game Plan:

1. **Data Acquisition**: Fetch data from the Codeup SQL database.
2. **Data Preparation**: Create calculated columns from existing data, such as tenure and churn.
3. **Data Exploration**: Investigate potential drivers of churn. I will be asking questions like: Does higher monthly cost contribute to more customer churn? Does any individual customer attribute contribute more to customer churn?
4. **Model Development**: Build and evaluate various predictive models using the identified drivers. The best model will be selected based on its accuracy.
5. **Conclusion**: Draw insights and make recommendations based on my findings.

# 📚 Data Dictionary: Your Guide to the Dataset

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


Want to dive into the data yourself? Here's how:

1. Clone this repo.
2. Get credentials from Codeup to query their telco_churn dataset.
3. Ensure the acquire.py, prepare.py, env.py, and telco_functions.py are in the same folder as the final notebook.
4. Run the final notebook.

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
