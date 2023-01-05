import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from prepare import train_validate

def get_pie(train):
    """
    Gets a pie chart for churn
    """
    #Set values and labels for chart
    values = [len(train[train.churn == 1]), len(train[train.churn == 0])]
    labels = ['Churn', 'No Churn']
    
    #Generate and show chart
    plt.pie(values,labels=labels, autopct='%.0f%%')
    plt.title("Customers who churn versus those who don't")
    plt.show()

def ind_of_churn(train):
    """
    This function takes in the train dataframe, calculates predictors
    of churn for categorical columns and returns two dataframes. One for
    indicators of churn and one of indicators of anti-churn.
    """
    #Split df by customers who churned and those who did not
    no_churn = train[train.churn == 0]
    churn_df = train[train.churn == 1]

    #Removing target and non categorical columns
    cols_to_drop = ['monthly_charges', 'tenure', 'total_charges', 'churn']
    churn_df.drop(columns=cols_to_drop, inplace = True)
    no_churn.drop(columns=cols_to_drop, inplace = True)
    
    #Printing a comparison between the baseline and the churn/no_churn DataFrames:
    distros = []
    for item in churn_df:
        bl = round(sum(train[item]) / len(train[item]) * 100,1)
        churn = round(sum(churn_df[item]) / len(churn_df[item]) * 100,1)
        no_c = round(sum(no_churn[item]) / len(no_churn[item]) * 100,1)

        output = {"Column" : item,
                  "Churn %": churn, 
                  "Churn Diff %": churn - bl, 
                  "Baseline %" : bl , 
                  "No_Churn Diff %": no_c - bl, 
                  "Not Churn %": no_c,
                  "Churn Indication %":(churn - bl) + (no_c - bl) }

        distros.append(output)
    dis_df = pd.DataFrame(distros)              
    dis_df = dis_df.set_index('Column')
    churn_ind = dis_df.sort_values("Churn Indication %", ascending=False).head(4)
    anti_churn = dis_df.sort_values("Churn Indication %", ascending=True).head(4)
    return churn_ind, anti_churn

def charges_chart(train):
    """
    Builds a plot to show a relationship 
    between tenure, monthly_charges and churn
    """
    sns.scatterplot(data = train, 
                    y = 'tenure', 
                    x = 'monthly_charges', 
                    hue='churn')
    month_ave = train.monthly_charges.mean()
    tenure_ave = train.tenure.mean()
    plt.axhline(tenure_ave, label="Tenure Average", c='tomato')
    plt.axvline(month_ave, label="Monthly Charges Average", c='tomato')

def q_1_viz(train):
    """
    Builds a plot to show a relationship between churn and customers
    with a month-to-month contract.
    """
    plt.title("It pays to be more committed")
    sns.barplot(x='contract_type_Month-to-month', y='churn', data=train)
    pop_churn_rate = train.churn.mean()
    plt.axhline(pop_churn_rate, label="Population churn rate")
    plt.legend()
    plt.show()
    
def q_2_viz(train):
    """
    Builds a plot to show a relationship between fiber optic internet
    and churn.
    """
    plt.title("Fiber optic internet drives customers away")
    sns.barplot(x='internet_service_type_Fiber optic', y='churn', data=train)
    pop_churn_rate = train.churn.mean()
    plt.axhline(pop_churn_rate, label="Population churn rate")
    plt.legend()
    plt.show()
    
def q_3_viz(train):
    """
    Builds a plot to show the relationship between not having
    tech support and churn.
    """
    plt.title("Customers that stay have support (tech)")
    sns.barplot(x='tech_support_No', y='churn', data=train)
    pop_churn_rate = train.churn.mean()
    plt.axhline(pop_churn_rate, label="Population churn rate")
    plt.legend()
    plt.show()
    
def q_4_viz(train):
    """
    Builds a plot to show the relationship between no internet
    service and churn.
    """
    plt.title("No internet = no churn")
    sns.barplot(x='internet_service_type_None', y='churn', data=train)
    pop_churn_rate = train.churn.mean()
    plt.axhline(pop_churn_rate, label="Population churn rate")
    plt.legend()
    plt.show()