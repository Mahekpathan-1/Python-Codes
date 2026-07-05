from functools import reduce

Product = lambda No1 , No2 : No1 * No2

def main():
    
    Numbers = [ 2, 4, 6, 3]
    
    RNumbers = reduce(Product, Numbers)
    
    print("Input Numbers is :", Numbers)
    
    print("Product of all numbers is :", RNumbers)
    
if __name__ == "__main__":
    main()