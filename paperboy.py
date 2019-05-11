class Paperboy:

    def __init__(self, name, experience, earnings):
        self.name = name 
        self.experience = 0
        self.earnings = 0
    
    def __str__(self):
        return "Name= {}, Experience= {}, Earnings= ${}".format(self.name, self.experience, self.earnings)

    def quota(self):
        return 50 + self.experience/2

    def deliver(self, start_address, end_address):       
        papers_delivered = (end_address - start_address + 1)
        
        if self.quota() < papers_delivered:
            self.earnings = self.earnings + ((0.50 * (papers_delivered - self.quota())) + (0.25 * self.quota()))
            
        elif self.quota() > papers_delivered:
            self.earnings = self.earnings - 2 + 0.25 * papers_delivered
        
        self.experience = self.experience + papers_delivered
        return self.earnings       

    def report(self):
        return "I'm {}, I've delivered {} papers and I've earned ${} so far!".format(self.name, self.experience, self.earnings)

goten = Paperboy("Judoboy", 0, 0)
print(goten)
print(goten.deliver(101,160))
print(goten.report())
print(goten.deliver(1,75))
print(goten.report())