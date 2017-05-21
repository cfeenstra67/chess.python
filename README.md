# chess.python
My solution to the classic programming problem--finding how to place n queens on an n x n chess board.

Note that this is very much a "brute force" solution to the problem.  I wrote this after seeing it presented in a python book, so speed was not my primarily concern so much as finding a solution that would always work.

To test, run these commands in terminal (to run on Windows, adjust syntax accordingly):
1. cd <chess.py path>
2. python3
3. from chess import queen_locations

queen_locations takes two arguments: num_queens and s_length
  num_queens: number of queens you would like placed on the board
  s_length: side length, the size of the chess board
