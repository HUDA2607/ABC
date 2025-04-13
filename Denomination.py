<<<<<<< HEAD
def no_notes(a):
  Q = [2000, 500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(7):
    q = Q[i]
    x = a//q
    print("Notes of {} = {}".format(q, x))
    a = a%q

amount = int(input("Enter Total Amount"))
=======
def no_notes(a):
  Q = [2000, 500, 200, 100, 50, 20, 10]
  x = 0
  for i in range(7):
    q = Q[i]
    x = a//q
    print("Notes of {} = {}".format(q, x))
    a = a%q

amount = int(input("Enter Total Amount"))
>>>>>>> 3920a7233fe64405a628e1fc7cc9ed6f85077a04
no_notes(amount) 