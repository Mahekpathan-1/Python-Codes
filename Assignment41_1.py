import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def MarvellousClassifier(Datapath):
    Border = '-'* 40
    
    # Step 1 : Load the Dataset from csv file
    
    print(Border)
    print("Step 1 : Load the dataset")
    print(Border)
    
    df = pd.read_csv(Datapath)
    
    print(Border)
    print("Some entries from dataset")
    print(Border)
    print(df.head())
    print(Border)
    
    # Step 2 : Clean the Dataset 
     
    print(Border)
    print("Step 2 : Clean , Prepared and manipulate  Data")
    print(Border)
    
    df.dropna(inplace= True)
    
    print("Shape of dataset :", df.shape)
    print("Total records : ", df.shape[0])
    print("Total columns :", df.shape[1])
    print(Border)
    
    # Step 3 : Train data
         
    print(Border)
    print("Step 3 : Train data")
    print(Border)
    
    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2 , random_state=42)
    
    print("shape of X_train :",X_train.shape)
    print("shape of X_test :",X_test.shape)
    
    print("shape of Y_train :",Y_train.shape)
    print("shape of Y_test :",Y_test.shape)
    
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    
    model = KNeighborsClassifier()
    
    model = model.fit(X_train_scaled,Y_train)
    
    print("Model training is completed")
    print(Border)
    
    # Step 4 : Test Data
             
    print(Border)
    print("Step 4 : Test data")
    print(Border)
        
    Y_pred = model.predict(X_test_scaled)
    
    print("Model testing is succsefully done")
    
    print(Border)
    
    # Step 5 : Accuracy check
    
    print(Border)
    print("Step 5 : Accuracy check")
    print(Border)
    
    accuracy = accuracy_score(Y_test,Y_pred)
            
    print("Accuracy is :", accuracy* 100 ,"%")
    
def main():
    
    MarvellousClassifier('Winepredictor.csv')
   
if __name__  =="__main__":
    main()