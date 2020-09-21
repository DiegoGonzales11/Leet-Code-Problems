def isPalindrome(x):
    if x < 0:
        return False
    elif x>=0 and x<=9:
        return True
    else:
        reverse = 0
        num = x
        while num != 0:
            reverse = reverse *  10 + num % 10
            num = int(num / 10)
            
        if reverse == x:
            return True
        else:
            return False