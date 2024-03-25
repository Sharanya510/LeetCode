class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        time_to_reach_stack = []
        for p,s in pairs:
            reach_location_at_time = (target-p)/s
            time_to_reach_stack.append(reach_location_at_time)
            if len(time_to_reach_stack) >= 2 and time_to_reach_stack[-1] <= time_to_reach_stack[-2]:
                time_to_reach_stack.pop()
        return len(time_to_reach_stack)
        
        # APPRAOCH --> BRUTE FORCE
        # cars = sorted(zip(position, speed))  # Sort cars by position
        # fleets = len(cars)  # Initially, each car forms a fleet by itself
        # for i in range(len(cars) - 1):
        #     for j in range(i + 1, len(cars)):
        #         time_i = (target - cars[i][0]) / cars[i][1]
        #         time_j = (target - cars[j][0]) / cars[j][1]
        #         if time_i <= time_j:  # Using less than or equal here
        #             fleets -= 1
        #             break
        # return fleets