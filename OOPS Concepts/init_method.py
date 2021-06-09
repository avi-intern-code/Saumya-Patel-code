class Computer:

    # def __init__(self): # for every object it is called once
    #     print("int init")

    def __int__(self, cpu,ram):
        self.cpu = cpu
        self.ram = ram

    # def config(self):
    #     print("i5, 16gb, 1TB")

    def config(self):
        print("Config is ", self.cpu, self.ram)



# com1 = Computer()
# com2 = Computer()

com1 = Computer("i5",16)
com2 = Computer("Ryzen 3",8)

com1.config()
com2.config()