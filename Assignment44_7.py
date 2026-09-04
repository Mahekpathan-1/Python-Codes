# Create a bar chart showing student names and their total marks.

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
    
if __name__ == "__main__":
    main()