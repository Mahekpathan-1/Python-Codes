def CheckVowel(ch):
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("vowel")
    else:
        print("consonant")
        
def main():
    char = input("Enter a Character : ")
    CheckVowel(char)
    
if __name__ == "__main__":
    main()