import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score
import math

def AccuracyCheck(X,Y,K):
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5, random_state=42)
    
    model = KNeighborsClassifier(n_neighbors=K)
    
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)
    
    Accuracy = accuracy_score(Y_test,Y_pred)
    
    return Accuracy

def MarvellousEucDistance(P1 , P2):
    
    Ans =math.sqrt((P1['X']- P2['X']) **2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousClassifier(Datapath):
    
    Border = ("-"*40)
    
    ######################################################
    # step 1 : Load the dataset
    ######################################################
     
    print(Border)
    print("# step 1 : Load the dataset")
    print(Border)
    
    df = pd.read_csv(Datapath)
    
    print(Border)
    print("Some Entries from the dataset :")
    print(Border)
    print(df.head())
    print(Border)
    

    # ##################################################
    # Step 2 : Clean, Prepare and Manipulate Data
    # ##################################################

    print(Border)
    print("# Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of dataset :", df.shape)
    print("Total records   :", df.shape[0])
    print("Total columns   :", df.shape[1])

    print(Border)
    WetherEncoder = LabelEncoder()
    TemperatureEncoder = LabelEncoder()
    PlayEncoder = LabelEncoder()

    df["Wether"] = WetherEncoder.fit_transform(df["Wether"])

    df["Temperature"] = TemperatureEncoder.fit_transform(df["Temperature"])

    df["Play"] = PlayEncoder.fit_transform(df["Play"])
    
    print(Border)
    print("Data after encoding")
    print(Border)
    print(df.head())
    
    ###################################################
    # Step 3 :  Train Model
    ###################################################
    
    print(Border)
    print("# Step 3 : Train Model ")
    print(Border)
    
    X = df[['Wether', 'Temperature']]
    Y = df['Play']
    
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    
    model = KNeighborsClassifier(n_neighbors=3)
    
    model = model.fit(X_scaled,Y)
    
    print("Model Train successfully")
    
    ###################################################
    # Step 4 :  Test Model
    ###################################################
        
    print(Border)
    print("# Step 4 : Test Model ")
    print(Border)
    
    Wether = input("Enter Wether : ")
    Temperature = input("Enter Temperature : ")
    
    Wether = WetherEncoder.transform([Wether])[0]
    
    Temperature = TemperatureEncoder.transform([Temperature])[0]
    
    TestData = [[Wether, Temperature]]

    Result = model.predict(TestData)

    Result = PlayEncoder.inverse_transform(Result)
    
    print(Border)
    print("Prediction is :" , Result[0])
    print(Border)
    
    print(Border)
    print("Accuracy of KNN")
    print(Border)

    Accuracy = AccuracyCheck(X, Y, 1)
    print("Accuracy for K = 1 :", Accuracy * 100, "%")
    
    Accuracy = AccuracyCheck(X, Y, 3)
    print("Accuracy for K = 3 :", Accuracy * 100, "%")
    
    Accuracy = AccuracyCheck(X, Y, 5)
    print("Accuracy for K = 5 :", Accuracy * 100, "%")
        
    Accuracy = AccuracyCheck(X, Y, 7)
    print("Accuracy for K = 7 :", Accuracy * 100, "%")
            
def main():
    
    MarvellousClassifier('MarvellousInfosystems_PlayPredictor.csv')
    
if __name__ == "__main__":
    main()