import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object

@dataclass # used for class within only define variables. But if you have other functions inside go ahead with normal class __init__
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformer_object(self):#create the model preprocessor to handle missing values, onehot, scaler
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course"]
            num_pipeline=Pipeline(
               steps=[
                   ("imputer",SimpleImputer(strategy="median")),#handling missing values
                   ("scaler",StandardScaler(with_mean=False))
               ]               
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical columns scaling completed")
            logging.info("Categorical columns encoding completed")
            
            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
                                
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_path,test_path):#use the model preprocessor on dataset to handle missing values, onehot, scaler and have a final train and test dataset. It isn't still divided into X_train etc
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data completed")
            
            logging.info("Obtaining preprocessing object")
            
            preprocessing_obj=self.get_data_transformer_object()
            
            target_column_name="math_score"
                        
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            input_feature_train_array=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array=preprocessing_obj.transform(input_feature_test_df)
            
            train_array=np.c_[
                input_feature_train_array,np.array(target_feature_train_df)
            ]            
            test_array=np.c_[input_feature_test_array,np.array(target_feature_test_df)]
            logging.info(f"Saved preprocessing object")
            #np.c_ 
            #a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #features
            #b = np.array([10, 11, 12]) #target
            #c = np.c_[a, b]
            #[[ 1  2  3 10]
            #[ 4  5  6 11]
            #[ 7  8  9 12]]
            
            save_object( # Saving the preprocessor pickle file
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return(
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys)
            
        
