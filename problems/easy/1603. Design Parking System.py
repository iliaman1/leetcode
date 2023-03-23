class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.current_big = 0
        self.medium = medium
        self.current_medium = 0
        self.small = small
        self.current_small = 0

    def addCar(self, carType: int) -> bool:
        if type(carType) != int or carType < 1 or carType > 3:
            return None

        if carType == 1 and self.current_big + 1 > self.big:
            return False
        elif carType == 1:
            self.current_big += 1
            return True

        if carType == 2 and self.current_medium + 1 > self.medium:
            return False
        elif carType == 2:
            self.current_medium += 1
            return True

        if carType == 3 and self.current_small + 1 > self.small:
            return False
        elif carType == 3:
            self.current_small += 1
            return True


# good short solution
class ParkingSystem1:

    def __init__(self, big: int, medium: int, small: int):
        self.size = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.size[carType] > 0:
            self.size[carType] -= 1
            return True
        return False
