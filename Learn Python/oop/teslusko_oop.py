class Computer:
    
    #static variable
    year = 2019

    def __init__(self, cpu, ram):
    	#instance variables are declared inside a constructor
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("config is ", self.cpu, self.ram)

    def compare(self, other):
        if self.ram == other.ram:
            return True
        else:
            return False

com1 = Computer('i5', '16')
com2 = Computer('Ryzen', '8')

#Computer.config(com1)
#Computer.config(com2)

com1.config()
com1.ram = '8'
com2.config()

if com1.compare(com2):
    print("They are same")
else:
    print("They are different")

Computer.year = 2020
print(com1.year)
print(com2.year)