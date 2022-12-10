
# DUCK TYPING 
class Pycharm:
    # first run method (you can name anything to run)
    def run(self):
        print("compiling")
        print("running")

class myeditor:
    # second run method (same name of previous)
    def run(self):
        print("check")
        print("print")

class laptop:
    def code(self,ide):
        # run method must present (call the both run)
        ide.run()
        
ide=Pycharm()
l1=laptop()
l1.code(ide)
# compiling
# running

ide2=myeditor()
l2=laptop()
l2.code(ide2)
# check
# print