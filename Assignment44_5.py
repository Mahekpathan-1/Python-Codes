# Replace the student name Pooja with Puja.

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
    
    df['Total'] = df[subject_cols].sum(axis=1)
    
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


if __name__ == "__main__":
    main()