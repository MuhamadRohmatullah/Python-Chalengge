def isPalindrome(s):
    return s == s[::-1]

word  = input("Masukan kata")
word = isPalindrome(word)

if word :
    print("Yes")
else :
    print("No")
