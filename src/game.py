import time
import signal
import time
import os
import random
import math
from colorama import Back,Fore,Style
position=[47,10]
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from board import Board
from mando import Mando
from boss import boss
# from bg_objects import obstacles
from bg_objects import vertical_obs
from bg_objects import horizontal_obs
from bg_objects import diagonal_obs
from bg_objects import obstacles
from bg_objects import coins
from bg_objects import magnet
from bg_objects import bullets
from snow_balls import snow_balls
boad = Board(50,600)
boad.create_board()
boss1 = boss([40,540])
boss1.reappear_boss(boad.matrix) 

mag_present=0
for i in range(0,6):
	a=random.randint(0,5)

	if i==5 and mag_present == 0:
		mag1=magnet([random.randint(5,43),random.randint((i+1)*2*30,(i+1)*2*30+15)])
		mag1.place_magnet(boad.matrix)
		mag_present=1
	elif a%4==1:
		obs1=vertical_obs(random.randint(10,15),[random.randint(5,48),random.randint((i+1)*2*30,(i+1)*2*30+15)])
		# obs1=vertical_obs()
		obs1.place_obs(boad.matrix)

	elif a%4==2:
		obs1=horizontal_obs(random.randint(10,15),[random.randint(5,43),random.randint((i+1)*2*30,(i+1)*2*30+15)])
		obs1.place_obs(boad.matrix)
	
	elif a%4==0:
		obs1=diagonal_obs(random.randint(10,15),[random.randint(5,43),random.randint((i+1)*2*30,(i+1)*2*30+15)])
		obs1.place_obs(boad.matrix)

	else:
		if mag_present == 0:
			mag1=magnet([random.randint(5,43),random.randint((i+1)*2*30,(i+1)*2*30+15)])
			mag1.place_magnet(boad.matrix)
			mag_present=1

		else:		
			obs1=diagonal_obs(random.randint(10,15),[random.randint(5,43),random.randint((i+1)*2*30,(i+1)*2*30+15)])
			obs1.place_obs(boad.matrix)

	coin1=coins(random.randint(5,10),[random.randint(5,43),random.randint((i*2*30)+30,(i*2*30)+45)])
	coin1.place_coins(boad.matrix)
r = 0
x1 = mag1.coor[0] 
y1 = mag1.coor[1] 

man= Mando(position, "LEFT", boad.matrix,0,0,3)
height=49-man.position[0]
sheild_state=0
sheild_avalability=True

xcoor=man.position[1]
rel_pos = 10
boad.print_board(xcoor,rel_pos,sheild_state,man.position)
man.initial_print_mando(boad.matrix,position)
fg =0
ball_lis=[]
bul_list = []
gravity_time=0
def movemando():
	''' moves Mando'''
	global gravity_time
	global bum_list
	global rel_pos
	global height
	global fg
	global shield_time
	global sheild_state
	global time_speed
	global sheild_avalability
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.04):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	char = user_input()
	if char == 'w':
		if height < 47 :
			gravity_time=0
			x=man.check_move(char,boad.matrix,sheild_state)
			boss1.move_boss(char,boad.matrix)
			height += x

	if char == 's':
		if height > 2 :
			x=man.check_move(char,boad.matrix,sheild_state)
			boss1.move_boss(char,boad.matrix)
			height -= x
	
	if char == 'd':
		if rel_pos < 198:
			x=man.check_move(char,boad.matrix,sheild_state)
			rel_pos += x
	
	if char == 'a':
		if rel_pos > 1 :
			x=man.check_move(char,boad.matrix,sheild_state)
			rel_pos -= x
	
	if char == 'q':
		quit()

	if char == 'f':
		bul_num=bullets([man.position[0],man.position[1]+2])
		bul_num.place_bullet(boad.matrix)
		bul_list.append(bul_num)

	if char == ' ':
		if sheild_state !=1 :
			if sheild_avalability is True:
				sheild_avalability = False
				sheild_state=1
				shield_time=time.time()

	if char == 'r':
		time_speed/=2



