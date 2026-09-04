# DataFrame of student marks and display its basic information 
# shape
# columns
# datatype

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

if __name__ == "__main__":
    main()