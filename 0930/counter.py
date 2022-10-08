class Counter:
    def __init__(self, initValue = 0):
        self.count = initValue

    def reset(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get(self):
        return self.count

a = Counter(100) #initValue가 아닌 100으로 초기화
print(a.get())
a.count = 50

b = Counter() #initValue로 초기화
print(b.get())





