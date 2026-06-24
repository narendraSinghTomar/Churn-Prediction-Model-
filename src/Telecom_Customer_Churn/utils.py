import os 
import sys
from src.Telecom_Customer_Churn.exception import CustomException
from src.Telecom_Customer_Churn.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL databse Stated ")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            ssl_disabled=True 
        )
        logging.info( "Connection Established",mydb)
        df=pd.read_sql_query("Select*from telecom_customer_churn",mydb)
        print(df.head())

        return df 

        
    except Exception as ex:
        raise CustomException(ex,sys)