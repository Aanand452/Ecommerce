import numpy as np
import pandas as pd


def ecommerce():
    ecommerce_df = pd.read_csv(
        "/Users/anandkumar/Downloads/data/Ecommerce.csv")
    print(ecommerce_df)

    # before analyze the data, should expolre the data

    print(ecommerce_df.shape)

    print(ecommerce_df.columns)

    print(ecommerce_df.count())

    print(ecommerce_df.value_counts)

    print(ecommerce_df[ecommerce_df.duplicated('Purchase Price')])
    print(ecommerce_df.sort_values(by='Language', ascending=True))

    # Display Top 10 rows of the data set
    print(ecommerce_df.head(10))

    # Display Last 10 Rows of the Dataset
    print(ecommerce_df.tail(10))

    # Check datatype of each column
    print(ecommerce_df.dtypes)

    # check Null values In the Dataset
    print(ecommerce_df.count())
    print(ecommerce_df.isnull().sum())

    # How many Rows and Columns Are There in Our Dataset
    print(ecommerce_df.shape)
    print(len(ecommerce_df.columns))
    print(len(ecommerce_df))
    print(ecommerce_df.info())

    # What is the purchase price of high and low
    print(ecommerce_df['Purchase Price'].max())
    print(ecommerce_df['Purchase Price'].min())

    # Average Purchase Price
    print(ecommerce_df['Purchase Price'].mean())

    # How Many People Have French 'fr' As their language?
    print(ecommerce_df.columns)

    print(ecommerce_df[ecommerce_df.Language == 'fr'])

    # Job Title Contains Engineer

    print(ecommerce_df[ecommerce_df['Job'].str.contains(
        'engineer', case=False)])

    # Find Email of the person With The Following IP address:

    print(ecommerce_df.columns)
    print(ecommerce_df[ecommerce_df['IP Address']
          == "132.207.160.22"]['Email'])
    print(ecommerce_df.dtypes)

    # How Many People Have MasterCard As Their Credit Card Provider And Made A Purchase Above 50?

    print(ecommerce_df[(ecommerce_df['CC Provider'] == "Mastercard") & (
        ecommerce_df['Purchase Price'] > 50)])

    # Find Email of the Person With The Follwoing Credit Card Number:4664825258997302
    print(ecommerce_df.dtypes)
    print(ecommerce_df[ecommerce_df['Credit Card']
          == 4664825258997302]["Email"])

    # How Many People Purchase During The AM and How Many People Purchase During PM?
    print(ecommerce_df["AM or PM"].value_counts())

    # How Many People Have A credit Card That Expires in 2020?
    print(ecommerce_df.columns)
    print(ecommerce_df["CC Exp Date"].isin("2020"))

    # 1 method
    def fun():
        count = 0
        for date in ecommerce_df['CC Exp Date']:
            if date.split('/')[1] == '20':
                count = count+1
            print(count)
    fun()

    # 2nd method
    print(ecommerce_df[ecommerce_df['CC Exp Date'].apply(
        lambda x: x[3:] == '20')])

    # Top 5 Most Popular Email providers(e.g gmail,yahoo,etc..)
    print(ecommerce_df['Email'].unique())

    list1 = []
    for email in ecommerce_df['Email']:
        list1.append(email.split('@')[1])

    ecommerce_df['temp'] = list1

    print(ecommerce_df['temp'].value_counts())

    print(ecommerce_df['Email'].apply(
        lambda x: x.split('@')[1]).value_counts().head())


ecommerce()
