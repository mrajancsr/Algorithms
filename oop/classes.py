#practing object oriented from chapter 15 in quick python book
import math
class Circle:
	pi = math.pi
	def __init__(self,radius=1):
		self.radius = radius
	def area(self):
		return self.radius**2 * Circle.pi # we can access class variable by using class_name.pi
		# we can also replace Circle.pi with self.__class__.pi

print(Circle.pi)  # we can access Class variables

Circle.pi = 4 # we can also assign

print('value of circle after assignment is : ', Circle.pi)

Circle.pi = math.pi
print(Circle.pi)

#creating instance of class Circle
c = Circle(2)
print("the value of area is: {}".format(c.area()))

print(c.pi) #we can also access class variables through the object.  
#but the above method is risky.  

#this is much better.  we access pi, a variable of class Circle
print(c.__class__.pi)

c1 = Circle()
c2 = Circle(2)

c1.pi = 3.14
print(c1.pi) #we create pi to be instance variable of class circle.  

print(c2.pi) # here we are accessing the class variable pi

print("Circle.pi is: {}".format(Circle.pi))

import circle
c1 = circle.Circle()
c2 = circle.Circle(2)

print(circle.Circle.total_area())

c2.radius = 4
print('using static method: ', circle.Circle.total_area())
print('Notice that two objects are created with circle.Circle.all_circles', circle.Circle.all_circles) #notice only two objects have been created

print('using @classmethod: ', circle.Circle.total_area1())  #using @classmethod


