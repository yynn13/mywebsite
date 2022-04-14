import pygame
import time
pygame.init()

win = pygame.display.set_mode((800,600))

pygame.display.set_caption('game')

swid=800
shit=600

class hitdelay():
	    def __init__(self):
	        self.last = pygame.time.get_ticks()
	        self.cooldown = 500    

	    def hitdela(self):
	    	# fire gun, only if cooldown has been 0.3 seconds since last
	        now = pygame.time.get_ticks()
	        if now - self.last >= self.cooldown:
	            self.last = now
	            box.phit()

class enemy(object):
	def __init__(self,x,y,wid,hit,end,end2):
		self.x = x
		self.y = y 
		self.wid = wid 
		self.hit = hit
		self.end = end
		self.end2 = end2
		self.path = [self.x, self.end]
		self.path2 = [self.y, self.end2] 
		self.velx = 10
		self.vely = 10
		self.hitbox= (self.x, self.y,self.wid,self.hit)
	def draw(self,win):
		self.move()
		self.hitbox= (self.x, self.y,self.wid,self.hit)
		pygame.draw.rect(win,'red',(self.x,self.y,self.wid,self.hit))
		pygame.draw.rect(win,'blue', (self.x,self.y,self.wid,self.hit),2)
	def move(self):

		if self.velx > 0:	
			if self.x + self.velx < self.path[1]:
				self.x += self.velx	
			else:
				self.velx = self.velx* -1	
		else:
			if self.x - self.velx > self.path[0]:
				self.x += self.velx
			else:
				self.velx = self.velx*-1

		if self.vely>0:
			if self.y + self.vely < self.path2[1]:
				self.y += self.vely	
			else:
				self.vely = self.vely* -1	
		else:
			if self.y+200 - self.vely > self.path2[0]:
				self.y += self.vely
			else:
				self.vely = self.vely*-1						
class enemy2(object):
	def __init__(self,x,y,wid,hit,end,end2):
		self.x = x
		self.y = y 
		self.wid = wid 
		self.hit = hit
		self.end = end
		self.end2 = end2
		self.path = [self.x, self.end]
		self.path2 = [self.y, self.end2] 
		self.velx = 10
		self.vely = 10
		self.hitbox= (self.x, self.y,self.wid,self.hit)
	def draw(self,win):
		self.move()
		self.hitbox= (self.x, self.y,self.wid,self.hit)
		pygame.draw.rect(win,'red',(self.x,self.y,self.wid,self.hit))
		pygame.draw.rect(win,'blue', (self.x,self.y,self.wid,self.hit),2)
	def move(self):

		if self.velx > 0:	
			if self.x + self.velx < self.path[1]:
				self.x += self.velx	
			else:
				self.velx = self.velx* -1	
		else:
			if self.x - self.velx > self.path[0]:
				self.x += self.velx
			else:
				self.velx = self.velx*-1

		if self.vely>0:
			if self.y + self.vely < self.path2[1]:
				self.y += self.vely	
			else:
				self.vely = self.vely* -1	
		else:
			if self.y+100 - self.vely > self.path2[0]:
				self.y += self.vely
			else:
				self.vely = self.vely*-1		

class player(object):
	def __init__(self,x,y,wid,hit):
		self.x = x
		self.y = y 
		self.wid = wid 
		self.hit = hit 
		self.vel = 10
		self.hitbox= (self.x, self.y,self.wid,self.hit)
		self.health = 5
		self.live = True
	def draw(self,win):
		if self.live:
			self.hitbox= (self.x, self.y,self.wid,self.hit)
			pygame.draw.rect(win,'red',(300,20,100,20))
			pygame.draw.rect(win,'green',(300,20,100- 20 *(5 - self.health),20))
			pygame.draw.rect(win,'green', (self.x,self.y,self.wid,self.hit),)
			pygame.draw.rect(win,'blue', self.hitbox,2)

	def phit(self):
		if self.health > 0:
			self.health -= 1
		else:
			self.live = False	
		print('hit')
		print(self.health)
class restart(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def draw(self):
		pass
def gameover():
	game_over = font.render('GAME OVER',1, 'white') 
	win.fill('black')
	win.blit(game_over,(300,300))
	pygame.display.update()
	time.sleep(5)
	pygame.quit()	

	
def redrawwin():
	box.draw(win)
	redbox2.draw(win)
	redbox.draw(win)
	pygame.display.update()
redbox2 = enemy2(300,100,50,55,750,545)
font = pygame.font.SysFont('Calibri',50)	
redbox = enemy(10,200,50,55,750,545)
box = player(400,300,15,15)
hitdel = hitdelay()
run = True

while run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run = False

	if box.y - box.hit < redbox.hitbox[1] + redbox.hitbox[3] and box.y + box.hit > redbox.hitbox[1]:
		if box.x + box.wid > redbox.hitbox[0] and box.x - box.wid < redbox.hitbox[0] + redbox.hitbox[2]:
			hitdel.hitdela()
	if box.y - box.hit < redbox2.hitbox[1] + redbox2.hitbox[3] and box.y + box.hit > redbox2.hitbox[1]:
		if box.x + box.wid > redbox2.hitbox[0] and box.x - box.wid < redbox2.hitbox[0] + redbox2.hitbox[2]:
			hitdel.hitdela()				
	if box.health == 0:
		gameover()
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and box.x > 15:
		box.x -= box.vel

	if keys[pygame.K_RIGHT] and box.x < swid - 15-15:
		box.x += box.vel

	if keys[pygame.K_UP] and box.y > 15:
		box.y-=box.vel

	if keys[pygame.K_DOWN] and box.y < shit - 15-15:
		box.y+=box.vel		

	win.fill('black')
	redrawwin()




pygame.quit
