class Vscode:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("debug using vscode")

class Pycharm:
    def compile(self):
        print("compiling using vscode")
    def execute(self):
        print("execute using vscode")
    def debug(self):
        print("debug using vscode")

class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)


