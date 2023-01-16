class vijay_mahto:
    def vij_fun(self):
     print("vijay mahto is a constructor")
    
class vinay_kumar:
    def vin_fun(self):
        print("vinay kumar is software engineer")
class raja_kumar:
    def raja_fun(self):
        print("raja kumar is the small son of mr vijay mahto")
class lakshmi(vinay_kumar,raja_kumar):
    def lak_fun(self):
        print("beautyfull daughter of mr vijay mahto")
v=lakshmi()
v.lak_fun()
v.raja_fun()
v.vin_fun()
v.vij_fun()