class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))  # Sort cars by position
        fleets = len(cars)  # Initially, each car forms a fleet by itself
        for i in range(len(cars) - 1):
            for j in range(i + 1, len(cars)):
                time_i = (target - cars[i][0]) / cars[i][1]
                time_j = (target - cars[j][0]) / cars[j][1]
                if time_i <= time_j:  # Using less than or equal here
                    fleets -= 1
                    break
        return fleets