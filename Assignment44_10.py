# drop english column from original dataframe

import pandas as pd
import matplotlib.pyplot as plt

def main():
    Border = '-'* 40
    
    Data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85,90,78],
        'Science' : [92, 88,80],
        'English' : [75,85,82]
    }
    
    df = pd.DataFrame(Data)
    
    print("Dataframe")
    print(df)

    print(Border)
    print("Shape is :")
    print(df.shape)
    print(Border)
    
    print("Columns is :")
    print(df.columns)
    print(Border)
    
    print("datatype is :")
    print(df.dtypes)   
    
    subject_cols = ['Math', 'Science', 'English'] 
    
    df['TotalMarks'] = df[subject_cols].sum(axis=1)
    
    print(Border)
    print("Full dataframe with total marks :")
    print(df)
    print(Border)
    
    science_top = df[df['Science'] > 85 ]
    
    print("Students with science marks > 85 :\n", science_top)
    
    df['Name'] = df['Name'].replace('Pooja', 'Puja')
    
    print(Border)
    print("Replace Pooja with puja")
    print(df)
    
    sorted_df = df.sort_values(by = 'TotalMarks', ascending= False)
    
    print(Border)
    print("Total Marks in descending order :")
    print(sorted_df)

    plt.bar(
        df['Name'],
        sorted_df['TotalMarks'],
        width = 0.6,                     # width of bars 
        edgecolor = "black",              # border color of bars
        linewidth = 1,                    # width of bar border
        alpha = 0.8,                      # transperance 0.0 to 1.0
        label = "TotalMarks"                # legend texx   
        )
    
    plt.title("Student Bar plot")
    plt.xlabel("Students Name")
    plt.ylabel("TotalMarks")
    
    plt.legend()
    plt.show()
    
    amit = df[df['Name'] == 'Amit'].iloc[0]

    subjects = ['Math', 'Science', 'English']

    marks = [
        amit['Math'],
        amit['Science'],
        amit['English']
    ]
    
    plt.plot(subjects, marks, marker='o')

    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title("Amit's Marks Across Subjects")

    plt.show()
    
    Data2 ={
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [None, 76,88],
        'Science' : [91,None,85]
    }
    
    df2 = pd.DataFrame(Data2)
    
    print(Border)
    print("DataFrame with None value")
    print(df2)
    
    df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
    df2['Science'] = df2['Science'].fillna(df2['Science'].mean())
    
    print(Border)
    print("Fill none value with column mean ")
    print(df2)
    
    df = df.drop(columns=['English'])
    print(Border)
    print("English column drop")
    print(df)
    
if __name__ == "__main__":
    main()