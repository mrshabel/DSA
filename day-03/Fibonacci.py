class Fibonacci:
    def fib(self, n):
        numbers = [0,1]
        for i in range(2, n + 1):
            numbers.append(numbers[i - 1] + numbers[i - 2])
        return numbers[n]
    
#create instance of class
number = Fibonacci()

#output results
print(number.fib(0))


