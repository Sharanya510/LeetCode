class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        foodCounter = 0
        if not hamsters: 
            return -1
        for i in range(len(hamsters)): 
            #If empty of food continue
            if hamsters[i] != 'H': 
                continue
            #If left is hamster and right is h, return -1
            if (i == 0 or hamsters[i-1] == 'H') and (i == len(hamsters)-1 or hamsters[i+1] == 'H'):
                return -1
            # If left is food bucket, continue
            if i > 0 and hamsters[i-1] == 'F': 
                continue
                   
            # If left is empty or hampster and right is empty, put it to the right.
            if (i == 0 or hamsters[i-1] != 'F') and i != len(hamsters)-1 and hamsters[i+1] == '.':
                hamsters[i+1] = 'F'
                foodCounter +=1 
            # If left is empty and right is hamster, put it to the left
            elif i > 0 and hamsters[i-1] == '.' and (i == len(hamsters)-1 or hamsters[i+1] == 'H'): 
                hamsters[i-1] = 'F'
                foodCounter +=1 

        return foodCounter