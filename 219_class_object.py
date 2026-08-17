class mouse():
    def setMouse(self,company,color,rating,price):
        self.company=company
        self.color=color
        self.rating=rating
        self.price=price

    def getMouse(self):
        print("mouse info :") 
        print("company :",self.company)
        print("color :",self.color)
        print("rating :",self.rating)
        print("price :",self.price)
        print("---------------------")


m1=mouse()
m1.setMouse("HP","black",4.5,600)
m1.getMouse()


m2=mouse()
m2.setMouse("frontech","red",2.5,300)
m2.getMouse()






