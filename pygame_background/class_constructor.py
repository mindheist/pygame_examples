class Game_Character():
	def __init__(self,name,sex,max_hit_points,current_hit_points,max_speed):
		print "Initilizing Game_Character"
		self.name = name
		self.sex = sex
		self.max_hit_points = max_hit_points
		self.current_hit_points = current_hit_points
		self.max_speed = max_speed

	def increase_max_speed(self,max_speed):
		print "max_speed before increasing is",max_speed
		max_speed = max_speed + 10
		print "max_speed after increasing is ",max_speed

	def increase_current_hit_points(self,current_hit_points):
		print "the current_hit_points is " , current_hit_points
		current_hit_points = current_hit_points + 10
		print "the increased current_hit_points is " , current_hit_points

	def display_character(self):
		print "Name = " , self.name
		print "Sex =  " , self.sex
		print "Max Hit Points = " ,self.max_hit_points
		print "Current hit Points = " ,self.current_hit_points
		print "Max Speed = " , self.max_speed

mario = Game_Character("mario","Male",100,100,0)
mario.display_character()
print("===========================")

