import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

#-------------------------------------------------------
# Step 1. Load and Explore the Dataset
#-------------------------------------------------------

Border = "-"* 40

def DataLoad():
    
    global df
    global X
    global Y
    
    print(Border)
    print("Step 1. Load and Explore the Dataset")
    print(Border)

    data = load_breast_cancer()

    df = pd.DataFrame(data.data, columns=data.feature_names)

    print("Shape of Dataset :", data.data.shape)

    X = data.data
    Y = data.target

    print("Shape of X :", X.shape)
    print("Shape of Y :", Y.shape)

    print(Border)
    print("First Five Record")
    print(Border)
    print(df.head())
    
    print(Border)
    print("Columns Names")
    print(Border)
    print(df.columns)
    
    print(Border)
    print("Information about dataset")
    print(Border)
    print(df.info)

    print(Border)
    print("Statistical information")
    print(Border)
    print(df.describe())
    
    #---------------------------------------------------------------------
    # The Breast Cancer dataset is loaded using load_breast_cancer() from Scikit-learn. 
    # The dataset is converted into a Pandas DataFrame for easy analysis. 
    # The dataset is explored by checking its first and last records, shape,
    # feature names, data types, statistical summary.
    #---------------------------------------------------------------------
    
#----------------------------------------------------------------------
# Step 2. Data Preprocesing
#----------------------------------------------------------------------
    
def Preprocess():

    print(Border)
    print("Step 2. Data Preprocesing")
    print(Border)
    
    #--------------------------------
    # Handle Missing Values 
    #--------------------------------
    
    print("Missing Values")
    print(df.isnull().sum())
    
    if df.isnull().sum().sum()== 0:
        print("No missing values are present in dataset")
    else:
        print("Missing values are present. Handling them...")
        df.fillna(df.mean(numeric_only=True),inplace=True)
        print("Missing values have been handled.")
    print(Border)
    #--------------------------------
    # Normalize or ScaleFeatures 
    #--------------------------------
    
    scalar = StandardScaler()
    
    X_scaled = scalar.fit_transform(X)
    
    print("Original Shape :", X.shape)
    print("Scaled Shape   :", X_scaled.shape)

    print("First Five Records After Scaling:")
    print(Border)
    print(X_scaled[:5])
    
def main():
    
    DataLoad()
    
    Preprocess()
    
if __name__ =="__main__":
    main()
    