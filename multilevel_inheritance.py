class parent:
    def p_fun(self):
        print("this is parent class")
        
class child(parent):
    def c1f_fun(self):
        print("first child")
class child2(child):
    def c2_fun(self):
        print("second child")
class child3(child2):
    def c3_fun(self):
        print("third child")
        
obj=child3()
obj.c1f_fun()
obj.c2_fun()
obj.c3_fun()
obj.p_fun()