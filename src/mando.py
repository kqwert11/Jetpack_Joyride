import os
class Mando():

	def __init__(self,position,direction,matrix,coins,score,lives_left):
		self.__position=position
		self.__direction=direction
		self.__coor = {position[0] - 1 : [position[1]] ,position[0] : [position[1]-1,position[1],position[1]+1],  position[0] + 1 : [position[1]-1,position[1],position[1]+1]}
		self.__shape1 = [ "O", "|", "v", "|", "/", "#", "\\" ]
		self.__possible_collision = [" ","$","-"]
		self.__coins=0
		self.__score=0
		self.__lives_left=10
		self.__store={}
	
	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self,a):
		self.__position = a

	@property
	def direction(self):
		return self.__direction
	@direction.setter
	def direction(self,a):
		self.__direction = a

	@property
	def coor(self):
		return self.__coor
	@coor.setter
	def coor(self,a):
		self.__coor = a

	@property
	def shape1(self):
		return self.__shape1
	@shape1.setter
	def shape1(self,a):
		self.__shape1 = a

	@property
	def possible_collision(self):
		return self.__possible_collision
	@possible_collision.setter
	def possible_collision(self,a):
		self.__possible_collision = a

	@property
	def coins(self):
		return self.__coins
	@coins.setter
	def coins(self,a):
		self.__coins = a

	@property
	def score(self):
		return self.__score
	@score.setter
	def score(self,a):
		self.__score = a

	@property
	def lives_left(self):
		return self.__lives_left
	@lives_left.setter
	def lives_left(self,a):
		self.__lives_left = a

	@property
	def store(self):
		return self.__store
	@store.setter
	def store(self,a):
		self.__store = a


		# self.not_possible_collision = ["-",""]
	def initial_print_mando(self,matrix,position):
		t=0
		for i in self.coor:
			for j in self.coor[i]:
				matrix[i][j]=self.shape1[t]
				t+=1
				# matrix[position[0]-1+i][position[1]-1+j]=self.shape1[i][j]
				# matrix[j][i]=self.shape1[j-(position[0]-1)][i-(position[1]-1)]

	def disappear_mando(self,matrix):
		for i in self.coor:
			for j in self.coor[i]:
				matrix[i][j]=" "
		# for i in range(0,3):
		# 	for j in range(0,3):
		# 		matrix[position[0]-1+i][position[1]-1+j]=" "

	def reappear_mando(self,matrix):
		# print("\033[52;0H")
		t=0
		for i in self.coor:
			for j in self.coor[i]:
				matrix[i][j]=self.shape1[t]
				t+=1
			# 	print(i,j,end=' ')
			# print()

	def check_move(self,x,matrix,shield_mode):
		# return
		coins=0
		score=0
		temp=[]
		fg=1
		self.disappear_mando(matrix)
		coor_new ={}

		self.store = {}

		for i in self.coor:
			self.store[i] = []
			for j in self.coor[i]:
				self.store[i].append(j)

	
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
		# self.coor = coor_new.copy()
		for i in coor_new:
			self.coor[i] = []
			for j in coor_new[i]:
				self.coor[i].append(j)
		for i in self.coor:
			for j in self.coor[i]:
				if matrix[i][j] in self.possible_collision:
					if matrix[i][j]=='$':
						coins+=1
						score+=1
				else:
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
			
			self.coins+=coins
			self.score+=score
			self.reappear_mando(matrix)
			# print("\033[54;0H")
			# print("wow")
				
			return 1


		else:
			if matrix[x1][y1]=="M":
				# if x!= 'd':
				self.coor.clear()
				for i in self.store:
					self.coor[i] = []
					for j in self.store[i]:
						self.coor[i].append(j)
				# if x=='d':
				# 	self.position[1]+=1
				# print("\033[54;0H")
				# print(x1,y1)
				# print(self.coor)
				self.reappear_mando(matrix)
				if x=='d':
					return -1
				else:
					return 0
				# else:
				# 	return 0

			else:
				# print("\033[54;0H")
				# print("wow")
				# quit()
				if x=='a':
					self.position[1]-=1
				elif x=='d':
					self.position[1]+=1
				elif x=='w':
					self.position[0]-=1
				elif x=='s':
					self.position[0]+=1
				
				x2=x1
				y2=y1
				# os.system('clear')
				# print(x2,y2)
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
				if shield_mode == 0:
					if self.lives_left == 0:
						# if self.shield_state ==0:
							print("Game Over!!")
							quit()
					else:
						# if self.shield_state == 0:
						self.lives_left-=1
						self.reappear_mando(matrix)
				else:
					self.reappear_mando(matrix)
				print("\033[54;0H")
				print(shield_mode)
				return 1

			# self.disappear_mando(matrix)
			# coor_new ={}
		
			# self.coor.clear()
			# # self.coor = coor_new.copy()
			# for i in coor_new:
			# 	self.coor[i] = []
			# 	for j in coor_new[i]:
			# 		self.coor[i].append(j)
			# for i in self.coor:
			# 	for j in self.coor[i]:
			# 		if matrix[i][j] in self.possible_collision:
			# 			if matrix[i][j]=='$':
			# 				coins+=1
			# 				score+=1
			# 		else:
			# 			fg=0
			# 			break
			# if fg==1:
			# 	# print("ASDASD")
			# 	self.coins+=coins
			# 	self.score+=score
			# 	self.reappear_mando(matrix)
			# else:
			# 	self.lives_left-=1
			# 	self.disappear_mando(matrix)


			# self.disappear_mando(matrix)
			# coor_new ={}
		



			# self.coor.clear()
			# # self.coor = coor_new.copy()
			# for i in coor_new:
			# 	self.coor[i] = []
			# 	for j in coor_new[i]:
			# 		self.coor[i].append(j)
			# for i in self.coor:
			# 	for j in self.coor[i]:
			# 		if matrix[i][j] in self.possible_collision:
			# 			if matrix[i][j]=='$':
			# 				coins+=1
			# 				score+=1
			# 		else:
			# 			fg=0
			# 			break
			# if fg==1:
			# 	# print("ASDASD")
			# 	self.coins+=coins
			# 	self.score+=score
			# 	self.reappear_mando(matrix)
			# else:
			# 	self.lives_left-=1
			# 	self.disappear_mando(matrix)
		
			# self.disappear_mando(matrix)
			# coor_new ={}
		


			# self.coor.clear()
			# # self.coor = coor_new.copy()
			# for i in coor_new:
			# 	self.coor[i] = []
			# 	for j in coor_new[i]:
			# 		self.coor[i].append(j)
			# for i in self.coor:
			# 	for j in self.coor[i]:
			# 		if matrix[i][j] in self.possible_collision:
			# 			if matrix[i][j]=='$':
			# 				coins+=1
			# 				score+=1
			# 		else:
			# 			fg=0
			# 			break
			# if fg==1:
			# 	# print("ASDASD")
			# 	self.coins+=coins
			# 	self.score+=score
			# 	self.reappear_mando(matrix)
			# else:
			# 	self.lives_left-=1
			# 	self.disappear_mando(matrix)

	# def print_topbar(self,ini_time):
		