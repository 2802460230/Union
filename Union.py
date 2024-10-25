def union():

  a = input("Input List 1")
  b = input("Input List 2")

  A = []
  B = []
  y = ""

  for x in a:
    if x != "[" and x != "," and x != "]":
      y = y + x
    else:
      if y != "":
        A.append(int(y))
        y = ""

  for x in b:
    if x != "[" and x != "," and x != "]":
      y = y + x
    else:
      if y != "":
        B.append(int(y))
        y = ""

  for x in range(len(B)):
    flag = False
    for y in range(len(A)):
      if B[x] == A[y]:
        flag = True
    if flag == False:
      A.append(B[x])

  for x in range(len(A) - 1):
    while x > 0:
      if A[x + 1] < A[x]:
        y = A[x]
        A[x] = A[x + 1]
        A[x + 1] = y
      x = x - 1

  print(A)

union()

def weaow():
  string = input("string?")
  tuple = input("tuple?")

  A = ()
  B = ""
  
  for x in tuple:
    if x != "(" and x != "," and x != ")":
      y = y + x
    else:
      if y != "":
        A.append(int(y))
        y = ""

  for x in range(len(string)):
    for y in range(A[x]):
      B = B + string[x]

  print(B)

weaow()
      

  