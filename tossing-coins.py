
import random
import numpy as np
import matplotlib.pyplot as plt

#In this little program, it is try to simulate a tossing coins experiment
#Here we have "n" experiments by "m" tossing coin trys
#It is possible to change m and n by any positive integer number
#When the value of VA is 1, it is added 1 to the variable p
#When the value of VA is 0, it is substracted 1 to the variable p

X = np.array([]) # creating a empty array
p = 0            # setting varible p to 0

#starting the 2 "for loops"
for experiment in range (100000):
   for tossing_coin in range(100):
       VA = random.randint(0,1)

       if VA == 1:
           p = p + 1
           
       if VA == 0:
           p = p - 1
            
   print p
   X = np.hstack((X,p))
   p = 0

print X #X variable contains all the results from the n experiments

fig, HistogramaX =  plt.subplots()
HistogramaX.hist(X, 100)
plt.show()

fig, lineaX = plt.subplots()
lineaX.plot(X)
plt.show()




