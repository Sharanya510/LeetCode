class TimeMap:

    def __init__(self):
        self.hash_map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
            
        self.hash_map[key].append([timestamp, value])
        
        # APPROACH --> BRUTE FORCE
        # if key not in self.hash_map:
        #     self.hash_map[key] = {}
        # self.hash_map[key][timestamp] = value
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        if timestamp < self.hash_map[key][0][0]:
            return ""
        
        left , right = 0, len(self.hash_map[key])
        
        while left < right:
            mid = (left + right) // 2
            if self.hash_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.hash_map[key][right - 1][1]
        
        
        # APPROACH --> BRUTE FORCE
        # if key not in self.hash_map:
        #     return ""
        # for curr_time in range(timestamp, -1, -1 ):
        #     if curr_time in self.hash_map[key]:
        #         return self.hash_map[key][curr_time]
        # return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)