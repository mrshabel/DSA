import timeit
class Palindrome:
    def isPalindrome1(self, x):
        num = list(str(x))
        reverse = []
        for i in range(1, len(num) + 1):
            reverse.append(num[-i])
        
        return num == reverse
    
    def isPalindrome2(self, x):
        return list(str(x)) == list(str(x))[::-1]
    
    def isPalindrome3(self, x):
        num = str(x)
        return num == num[::-1]

#create instance of class
number = Palindrome()

#show solution here
print(number.isPalindrome1(121))
print(number.isPalindrome2(121))
print(number.isPalindrome3(221))