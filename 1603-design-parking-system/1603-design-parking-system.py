class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.hash_map = {}
        self.res = [self.big, self.medium, self.small]
        
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
            elif self.big == 0:
                return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            elif self.medium == 0:
                return False
        elif carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
            elif self.small == 0:
                return False
            


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)