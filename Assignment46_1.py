import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , r2_score
from sklearn.model_selection import train_test_split

def MarvellousRegression(Datapath):
    
    Border= "-"*60
    
    ##########################################
    # Step 1 : Load the Dataset
    ##########################################

    print(Border)
    print(" Step 1 : Load the Dataset")
    df = pd.read_csv(Datapath)
    
    print(Border)
    print(df.head())
    print(Border)
    
    ##########################################
    # Step 2 : Clean, Manipulate and Prepare data
    ##########################################
    
    print("Step 2 : Clean, Manipulate and Prepare data")
    
    if "Unnamed: 0" in df.columns:
        df= df.drop(columns=['Unnamed: 0'])
        
    print(Border)
    print(df.head())
    print(df.isnull().sum())
    print(Border)
    
    ##########################################
    # Step 3 : Train the Data
    ##########################################

    print( "Step 3 : Train the Data")
    
    
    X = df[["TV", "radio", "newspaper"]]   
    Y =  df["sales"]
    
    X_train , X_test, Y_train, Y_test = train_test_split(X,Y, train_size= 0.50, random_state=42)
    
    model = LinearRegression()
    
    model = model.fit(X_train,Y_train)
    
    print("Model Trained Succesfully")
    print(Border)
    
    ##########################################
    # Step 4 : Test the Data
    ##########################################
    
    print("Step 4 : Test the Data")
    
    Y_pred = model.predict(X_test)
    
    print("Model Testing is succesfully completed ")
    print(Border)
    
    ##########################################
    # Step 5 : Test the data 
    ##########################################
    
    print("Expected Value :", Y_test[:6])
    
    print("Predicted value :", Y_pred[:6])
    
def main():
    
    MarvellousRegression("Advertising.csv")
    
if __name__ == "__main__":
    main()
