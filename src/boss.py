# from mando import Mando
class boss():
	def __init__ (self,position):
		self.__coor={}
		self.__fig=[]
		self.__shape=[]
		self.__position=position
		self.__lives =5
		self.__store={}

	@property
	def coor(self):
		return self.__coor
	@coor.setter
	def coor(self,a):
		self.__coor = a

	@property
	def fig(self):
		return self.__fig
	@fig.setter
	def fig(self,a):
		self.fig = a

	@property
	def shape(self):
		return self.__shape
	@shape.setter
	def shape(self,a):
		self.__shape = a

	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self,a):
		self.__position = a

	@property
	def lives(self):
		return self.__lives
	@lives.setter
	def lives(self,a):
		self.__lives = a

	@property
	def store(self):
		return self.__store
	@store.setter
	def store(self,a):
		self.__store = a


		for i in range (self.position[0]-7,self.position[0]+8):
			self.coor[i]=[]
			for j in range (self.position[1]-19,self.position[1]+20):
				self.coor[i].append(j)
	
		with open("./boss.txt") as obj:
			for line in obj:
				self.fig.append(line.strip('\n'))
		
		for i in range(15):
			for j in range(39):
				x=self.fig[i][j]
				self.shape.append(x)
		
	def reappear_boss(self,matrix):	
		t=0
		for i in self.coor:
			for j in self.coor[i]:
				matrix[i][j]=self.shape[t]
				t+=1
		
	def disappear_boss(self,matrix):

		for i in self.coor:
			for j in self.coor[i]:
				matrix[i][j]=" "
		

	def move_boss(self,x,matrix):

		self.disappear_boss(matrix)
		self.store = {}

		for i in self.coor:
			self.store[i] = []
			for j in self.coor[i]:
				self.store[i].append(j)

		coor_new ={}
		if x=='a':
			for i in self.coor:
				coor_new[i] = []
				for j in self.coor[i]:
					coor_new[i].append(j-1)
			


		elif x=='d':
			for i in self.coor:
				coor_new[i] = []
				for j in self.coor[i]:
					coor_new[i].append(j+1)
			

		elif x=='w':
			for i in self.coor:
				coor_new[i-1] = []
				for j in self.coor[i]:
					coor_new[i-1].append(j)
		

		elif x=='s':
			for i in self.coor:
				coor_new[i+1] = []
				for j in self.coor[i]:
					coor_new[i+1].append(j)

		fg=1
		self.coor.clear()
		for i in coor_new:
			self.coor[i] = []
			for j in coor_new[i]:
				self.coor[i].append(j)
		for i in self.coor:
			for j in self.coor[i]:
				if matrix[i][j] == "-":
					x1=i
					y1=j
					fg=0
					break
			if fg==0:
				break

		if fg==1:
			# print("ASDASD")
			if x=='a':
				self.position[1]-=1
			elif x=='d':
				self.position[1]+=1
			elif x=='w':
				self.position[0]-=1
			elif x=='s':
				self.position[0]+=1
			
			self.reappear_boss(matrix)
				
			return 1

		else:
			if matrix[x1][y1]=='-':
				self.coor.clear()
				for i in self.store:
					self.coor[i] = []
					for j in self.store[i]:
						self.coor[i].append(j)
				self.reappear_boss(matrix)
				

