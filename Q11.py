def cube(num):
    num = num * num * num
    print("cube of number is :", num)
    
def main():
    value = int(input("Enter Number:"))
    cube(value)

if __name__ =="__main__":
    main()