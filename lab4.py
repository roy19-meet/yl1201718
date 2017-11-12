#class animal(object):
	#def __init__(self,sound,name,age,favorite_color):
		#self.sound=sound
		#self.name=name
		#self.age=age
		#self.favorite_color=favorite_color
	#def eat(self,food):
		#print('Yummy!! '+self.name+' is eating '+food)
	#def description(self):
	    #print(self.name+' is '+self.age+' years old and loves the color '+self.favorite_color)
	#def make_sound(self,amount):
		#print(self.sound*amount)    
#j=animal('moo','cow','15','green')
#j.eat('grass')		
#j.description()
#j.make_sound(3)

class person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat_breakfast(self,food):
		print(self.name+' is eating '+food)
	def sports(self,sport):
		print(self.name+' is playing '+sport)	
o=person('jake','17','jerusalem','male')		
o.eat_breakfast('milky')
o.sports('soccer')


class song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
					