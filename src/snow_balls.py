from bg_objects import bullets
class snow_balls(bullets):

	def __init__ (self,coor):

		self.__coor=coor
		self.__coor2=coor
		self.__shape= ["/", "-", "\\", "|", "-", "|" ,"\\", "-", "/"]


	@property
	def coor(self):
		return self.__coor
	@coor.setter
	def coor(self,a):
		self.__coor = a

	@property
	def coor2(self):
		return self.__coor2
	@coor2.setter
	def coor2(self,a):
		self.__coor2 = a
	
	@property
	def shape(self):
		return self.__shape
	@shape.setter
	def shape(self,a):
		self.__shape = a


	def place_ball(self,matrix):
		t=0
		for i in range (0,3):
			for j in range (0,3):
				matrix[self.coor[0] +i][self.coor[1]-20+j]=self.shape[t]
				t+=1

	def reappear_ball(self,matrix):
		t=0
		for i in range (0,3):
			for j in range (0,3):
				matrix[self.coor[0]+i][self.coor[1]+j-20]=self.shape[t]
				t+=1

	def disappear_ball(self,matrix):
		for i in range (0,3):
			for j in range (0,3):
				matrix[self.coor[0]+i][self.coor[1]+j-20]=" "
		 

	def move_ball(self,matrix):

		self.disappear_ball(matrix)
		self.coor[1] -= 3
		for i in range (0,3):
			for j in range (0,3):
				if matrix[self.coor[0]+i][self.coor[1]+j-20]== ">":
					# self.disappear_ball(matrix)
					return 0,0

				elif matrix[self.coor[0]+i][self.coor[1]+j-20]== "=":
					# self.disappear_ball(matrix)
					return 0,0

				elif matrix[self.coor[0]+i][self.coor[1]+j-20]== "v":
					# self.disappear_ball(matrix)
					return 0,1
				elif matrix[self.coor[0]+i][self.coor[1]+j-20]== "O":
					# self.disappear_ball(matrix)
					return 0,1
				elif matrix[self.coor[0]+i][self.coor[1]+j-20]== "#":
					# self.disappear_ball(matrix)
					return 0,1
				# elif matrix[self.coor[0]+i][self.coor[1]+j-20]== "/":
				# 	# self.disappear_ball(matrix)
				# 	return 0,0
		# self.coor[0] = self.coor[0]
		# if matrix[self.coor[0]][self.coor[1]]=='\\' or matrix[self.coor[0]][self.coor[1]-1]=='\\' or matrix[self.coor[0]][self.coor[1]-2]=='\\':
		# 	return 0 
		self.reappear_ball(matrix)
		return 1,0