rel_pos = man.position[1]
ini_time=time.time()
t1=time.time()
t2=time.time()
t3=time.time()
shield_time=time.time() - 60
os.system('clear')
val=100
time_speed=0.15
while True:

	if sheild_state ==1 and time.time() - shield_time > 10:
		sheild_state=0
		shield_time=time.time()
		sheild_avalability = False

	print("\033[0;0H")
	print("Time remaining: ",end="              ")
	a=150-time.time()+ini_time
	if a<0 and boss1.lives > 0:
		os.system('clear')
		print("Time Over!!")
		quit()
	if a<0:
		a=0
	print ("{0:.1f}".format(a),end="             ")
	print("Coins: ",man.coins,end="           ")
	print("Lives Left: ",man.lives_left,end="             ")
	print("Score: ",man.score,end="      ")
	
	a=60-(time.time()-shield_time)
	if sheild_state == 1:
		print(Fore.RED + Back.WHITE +"Sheild Activated" + Style.RESET_ALL,end="           ")

	elif time.time() - shield_time <= 60:
		print("Sheild available in: ",end="  ")
		print( "{0:.1f}".format(a),end="             ")

	elif time.time() - shield_time >60:
		print("Sheild is Available",end="           ")
		sheild_avalability=True

	if xcoor - rel_pos >380:
		print("Boss Lives: ",boss1.lives,end='         ')

	if boss1.lives <=0:
		boss1.disappear_boss(boad.matrix)
	movemando()
	if man.position[1] == 598:
		os.system('clear')
		print("You won!!")
		quit()
	xcoor=man.position[1]
	if man.lives_left < 0:
		os.system('clear')
		man.lives_left=0
		quit()
		quit()

	if time.time() - t1 >= time_speed:
		if xcoor - rel_pos <400:
			x=man.check_move('d',boad.matrix,sheild_state)

		elif boss1.lives<=0:
			man.score+=val
			x=man.check_move('d',boad.matrix,sheild_state)
			val=0

		if man.position[0] < x1 + 20 and man.position[0] > x1-20 and man.position[1] < y1 + 20 and man.position[1] > y1-20:
			if man.position[0] > x1:
				if height < 47:
					x=man.check_move('w',boad.matrix,sheild_state)
					height+=x
					if height < 47:
						x=man.check_move('w',boad.matrix,sheild_state)
						height+=x
			else:
				if height > 2:
					x=man.check_move('s',boad.matrix,sheild_state)
					height-=x
			if man.position[1] > y1:
				if rel_pos > 1:
					x=man.check_move('a',boad.matrix,sheild_state)
					rel_pos-=x
					if rel_pos > 1:
						x=man.check_move('a',boad.matrix,sheild_state)
						rel_pos-=x
					
			else:
				if rel_pos < 198:
					x=man.check_move('d',boad.matrix,sheild_state)
					rel_pos+=x
			gravity_time=0
		
		else:
			if height < 2:
				gravity_time=0
			else:
				gravity_time+=1
				gravity_times = math.ceil(0.5*9.8*gravity_time*gravity_time/1000)
				for i in range(gravity_times):
					if height > 2:
						x=man.check_move('s',boad.matrix,sheild_state)
						height-=x
						boss1.move_boss('s',boad.matrix)
		
		t=-1
		for i in bul_list:
			t+=1
			a,b,c=i.move_bullet(boad.matrix,man.position,rel_pos,boss1)
			man.score+=(3*c)
			c=0
			if b==1:
				boss1.lives -=1
			if a==0:
				bul_list.remove(bul_list[t])
			else:
				a,b,c=i.move_bullet(boad.matrix,man.position,rel_pos,boss1)
				man.score+=(3*c)
				c=0
				if a==0:
					bul_list.remove(bul_list[t])
				if b==1:
					boss1.lives -=1
			
		t=-1
		for i in ball_lis:
			t+=1
			a,b=i.move_ball(boad.matrix)
			if a==0:
				ball_lis.remove(ball_lis[t])
				if b==1:
					if sheild_state ==0:
						man.lives_left-=1
			elif i.coor[1] < xcoor -rel_pos-20:
				ball_lis.remove(ball_lis[t])
			

		xcoor=man.position[1]
		boad.print_board(xcoor,rel_pos,sheild_state,man.position)
		t1=time.time()

	if time.time() -t3 >=0.9:
		
		if xcoor -rel_pos > 380:
			if boss1.lives > 0:
				c1 = boss1.position
				x1 = c1[0]
				x2 = c1[1]
				s_b1=snow_balls([x1, x2])
				s_b1.place_ball(boad.matrix)
				ball_lis.append(s_b1)
		t3=time.time()
			
