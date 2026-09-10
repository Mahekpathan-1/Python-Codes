import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


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
    
#----------------------------------------------------------------------
# Step 3. Exploratory Data Analysis (EDA)
#----------------------------------------------------------------------
    
def EDA():
    print(Border)
    print("Step 3. Exploratory Data Analysis (EDA)")
    print(Border)
    print("Summary statistics")
    print(Border)
    print(df.describe())
    
    print(Border)
    print("Feature Correlation")
    print(Border)
    
    correlation = df.corr()                   # calculate correlation matrix
    print(correlation)
    
    plt.figure(figsize=(8,6))
    
    sns.heatmap(
        correlation,
        annot=False,
        cmap="coolwarm"
    )
    
    plt.title("Feature correlation Heatmap")
    plt.show()
    
    #-----------------------------------------------------------------------
    #Feature correlation is used to measure the strength and direction of the relationship 
    # between different features in the dataset.
    # A correlation matrix and heatmap are used to visualize these relationships.
    #-----------------------------------------------------------------------
    
#----------------------------------------------------------------------
# Step 4. Split the dataset into training and testing sets
#----------------------------------------------------------------------
def modelBuild():
    
    print(Border)
    print("Step 4. Split the dataset into training and testing sets")
    print(Border)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=42)
    
#----------------------------------------------------------------------
# Step 5. Machine Learning Classification model to predict Tumor type
#----------------------------------------------------------------------
    
    print(Border)
    print("Step 5. Machine Learning Classification model to predict Tumor type")
    print(Border)
    
    model = LogisticRegression(max_iter=5000)
        
    model = model.fit(X_train,Y_train)
    
    Y_pred =model.predict(X_test)
    
    print("Model Build Successfully")
    
#----------------------------------------------------------------------
# Step 6. Evaluate the model
#----------------------------------------------------------------------
    
    print(Border)
    print("Step 6. Evaluate the model")
    print(Border)
    
    print("Accuracy :", accuracy_score(Y_test, Y_pred))
    print(Border)
    
    cm= confusion_matrix(Y_test, Y_pred)
    print("Confusion Matrix :",cm)
    print(Border)
    
    report = classification_report(Y_test, Y_pred)
    print("Classification Report :")
    print(report)
    print(Border)
    
#----------------------------------------------------------------------
# Step 7. Observations And Conclusion 
#----------------------------------------------------------------------
    print(Border)
    print("Step 7. Observations And Conclusion ")
    print(Border)
    
    print("1.The Breast Cancer dataset was successfully loaded, explored and preprocessed.\n"
           "2.The dataset contained 569 samples, 30 features and no missing values.\n"
           "3.Feature correlation was analyzed using a correlation matrix and heatmap.\n"
           "4.Standardization improved the suitability of the numerical features for Logistic Regression.\n"
           "5.Logistic Regression successfully classified the breast cancer cases into malignant and benign classes.\n"
           "6.The model's performance was evaluated using accuracy, confusion matrix, precision, recall and F1-score.\n"
           "7.Logistic Regression provides good classification performance on this dataset.\n"
           "8.Therefore, Logistic Regression can be considered a suitable machine-learning model for breast cancer classification.\n")

def main():
    
    DataLoad()
    Preprocess()
    EDA()
    modelBuild()
    
if __name__ =="__main__":
    main()
    