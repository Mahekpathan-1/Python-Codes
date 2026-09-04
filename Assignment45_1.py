# Normalize the Math scores using Min-Max Scaling

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
    
    
if __name__ == "__main__":
    main()