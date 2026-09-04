# Rename 'Math' column to 'Mathematics'

import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

def main():
    Border = '-'* 40
    
    Data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92, 88,80],
        'English' : [75,85,82]
    }
    
    df = pd.DataFrame(Data)
    
    print(df)
    print(Border)
    
    scalar = MinMaxScaler()
    
    print("Using MinMAxscaler :")
    
    df['Math'] = scalar.fit_transform(df[['Math']])     # normalize numerical value between 0 and 1
    
    print(df)
    
    print(Border)
    
    df['Gender']= ["Male", "Male","Female"]
    
    average_marks = df.groupby('Gender')[
        ['Math','English','Science']
    ].mean()
    
    print("Average Marks")
    print(average_marks)
    print(Border)
    
    sagar = df[df["Name"] == "Sagar"]
    subjects = ["Math", "Science", "English"]
    marks = sagar[subjects].values[0]
    
    plt.pie(
        marks,
        labels = subjects,
        autopct="%1.1f%%"
    )
    
    plt.title("Subject marks of sagar")
    
    plt.show()
    
    df['Total'] = df[subjects].sum(axis=1)
    
    df["Status"] = np.where(
    df["Total"] >= 250,
    "Pass",
    "Fail"
)
    print(df)
    
    print("Total Passed :" , df[df['Status'] == 'Pass'].shape[0])
    
    df.to_csv("students_result.csv", index= False)
    
    plt.hist(df['Math'], bins=5, edgecolor='black')
    plt.title("Distribution of math marks")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()
    
    df.rename(columns={'Math' : 'Mathematics'}, inplace=True)
    
    print(df)
    
if __name__ == "__main__":
    main()