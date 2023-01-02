import os
import pandas as pd
import numpy as np
from env import get_connection

"""
This is how you get rid of the Unnamed: 0 column:

#read_csv(filename, index_col=0)
#to_csv(filename, index=False)
"""


def get_telco_data():
    """
    This function reads the telco_churn data from Codeup db into a df.
    """
    filename = "telco_churn.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        
        # read the SQL query into a dataframe
        query = """
        SELECT * FROM customer_subscriptions
        LEFT JOIN customer_churn USING (customer_id)
        LEFT JOIN customer_contracts USING (customer_id)
        LEFT JOIN customer_details USING (customer_id)
        LEFT JOIN customer_payments USING (customer_id)
        LEFT JOIN customer_signups USING (customer_id)
        LEFT JOIN contract_types USING (contract_type_id)
        LEFT JOIN internet_service_types USING (internet_service_type_id)
        LEFT JOIN payment_types USING (payment_type_id);
        """
        df = pd.read_sql(query, get_connection('telco_churn'))
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)
        
        # Return the dataframe to the calling code
        return df