#TC: O(n)
#SC: O(1)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #iterating the matrix using loop and considering the the iteration from second row
        
        n=len(matrix)
        for i in range (1,n):
            for j in range(n):
                #two checks in place
                if j==0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                #again two check if it is the last column 
                elif  j==n-1:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1])
                    #three checks for the middle element
                else:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])
             #returning the minimum element of last row
            
        return min(matrix[-1])
                    
                    
