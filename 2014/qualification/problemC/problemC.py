from sys import stdin

test_cases = int(stdin.readline())

for i in range(test_cases):
   print("Case #" + str(i+1) + ":") 
   oneC = False
   oneR = False
   impossible = False 
   values = stdin.readline().split()
   R = int(values[0])
   C = int(values[1])
   M = int(values[2])
   N = R*C-M
   if (N%2 == 0):
       even = True
   else:
       even = False
   board = []
   # Let's get the trivial ones out of the way
   if (R == 1):
       if (not (C > M)):
           impossible = True
       oneR = True
   elif(C == 1):
       if (not (R > M)):
           impossible = True
       oneC = True
   elif ((R > 1) and (C > 1)):
       #if number of empty spaces is even we need at least 4 
       if(((R*C-M)<4) and (N%2 == 0)):
           impossible = True
       #if number of empty spaces is odd we need at least 9 and R and C must be at least 3
       elif ((N%2 > 0) and ( N < 9 or R < 3 or C < 3) and N > 1):
           impossible = True
   if (not impossible):
       #fill board with mines
       for j in range(R):
           board.append([])
           for k in range(C):
               board[j].append("*")
       if (oneR):
            for k in range(N):
                board[0][k] = "."
            board[0][0] = "c"
       elif (oneC):
            for j in range(N):
                board[j][0] = "."
            board[0][0] = "c"
       # single mine
       elif (N == 1):
           board[0][0] = "."
       # can't fill at least two rows, then fill first two rows with N/2
       elif (even and N-2*C < 0):
           a = int(N/2)
           for j in range(a):
               board[0][j] = "."
               board[1][j] = "."
       # if N is odd and can't fill at least two rows and a third row with 3 non-mines        
       # fill the first two rows with (N-3)/2 and the third with 3 non-mines
       elif ((not even) and N-2*C-3 < 0):
           a = int((N-3)/2)
           for j in range(a):
               board[0][j] = "."
               board[1][j] = "."
           board[2][0] = "."
           board[2][1] = "."
           board[2][2] = "."
       else:
           #fill board
           a = N
           j = 0
           k = 0
           while (a > 0):
               board[j][k] = "."
               a -= 1
               k += 1
               if (k >= C):
                   k = 0
                   j += 1
                   # if last mine and at beginning of row, move one empty space to this row from last row
               if(a == 0 and k == 1):
                   board[j-1][C-1] = "*"
                   board[j][1] = "."
       #print board
       board[0][0] = "c"
       for j in range(R):
           for k in range(C):
               print(board[j][k],end="")
           print() 
   else:
       print("Impossible")
