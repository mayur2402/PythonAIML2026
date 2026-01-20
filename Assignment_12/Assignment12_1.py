#Write a program which accepts one character and checks whether it is vowel or consonant.
#Input: a
#Output: Vowel

def IsVowel(ch):
    
    if(ch.lower() == 'a' or ch.lower() == 'e' or ch.lower() == 'i' or ch.lower() == 'o' or ch.lower() == 'u'):
        return True
    else:
        return False

def main():
    print("Enter one character to checks whether it is vowel or consonant")
    ch = input()
    if(len(ch) > 1):
        print("Enter one character")
        return
    isvowel = IsVowel(ch)
    if(isvowel):
        print("vowel")
    else:
        print("consonant")

if __name__ == "__main__":
    main()