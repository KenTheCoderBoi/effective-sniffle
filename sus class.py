class Citizen():
    def __init__(self,name,phone,ID):
        self.name=name
        self.phone=phone
        self.ID=ID
    def create(self):
        print("name:"+self.name)
        print("phone:"+str(self.phone))
        print("ID:"+str(self.ID))
c1=Citizen("sussus",9082923524,298923)
c1.create()
c2=Citizen("EZ",9112002,9112002)
c2.create()