class BankAccount:
     ROI = 10.5        # Rate OF Interest
     
     def __init__(self , Name , Amount):
          self.Name = Name
          self.Amount = Amount
          
     def Display(self):
          print("\n------------------Account Details---------------")
          print("Account holder name :", self.Name)
          print("Account Balance :", self.Amount)
          
     def Deposite(self):
          DepositeAmount = float(input("Enter Deposite Amount :"))
          
          if DepositeAmount > 0 :
               self.Amount += DepositeAmount
               print("Amount Deposited Successfully")
          else:
               print("Invalid Deposite amount")
               
     def Withdraw(self):
          withdrawAmount = float(input("Enter withdraw amount :"))
          
          if withdrawAmount <= 0 :
               print("Insufficient withdraw amount")
               
          elif withdrawAmount <= self.Amount:
               self.Amount -= withdrawAmount
               print("withdraw successfully")
               
          else:
               print("insufficient balance")
               
     def CalculateInterest(self):
          Interest = (self.Amount * BankAccount.ROI) / 100
          return Interest
     
def main():
     Name = input("Enter Amount holder name :")
     Amount = float(input("Enter Initial Amount :"))
     
     obj1 = BankAccount(Name,Amount)
       
     obj1.Deposite()
     obj1.Display()  
     
     obj1.Withdraw()
     obj1.Display()  
     
     Interest = obj1.CalculateInterest()
     
     print("Rate of Interest :", BankAccount.ROI, "%")
     print("Interest Amount :", Interest)

if __name__ == "__main__":
     main()           
               