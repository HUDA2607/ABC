<<<<<<< HEAD
def fib_series(nterms):
  # first two terms
  n1, n2 = 0, 1
  count = 0
  while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

nterms = int(input("How many terms? "))
       
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   fib_series(nterms)
else:
   print("Fibonacci sequence:")
=======
def fib_series(nterms):
  # first two terms
  n1, n2 = 0, 1
  count = 0
  while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

nterms = int(input("How many terms? "))
       
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   fib_series(nterms)
else:
   print("Fibonacci sequence:")
>>>>>>> 3920a7233fe64405a628e1fc7cc9ed6f85077a04
   fib_series(nterms)