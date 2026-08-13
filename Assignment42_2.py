import math

def MarvellousEucDistance(P1 , P2):
    
    Ans =math.sqrt((P1['X']- P2['X']) **2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def MarvellousKNNclassifier(X,Y,K):
    
    Border = ("-"* 40)
    
    Data = [
        {'point' : 'A', 'X' : 1 , 'Y' : 2, 'label' : 'Red'}, 
        {'point' : 'B', 'X' : 2 , 'Y' : 3, 'label' : 'Red'},
        {'point' : 'C', 'X' : 3 , 'Y' : 1, 'label' : 'Blue'},
        {'point' : 'D', 'X' : 6 , 'Y' : 5, 'label' : 'Blue'},
        {'point' : 'E', 'X' : 5 , 'Y' : 4, 'label' : 'Blue'} 
    ]
    Testpoint = {
        'X': X,
        'Y': Y
    }

    for d in Data :
        d['distance']= MarvellousEucDistance(d,Testpoint)

    sorted_Data = sorted(Data, key=lambda item: item['distance'] )

    nearest = sorted_Data[:K]
    
    print(Border)
    print("K =", K)
    print(Border)
    print("Nearest Neighbours")
    print(Border)
    
    for d in nearest:
        print(d)
    
    votes = {}
    
    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label,0) + 1
        
    print(Border)
        
    for d in votes:
        print("Name :", d , "Number of votes :", votes[d])
        
    print(Border)
        
    iMax= 0
    Name = ""
    
    for d in votes:
        if(votes[d]> iMax):
            iMax = votes[d]
            Name = d
    
    print("Final Prediction is :", Name)
        
def main():
    
    X = float(input("Enter X Coordinator :"))
    Y = float(input("Enter Y Coordinator :"))
    
    Kvalues = [1,3,5]
    
    for K in Kvalues:
        MarvellousKNNclassifier(X,Y,K)
    
if __name__ == "__main__":
    main()