import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy import stats
from prepare import train_validate

#Tools to build machine learning models and reports
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

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
    churn_df = train[train.churn == 1]
    no_churn = train[train.churn == 0]

    #Removing target and non categorical columns
    cols_to_drop = ['churn', 'monthly_charges', 'total_charges', 'tenure', 'customer_id']

    churn_df.drop(columns=cols_to_drop, inplace = True)
    no_churn.drop(columns=cols_to_drop, inplace = True)

    
    #Printing a comparison between the baseline and the churn/no_churn DataFrames:
    distros = []
    for item in churn_df:
        churn = round((churn_df[item].mean()) * 100,1)
        no_c = round((no_churn[item].mean()) * 100,1)

        output = {"Column" : item,
                  "Churn %": churn,    
                  "Not Churn %": no_c,
                  "Churn Indication":(churn - no_c) }

        distros.append(output)
    dis_df = pd.DataFrame(distros)              
    dis_df = dis_df.set_index('Column')
    churn_ind = dis_df.sort_values("Churn Indication", ascending=False).head(4)
    anti_churn = dis_df.sort_values("Churn Indication", ascending=True).head(4)
    return churn_ind, anti_churn, dis_df

def viz_ind_churn(dis_df):
    """
    This function plots a list of features and their contribution to churn.
    """
    my_range=range(1,len(dis_df.index) + 1)
    # Builds the chart
    plt.figure(figsize=(4,10))
    plt.scatter(dis_df['Churn Indication'], my_range, color='green', alpha=0.8 , label='Churn Indication')
    plt.axvline(0, c='tomato')
    plt.legend()

    # Add title and axis names
    plt.yticks(my_range, dis_df.index)
    plt.title("Drivers of Churn", loc='center')
    plt.xlabel('Anti-Churn= -100      Occures Evenly = 0      Churn= 100')
    plt.ylabel('Feature')

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
    plt.title("Customers stay when they are more committed")
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

def get_chi_m2m(train):
    """
    Does a chi^2 test on churn and month-to-month contract customers.
    """
    
    # Let's run a chi squared to compare proportions, to have more confidence
    alpha = 0.05
    null_hypothesis = "customers with Month-to-month contracts and that churn are independent."
    alternative_hypothesis = "there is a relationship between customers with Month-to-month contracts and that churn."

    # Setup a crosstab of observed churn to contract_type_Month-to-month
    observed = pd.crosstab(train.churn, train['contract_type_Month-to-month'])

    chi2, p1, degf, expected = stats.chi2_contingency(observed)
    
    #Answer logic
    if p1 < alpha:
        print("Reject the null hypothesis that", null_hypothesis)
        print("")
        print("Sufficient evidence to move forward understanding that", alternative_hypothesis)
        print("")
    else:
        print("Fail to reject the null")
        print("Insufficient evidence to reject the null")
    print(f'The associated p-value is: {p1}')
    
def get_chi_fo(train):
    """
    Runs the chi^2 test on the dataframe column that has internet_service_type_Fiber optic and churn to see if there is a relationship.
    """
    
    # Let's run a chi squared to compare proportions, to have more confidence
    alpha = 0.05
    null_hypothesis = "customers with fiber optic internet service and that churn are independent."
    alternative_hypothesis = "there is a relationship between customers with fiber optic internet service and that churn."

    # Setup a crosstab of observed churn to internet_service_type_Fiber optic
    observed = pd.crosstab(train.churn, train['internet_service_type_Fiber optic'])

    chi2, p2, degf, expected = stats.chi2_contingency(observed)

    #Answer logic
    if p2 < alpha:
        print("Reject the null hypothesis that", null_hypothesis)
        print("")
        print("Sufficient evidence to move forward understanding that", alternative_hypothesis)
        print("")

    else:
        print("Fail to reject the null")
        print("Insufficient evidence to reject the null")
    print(f'The associated p-value is: {p2}')

    
def get_chi_ts(train):
    """
    Runs the chi^2 test on the dataframe column that has tech_support_No and churn to see if there is a relationship.
    """
    # Let's run a chi squared to compare proportions, to have more confidence
    alpha = 0.05
    null_hypothesis = "customers who don't have tech support and that churn are independent."
    alternative_hypothesis = "there is a relationship between customers who don't have tech support and that churn."

    # Setup a crosstab of observed churn to payment_type_Electronic check
    observed = pd.crosstab(train.churn, train['tech_support_No'])

    chi2, p3, degf, expected = stats.chi2_contingency(observed)

    #Answer logic
    if p3 < alpha:
        print("Reject the null hypothesis that", null_hypothesis)
        print("")
        print("Sufficient evidence to move forward understanding that", alternative_hypothesis)
        print("")

    else:
        print("Fail to reject the null")
        print("Insufficient evidence to reject the null")
    print(f'The associated p-value is: {p3}')

