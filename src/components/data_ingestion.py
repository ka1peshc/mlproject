import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#Generally to define a class we need __init__ method.
#instead we can use dataclass.
@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join("artifacts","train.csv")
    test_data_path: str= os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join('artifacts','data.csv')

#Not using dataclass annotation coz class contain methods
#In above class only variable is created.
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() #this variable will contain above variable.
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            #Read the dataset from somewhere
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #convert raw data into csv file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            #Create train test part
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            #Save train and test data file
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed.")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj=DataIngestion()       
    obj.initiate_data_ingestion()