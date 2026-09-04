
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

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
    
    print(average_marks)
    
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
    
if __name__ == "__main__":
    main()