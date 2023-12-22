#cellGrid creation
cellGrid = []
for i in range (0, 9):
    row = []
    for j in range (0,9):
        row.append(0)
    cellGrid.append(row)

#initializing board
for row in range (3, 6):
    for col in range(3, 6):
        cellGrid[row][col] = 1

#print statement format
print("Initial State")
for row in cellGrid:
    for col in row:
        print(col, end=" ") 
    print()

#next generation of cell grid
nextGen = []
for i in range (0, 9):
    row = []
    for j in range (0,9):
        row.append(0)
    nextGen.append(row)

#game algorithm
simulate = 1

while(simulate == 1):
    for row in range(1, 8):
        for col in range(1, 8):
            numNeighbors = 0
            if (cellGrid[row-1][col-1] == 1):
                numNeighbors = numNeighbors + 1
            if (cellGrid[row][col-1] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row+1][col-1] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row-1][col+1] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row][col+1] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row+1][col+1] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row-1][col] == 1):
                numNeighbors = numNeighbors + 1 
            if (cellGrid[row+1][col] == 1):
                numNeighbors = numNeighbors + 1 
            if ((numNeighbors == 2 or numNeighbors == 3) and cellGrid[row][col] == 1):
                nextGen[row][col] = 1
            elif(cellGrid[row][col] == 0 and numNeighbors == 3):
                nextGen[row][col] = 1
            else:
                nextGen[row][col] = 0

    print()
    generationNumber = "Generation Number: {0}"
    print(generationNumber.format(simulate))
    for row in nextGen:
        for col in row:
            print(col, end=" ") 
        print()

    #make cellGrid equal to previous generation
    for i in range (0, 9):
        for j in range (0,9):
            cellGrid[i][j] = nextGen[i][j]
        
    print()
    simulate = input("Enter 1 to continue or anything else to stop: ")
    simulate = int(simulate)

print("while loop over")