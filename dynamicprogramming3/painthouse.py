
#TC: O(n)
#SC: O(1)
class Solution(object):
    def minCost(self,costs):
    #iterate through reverser and store value at each step ,from len -2 because we are starting it from before row
        for i in range (len(costs)-2,-1,-1):
            
        #adding the minimum of last row and add it to before row first element and checking the first and second index for zeroth index 
            costs[i][0] +=min(costs[i+1][1],costs[i+1][2])
        #in case of first index check the zeroth and seconf index
            costs[i][1]+= min(costs[i+1][0],costs[i+1][2])
        #incase of second index then check the first and zeroth
            costs[i][2]+= min(costs[i+1][0],costs[i+1][1])
        #returning the minimmum of the costs overall value
        return min(costs[0])
