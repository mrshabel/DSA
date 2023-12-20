class WaterBottles:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = 0
        while (numBottles >= numExchange):
            numBottles = (numBottles - numExchange) + 1
            bottlesDrunk += numExchange
        
        return bottlesDrunk + numBottles
    
# create instance of class
bottles = WaterBottles()

bottles1 = bottles.numWaterBottles(9 ,3)
bottles2 = bottles.numWaterBottles(15, 4)

print(f"The bottles drunk in the first problem is {bottles1}\nThe bottles drunk in the second problem is {bottles2}")