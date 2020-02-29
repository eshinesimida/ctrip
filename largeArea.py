# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:35:48 2020

@author: a4546
"""

class Solution:
    
    def biggestTable(self, grid):
        # your code here
        matrix = grid
        
        m, n = len(matrix), len(matrix[0])
        h, lo, hi = [0]*n, [0]*n, [n]*n
        ans = 0
        for i in range(m):
            left, right = 0, n
            for j in range(n):
                if matrix[i][j] == "1": #forward
                    h[j] += 1
                    lo[j] = max(lo[j], left)
                else: 
                    h[j] = lo[j] = 0
                    left = j+1
                    
                if matrix[i][~j] == "1": #backward
                    hi[~j] = min(hi[~j], right)
                else: 
                    hi[~j] = n
                    right = n-j-1
            ans = max(ans, max((x-y)*z for x, y, z in zip(hi, lo, h)))
            
        return ans 

    
def get_matrix():
    row = int(input())
    col = int(input())
    grid = [["0"]*col]*row

    for i in range(row):
        line = input()
        grid[i] = list(line)[0:col]
    return grid

        
if __name__ == "__main__":
    sol = Solution()
    grid = get_matrix()
    bigTable = sol.biggestTable(grid)
    print(bigTable)

