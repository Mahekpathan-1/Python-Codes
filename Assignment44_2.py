# Print descriptive statistics using describe()

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
    
    print("Discriptive statistics")
    print(df.describe())
    
if __name__ == "__main__":
    main()