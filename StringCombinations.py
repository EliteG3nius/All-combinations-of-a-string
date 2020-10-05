#This program finds all possible string cominations of the user input
from itertools import combinations
print ("Enter your word:")
UserInput = str(input())
combo = [UserInput[i:j] for i, j in combinations(range(len(UserInput) + 1), r = 2)]
print (combo)
