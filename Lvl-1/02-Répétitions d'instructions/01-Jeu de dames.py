#for loop in range(20) :
#   for loop in range(20) :
#      print("O",end="")
#      print("X",end="")
#   print()
#   for loop in range(20) :
#      print("X",end="")
#      print("O",end="")
#   print()


# Nous pouvons supprimer deux lignes inutiles en faisant ceci :
# We could delete useless lines like this :

for loop in range(20):
   for loop in range(20):
      print("OX", end = "")
   print()
   for loop in range(20):
      print("XO", end = "")
   print()

   
