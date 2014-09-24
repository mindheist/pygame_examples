class Boat():
	#tonnage = 0
	#isDocked = True
	#name = ""

	def __init__(self,tonnage,isDocked,name):
		self.tonnage = tonnage
		self.isDocked = isDocked
		self.name = name


	def dock(self):
		if self.isDocked == True :
			print "The Boat is already docked"
		else :
			self.isDocked = False
			print "The boat has been undocked"

	def undock(self):
		if self.isDocked == False :
			print "The boat is already undocked"
		else :
			self.isDocked = False
			print "The boat has been undocked"
	
	def print_boat(self):
		print "tonnage of boat is " , self.tonnage
		print "name of the boat is" , self.name
		print "Dock Status of Boat is " , self.isDocked
    

b = Boat(100,False,"Titanic")
b.print_boat()


# Submarine is a subclass of Boat 

class Submarine(Boat):
	def submerge(self):
		print ("submerge")