def get_chi_ni(train):
    """
    Runs the chi^2 test on the dataframe column that has internet_service_type_None and churn to see if there is a relationship.
    """
    # Let's run a chi squared to compare proportions, to have more confidence
    alpha = 0.05
    null_hypothesis = "customers with no internet service and that churn are independent"
    alternative_hypothesis = "there is a relationship between customers with no internet service and that churn"

    # Setup a crosstab of observed churn to having no internet service
    observed = pd.crosstab(train.churn, train['internet_service_type_None'])

    chi2, p4, degf, expected = stats.chi2_contingency(observed)

    #Answer logic
    if p4 < alpha:
        print("Reject the null hypothesis that", null_hypothesis)
        print("")

        print("Sufficient evidence to move forward understanding that", alternative_hypothesis)
        print("")

    else:
        print("Fail to reject the null")
        print("Insufficient evidence to reject the null")
    print(f'The associated p-value is: {p4}')

def train_val_test(train, val, test):
    """
    Seperates out the target variable and creates a series with only the target variable to test accuracy.
    """
    #Seperating out the target variable
    X_train = train.drop(columns=['churn', 'customer_id'])
    y_train = train.churn

    X_val = val.drop(columns = ['churn', 'customer_id'])
    y_val = val.churn

    X_test = test.drop(columns = ['churn', 'customer_id'])
    y_test = test.churn
    id_test = test.customer_id
    return X_train, y_train, X_val, y_val, X_test, y_test



def dec_tree(X_train, y_train, X_val, y_val):
    """
    This function runs the Decission Tree classifier on the training and validation test sets.
    """
    #Create the model
    clf = DecisionTreeClassifier(max_depth=3, random_state=1969)
    
    #Train the model
    clf = clf.fit(X_train, y_train)

    #Finding the Accuracy
    print(f'Accuracy of Decision Tree classifier on training set:   {clf.score(X_train, y_train):.4f}')
    print(f'Accuracy of Decision Tree classifier on validation set: {clf.score(X_val, y_val):.4f}')
    
def rand_forest(X_train, y_train, X_val, y_val):
    """
    This function runs the Random Forest classifier on the training and validation test sets.
    """
    #Creating the random forest object
    rf = RandomForestClassifier(bootstrap=True,
                                class_weight=None,
                                criterion='gini',
                                min_samples_leaf=3,
                                n_estimators=100,
                                max_depth=3,
                                random_state=1969)
    
    #Fit the model to the train data
    rf.fit(X_train, y_train)
    
    #Finding the Accuracy
    print(f'Accuracy of Random Forest classifier on training set:   {rf.score(X_train, y_train):.4f}')
    print(f'Accuracy of Random Forest classifier on validation set: {rf.score(X_val, y_val):.4f}')


def knn_mod(X_train, y_train, X_val, y_val):
    """
    This function runs the KNN classifier on the training and validation test sets.
    """
    #Creating the model
    knn = KNeighborsClassifier(n_neighbors=10, weights='uniform')

    #Fitting the KNN model
    knn.fit(X_train, y_train)

    #Finding the Accuracy
    print(f'Accuracy of KNN classifier on training set:   {knn.score(X_train, y_train):.4f}')
    print(f'Accuracy of KNN classifier on validation set: {knn.score(X_val, y_val):.4f}') 

def lr_mod(X_train, y_train, X_val, y_val):
    """
    This function runs the Logistic Regression classifier on the training and validation test sets.
    """
    #Creating a logistic regression model
    logit = LogisticRegression(random_state=1969)

    #Fitting the model to the train dataset
    logit.fit(X_train, y_train)

    #Finding the Accuracy
    print(f'Accuracy of Logistic Regression classifier on training set:   {logit.score(X_train, y_train):.4f}')
    print(f'Accuracy of Logistic Regression classifier on validation set: {logit.score(X_val, y_val):.4f}')
    
def final_test(X_train, y_train, X_test, y_test):
    """
    This function runs the Logistic Regression classifier on the final test set.
    """
    #Creating a logistic regression model
    logit = LogisticRegression(random_state=1969)

    #Fitting the model to the train dataset
    logit.fit(X_train, y_train)
    
    #Testing the final Accuracy
    print(f'Accuracy of Logistic Regression classifier on test set: {logit.score(X_test, y_test):.4f}')