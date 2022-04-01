{% include navigation.html %}

# Python Project

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@SonakshiBhalla/Sonakshi?lite=true#main.py">

## Replit Artifacts
### Week 0
### Week 1
Factorial:
```
  def factorial():   
    def fac(n):
      if n == 1 or n == 0:
          return 1
      else:
          return n * fac(n-1)
    num = int(input("Enter a number for factorial: "))
    if num < 0:
        print("factorial does not exist for negative numbers")
    else:
        print(fac(num))

if __name__ == "__main__":
    factorial()
```
### Week 2
Factors Imperative:
```
  def factorsimp():
  def factorial(n):
      for i in range(1, n+1):
          if n % i == 0:
              print(i)
      print()

  print("Enter a Number: ", end="")
  try:
      number= int(input())
      print(end="")
      factorial(number)
  except ValueError:
      print("Invalid Input!")

if __name__ == "__main__":
    factorsimp()
```
Palindrome:
```
  def palindrome():
  class Palindrome(object): 
      def function(self, a_string): 
          self.a_string = a_string 
          len_a = len(self.a_string) 
          x = int(len_a / 2) 
 
          if self.a_string[0:x] == self.a_string[-1:-x - 1:-1]: 
              print("This is a Palindrome String") 
          else: 
              print("This is not a Palindrome String") 
 
 
  x = input("Enter the String: ")  
  Object = Palindrome() 
  
  Object.function(x)

if __name__ == "__main__":
    palindrome()

```
Partner code:
```
  class newFibonacci(): # ethan commit, fibonacci with OOP
  def __init__(self):
    print("1", end=" ") # 0 will always start the sequence
  def __call__(self, n):
    x = 0
    y = 1
    z = 0
    fs = []
    for i in range(n-1):
        z = x + y
        x = y
        y = z
        i += 1
        fs.append(z)
        print(z, end = " ")
    print()
      
def testerf(): # tester for OOP fibonacci
  try:
    y = int(input("Enter to what term you want the fibonacci sequence to go to: "))
    f = newFibonacci()
    f(y)
  except:
    print("Something went wrong")

```
### Week 3
