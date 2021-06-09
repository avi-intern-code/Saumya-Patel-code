class Computer:

    def config(self):
        print("i5, 16gb, 1TB")

a = '8'
print(type(a))

com1 = Computer()
com2 = Computer()

print(type(com1))

Computer.config(com1)
com2.config()

a=5
a.bit_length() #ctrl+click on func for definition


com1.config()
com2.config()
