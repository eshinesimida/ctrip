# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 16:05:41 2020

@author: a4546
"""

class Solution(object):
    def numOffices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # your code here
        result = 0

        def mark_island(grid, x, y, visited):
            
            if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[x]) - 1:
                return ''

            
            if visited[x][y] == True:
                return ''
            visited[x][y] = True
            
            
            if grid[x][y] == '0':
                return ''

            
            mark_island(grid, x - 1, y, visited)
            mark_island(grid, x + 1, y, visited)
            mark_island(grid, x, y - 1, visited)
            mark_island(grid, x, y + 1, visited)
        
       
        visited = []
        for i in range(len(grid)):
            visited.append(['' for item in grid[0]])

      
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if not visited[x][y] and grid[x][y] == '1':
                    result += 1
                    mark_island(grid, x, y, visited)
                visited[x][y] = True
        return result

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
    matrix = get_matrix()
    offices = sol.numOffices(matrix)
    print(offices)

