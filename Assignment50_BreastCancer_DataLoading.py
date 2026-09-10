import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer

#-------------------------------------------------------
# Step 1. Load and Explore the Dataset
#-------------------------------------------------------

def DataLoad():
    Border = "-"* 40
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
    
def main():
    
    DataLoad()
    
if __name__ =="__main__":
    main()
    