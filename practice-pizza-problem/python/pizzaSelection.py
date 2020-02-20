from itertools import combinations_with_replacement

infile = open("e_also_big.in", "r")
firstLine = infile.readline().split()
maxNumOfPizzas = int(firstLine[0])
numOfDiffPizzaTypes = int(firstLine[1])
secondLine = infile.readline()
infile.close()
slicesByPizzaType = secondLine.split()
slicesByPizzaType = [ int(x) for x in slicesByPizzaType ]
maxComb = []
maxSum = 0
maxNumComb = 0
print(numOfDiffPizzaTypes)
for i in range(0,len(slicesByPizzaType)):
    possibleCombinations = list(combinations_with_replacement(slicesByPizzaType, i))
    for comb in possibleCombinations:
        combSum = sum(comb)
        numComb = len(comb)
        if maxSum <= combSum < maxNumOfPizzas:
            maxSum = combSum
            maxComb = comb
            maxNumComb = numComb
        elif combSum == maxSum and numComb < numOfDiffPizzaTypes:
            maxSum = combSum
            maxComb = comb
            maxNumComb = numComb

outfile = open("e_also_big.out", "w")
outfile.write(str(len(maxComb)) + "\n")
for slices in maxComb:
    pizzatype = slicesByPizzaType.index(slices)
    outfile.write(str(pizzatype) + " ")
print(maxSum)

