
#TC: O(n)
#SC: O(1)
class Solution(object):
    def minCost(self,costs):
    #iterate through reverser and store value at each step ,from len -2 because we are starting it from before row
        for i in range (len(costs),-2,-1,-1):
            
        #adding the minimum of last row and add it to before row first element and checking the first and second index for zeroth index 
            cost[i][0] +=min(cost[i+1][1],cost[i+1][2])
        #in case of first index check the zeroth and seconf index
            cost[i][1]+= min(cost[i+1][0],cost[i+1][2])
        #incase of second index then check the first and zeroth
            cost[i][2]+= min(cost[i+1][0],cost[i+1][1])
        #returning the minimmum of the costs overall value
        return min(cost[0])
