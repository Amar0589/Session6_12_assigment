def ispalindrome(ip):
    s=str(ip)
    print("Input string is:",s)
    rev=s[::-1]
    if s == rev:
        print("string is palindrome")