# Program Tic-Tac-Toe

import random

board = []
for i in range(3):
    board.append([" "," "," "])

optAvailable = []
for i in range(3):
    for j in range(3):
        optAvailable.append([i+1,j+1])
print(optAvailable)

while True:
    print("--Tic-Tac-Toe by Restu--")
    rowCounting = 0
    for row in board:
        print(f"{row[0]}|{row[1]}|{row[2]}")
        if rowCounting != 2:
            print("-----")
        rowCounting += 1
    print()
    
    userRow = int(input("Masukkan baris: "))
    userCol = int(input("Masukkan kolom: "))
    print()

    if board[userRow-1][userCol-1] == " ":
        optAvailable.remove([userRow,userCol])
        board[userRow-1][userCol-1] = 1

        if (board[0][0]==1 and board[0][1]==1 and board[0][2]==1) or (board[1][0]==1 and board[1][1]==1 and board[1][2]==1) or (board[1][0]==1 and board[1][1]==1 and board[1][2]==1) or (board[0][0]==1 and board[1][0]==1 and board[2][0]==1) or (board[0][1]==1 and board[1][1]==1 and board[2][1]==1) or (board[0][2]==1 and board[1][2]==1 and board[2][2]==1):
            print("Player Wins!")
            break

        if len(optAvailable) != 0:
            comp = optAvailable[random.randint(0,len(optAvailable)-1)]
            compRow = comp[0]
            compCol = comp[1]
            optAvailable.remove([compRow,compCol])
            board[compRow-1][compCol-1] = 0
            if (board[0][0]==0 and board[0][1]==0 and board[0][2]==0) or (board[1][0]==0 and board[1][1]==0 and board[1][2]==0) or (board[1][0]==0 and board[1][1]==0 and board[1][2]==0) or (board[0][0]==0 and board[1][0]==0 and board[2][0]==0) or (board[0][1]==0 and board[1][1]==0 and board[2][1]==0) or (board[0][2]==0 and board[1][2]==0 and board[2][2]==0):
                print("Computer Wins!")
                break
        else:
            rowCounting = 0
            for row in board:
                print(f"{row[0]}|{row[1]}|{row[2]}")
                if rowCounting != 2:
                    print("-----")
                rowCounting += 1
            break