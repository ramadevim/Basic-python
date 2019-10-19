class Pycharm:
    def code(self):
        print('compile')
        print('execute')

class Laptop:
    def sw(self,ide):
        # self.ide=ide
        ide.code()

ide=Pycharm()

obj=Laptop()
print(obj.sw(ide))
