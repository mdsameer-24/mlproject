import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from mlproject.logger import logging
from mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv

import pickle
import numpy as np
import pymysql

load_dotenv()
host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')


def read_sql_data():
    logging.info("reading sql database started")
    try:
        mydb=pymysql.connect(
             host=host,
             user=user,
             password=password,
             db=db
        )
        logging.info("Completed Established ",mydb)
        df=pd.read_sql_query('select * from students',mydb)

        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e)
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
