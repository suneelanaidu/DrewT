{% include navigation.html %}

# Python Project

<iframe frameborder="0" width="100%" height="800px" src="https://replit.com/@SonakshiBhalla/Sonakshi?lite=true#main.py">

## Replit Artifacts
### Week 0
### Week 1
### Week 2
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
