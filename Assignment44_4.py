# Display students who scored more than 85 in Science

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


if __name__ == "__main__":
    main()