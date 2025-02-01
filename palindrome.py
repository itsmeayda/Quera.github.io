def palindrome(n):
    if n[::-1] == n[::] :
        print("YES")
    else :
        print("NO")



n = input()
palindrome(n)