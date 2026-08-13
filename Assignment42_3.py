import math

def MarvellousEcudistance(P1,P2):
    
    Ans =math.sqrt((P1['study Hours']  - P2['study Hours']) ** 2 + (P1['Attendance'] - P2['Attendance']) **2)
    return Ans

def MarvellousKNNclassifier(X,Y,K=3):
    Border = "-"*40
    
    Data = [
        {'study Hours' : 2, 'Attendance' : 60 , 'Result' : 'Fail'},
        {'study Hours' : 5, 'Attendance' : 80 , 'Result' : 'pass'},
        {'study Hours' : 6, 'Attendance' : 85 , 'Result' : 'pass'},
        {'study Hours' : 1, 'Attendance' : 50 , 'Result' : 'Fail'}
    ]
    
    TestPoint = {
        'study Hours' : X,
        'Attendance' : Y
    }
    
    for d in Data:
        d['distance'] = MarvellousEcudistance(d,TestPoint)
        
    sorted_Data = sorted(Data, key=lambda item: item['distance'] )
    
    nearest = sorted_Data[:K]
    
    votes = {}
    
    for neighbours in nearest:
        Result = neighbours['Result']
        votes[Result] = votes.get(Result,0) + 1
    
    iMax = 0
    Name = ""
    
    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d
            
    print(Border)
    print("prediction result is :", Name )
    
def main():
    
    X = float(input("Enter Study Hours :"))
    Y = float(input("Enter Attendance percentage  :"))
    
    MarvellousKNNclassifier(X,Y)
    
if __name__ == "__main__":
    main()