class obstacles():

	def __init__ (self,length,coor):
		self.__length=length
		self.__coor=coor
		self.__state=0

	@property
	def length(self):
		return self.__length
	@length.setter
	def length(self,a):
		self.__length = a
	
	
	@property
	def coor(self):
		return self.__coor
	@coor.setter
	def coor(self,a):
		self.__length = a
	
	@property
	def state(self):
		return self.__state
	@state.setter
	def state(self,a):
		self.__state = a
	

	def place_obs(self,matrix):

		for i in range (self.coor[1],min(self.coor[1]+self.length,599)):
			matrix[self.coor[0]][i]="0"
		self.state=1

class vertical_obs(obstacles):

	def place_obs(self,matrix):
		for i in range (self.coor[0],min(self.coor[0]+self.length,49)):
			matrix[i][self.coor[1]]="0"
		self.state=1

class horizontal_obs(obstacles):
	
	def place_obs(self,matrix):
		super().place_obs(matrix)

		# for i in range (self.coor[1],min(self.coor[1]+self.length,599)):
		# 	matrix[self.coor[0]][i]="0"
		# self.state=1

class diagonal_obs(obstacles):

	def place_obs(self,matrix):
		for i in range (0,self.length):
			if self.coor[0]+i>=48:
				break
			if self.coor[1]+i>599:
				break
			matrix[self.coor[0]+i][self.coor[1]+i]="0"
		self.state=1
			

class coins():

	def __init__ (self,length,coor):
		self.coor=coor
		self.length=length
	

	def place_coins(self,matrix):
		for i in range (self.coor[1],self.coor[1]+self.length):
				matrix[self.coor[0]][i]='$'


class magnet():

	def __init__ (self,coor):
		self.coor=coor
		
	def place_magnet(self,matrix):
		matrix[self.coor[0]][self.coor[1]]="M"


class bullets():
	def __init__(self,coor):
		self.coor=coor
		self.store=[]
		self.possible_collision = ["$"," ","M","-"]

	def place_bullet(self,matrix):
		self.store = [matrix[self.coor[0]][self.coor[1]+2],matrix[self.coor[0]][self.coor[1]+3],matrix[self.coor[0]][self.coor[1]+4]]
		matrix[self.coor[0]][self.coor[1]+2]="="
		matrix[self.coor[0]][self.coor[1]+3]="="
		matrix[self.coor[0]][self.coor[1]+4]=">"

	def move_bullet(self,matrix,position,rel_pos,boss):
		
		matrix[self.coor[0]][self.coor[1]+2]=self.store[0]
		matrix[self.coor[0]][self.coor[1]+3]=self.store[1]
		matrix[self.coor[0]][self.coor[1]+4]=self.store[2]
		x=self.check_collision(matrix)
		if x==1:
			return 0,0,0
		
		elif x==2:
			return 0,1,0
		
		self.coor[1]+=3
		
		if self.coor[1] < min(position[1] + 198 - rel_pos,593):
			self.store=[]
			self.store.append(matrix[self.coor[0]][self.coor[1]+2])
			self.store.append(matrix[self.coor[0]][self.coor[1]+3])
			self.store.append(matrix[self.coor[0]][self.coor[1]+4])
			matrix[self.coor[0]][self.coor[1]+2]="="
			matrix[self.coor[0]][self.coor[1]+3]="="
			matrix[self.coor[0]][self.coor[1]+4]=">"
		
			if x==0:
				return 1,0,1
		
			else:
				return 1,0,0
		
		else:
			return 0,0,0


	def diappear_bullet(self,matrix):
		matrix[self.coor[0]][self.coor[1]]=" "
		matrix[self.coor[0]][self.coor[1]+1]=" "
		matrix[self.coor[0]][self.coor[1]+2]=" "

	def check_collision(self,matrix):
		if self.store[0] == '0' or self.store[1] == '0' or self.store[2]=='0':

			if self.store[0]=='0':
				x1=self.coor[0]
				y1=self.coor[1]+2

			elif self.store[1]=='0':
				x1=self.coor[0]
				y1=self.coor[1]+3

			elif self.store[2]=='0':
				x1=self.coor[0]
				y1=self.coor[1]+4

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2>0 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2-=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2<49 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2+=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while y2>0 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				y2-=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while y2<599 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				y2+=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2>0 and y2>0 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2-=1
				y2-=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2<49 and y2>0 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2+=1
				y2-=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2>0 and y2<599 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2-=1
				y2+=1

			x2=x1
			y2=y1
			matrix[x2][y2]="0"
			while x2<49 and y2<599 and matrix[x2][y2] not in self.possible_collision:
				matrix[x2][y2]=" "
				x2+=1
				y2+=1
			matrix[x2][y2]=" "
			return 0
		
		elif self.store[0] == '\\' or self.store[1] == '\\' or self.store[2]=='\\':
			return 1
		
		elif self.store[0] == '|' or self.store[1] == '|' or self.store[2]=='|':
			return 1
		
		elif self.store[0] == '/' or self.store[1] == '/' or self.store[2]=='/':
			return 1

		elif self.store[0] == '$' or self.store[1] == '$' or self.store[2]=='$':
			return 4

		elif self.store[0] == '(' or self.store[1] == '(' or self.store[2]=='(':
			return 2
		
		elif self.store[0] == ')' or self.store[1] == ')' or self.store[2]==')':
			return 2
		
		elif self.store[0] == '=' or self.store[1] == '=' or self.store[2]=='=':
			return 2
		
		elif self.store[0] == '_' or self.store[1] == '_' or self.store[2]=='_':
			return 2
		
		elif self.store[0] == '[' or self.store[1] == '[' or self.store[2]=='[':
			return 2

		elif self.store[0] == '<' or self.store[1] == '<' or self.store[2]=='<':
			return 2

		elif self.store[0] == '\'' or self.store[1] == '\'' or self.store[2]=='\'':
			return 2


		elif self.store[0] == ' ' or self.store[1] == ' ' or self.store[2]==' ':
			return 3


		else:
			return 2
