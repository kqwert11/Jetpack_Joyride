from colorama import Back,Fore,Style
class Board():

	def __init__(self,rows,columns):
		
		self.__rows=rows
		self.__columns=columns
		self.__matrix=[]

	@property
	def rows(self):
		return self.__rows
	@rows.setter
	def rows(self,a):
		self.__rows = a

	@property
	def columns(self):
		return self.__columns
	@columns.setter
	def columns(self,a):
		self.__columns = a

	@property
	def matrix(self):
		return self.__matrix
	@matrix.setter
	def matrix(self,a):
		self.__matrix = a
	

	def create_board(self):

		for i in range (self.rows):
			self.new=[]
			for j in range (self.columns):
				if i==0 or i==self.rows-1:
					self.new.append("-")
			
				elif j==0 or j==self.columns-1:
					self.new.append("|")
			
				else:
					self.new.append(" ")
			self.matrix.append(self.new)

	def print_board(self,xcoor,rel_pos,shield_state,position):
		
		print("\033[2;0H")
		str1=""
		for i in range (self.rows):

			for j in range (min(400,xcoor - rel_pos) , min(xcoor - rel_pos + 200,600)):
		
				if i==position[0] and j==position[1] and shield_state ==1:
					str1+=(Fore.RED + Back.WHITE +  Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0] and j==position[1]+1 and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0] and j==position[1]-1 and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0]+1 and j==position[1] and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0] +1 and j==position[1]+1 and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0] +1 and j==position[1]-1 and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif i==position[0] -1 and j==position[1] and shield_state == 1:
					str1+=(Fore.RED + Back.WHITE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
			
				elif self.matrix[i][j]=='$':
					str1+=(Fore.YELLOW  + self.matrix[i][j] + Style.RESET_ALL)
		
				elif self.matrix[i][j]=='0':
					str1+=(Fore.YELLOW  + Back.RED+ self.matrix[i][j] + Style.RESET_ALL)

				elif self.matrix[i][j]=='M':
					str1+=(Fore.RED + Back.YELLOW + self.matrix[i][j]+Style.RESET_ALL)
			
				elif self.matrix[i][j]=='>':
					str1+=(Fore.CYAN + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif self.matrix[i][j]=='-':
					str1+=(Fore.CYAN + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				
				elif self.matrix[i][j]=='(':
					str1+=(Fore.GREEN + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
				

				elif self.matrix[i][j]=='/' or self.matrix[i][j]=='\\':
					str1+=(Fore.BLUE + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)
			
				elif self.matrix[i][j]=='=':
					str1+=(Fore.GREEN + Style.BRIGHT+self.matrix[i][j]+Style.RESET_ALL)

				else:
					str1+=(self.matrix[i][j])
			str1+='\n'

		print(str1)
			