import matplotlib.pyplot as plt
import math
from decimal import *
f = math.factorial
prob_list = []
getcontext().prec = 3

n = [i for i in range(0,366)]
for i in n:
	prob = Decimal(f(365)/f(365-i))
	prob = prob/Decimal(365**i)
	prob = 1 - prob
	prob_list.append(prob)


plt.plot(prob_list)
plt.xlabel('Number of people (n)')
plt.ylabel('Probability of n people having different birthdays ')
plt.title('Birthday Paradox',fontweight = 'bold')
plt.plot(23,prob_list[23],'ro'),plt.text(23,prob_list[23],'({},{})'.format(23,prob_list[23]))
plt.plot(70,prob_list[70],'ro'),plt.text(70,prob_list[70],'({},{})'.format(70,prob_list[70]))
plt.xlim([1,365]),plt.ylim([0,1.1]),plt.grid(True)
plt.show()


'''
Part 2 : the inverse problem
Given a probability of same birthday find the number of people
'''
import numpy as np
p_same = np.linspace(0 , 1.0,1000)
n_people = [math.sqrt(2 * 365 * math.log(1/(1-i))) for i in p_same]
plt.plot(p_same,n_people)
plt.ylabel('Number of people (n)')
plt.xlabel('Probability of n people having different birthdays ')
plt.title('Birthday Paradox Inverse Problem',fontweight = 'bold')
plt.ylim([1,100]),plt.xlim([0,1.01]),plt.grid(True)
plt.show()
