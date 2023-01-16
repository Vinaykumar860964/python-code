class parent:
    def p_fun(self):
        print("this is parent class")
class child(parent):
 def c_fun(self):
        print("this is child class")
obj=child()
obj.c_fun()
obj.p_fun()
