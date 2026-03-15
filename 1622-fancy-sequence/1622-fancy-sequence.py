class Fancy:

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def append(self, val):
        inv = pow(self.mul, self.MOD-2, self.MOD)
        val = (val - self.add) % self.MOD
        val = (val * inv) % self.MOD
        self.arr.append(val)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD