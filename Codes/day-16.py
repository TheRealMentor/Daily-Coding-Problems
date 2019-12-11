class LogDataStructure:
    def __init__(self, N):
        self.n = N
        self.logs = []
    
    def record(self, order_id):
        if len(self.logs) < self.n:
            self.logs.append(order_id)
        else:
            print('No more space!')
    
    def get_last(self, i):
        return self.logs[-i]
    
website = LogDataStructure(6)
website.record(231)
website.record(641)
website.record(825)
website.record(536)

print(website.get_last(2))

website.record(913)
website.record(342)

print(website.get_last(1))

website.record(23432)