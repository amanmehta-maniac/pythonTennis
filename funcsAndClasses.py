class Player:
	__j=0
	def __init__(self,score,gameCount,setCount):
		self.score=score
		self.gameCount=gameCount
		self.setCount=setCount
	def point(self):
		if self.score==0:
			self.score=15
		elif self.score==15:
			self.score=30
		elif self.score==30:
			self.score=40
		elif self.score==40:
			self.score="Game"
			if Tennis.deuce==1:
				self.score="A"
		elif self.score=="A":
			self.score="win"
		elif self.score==" ":
			reDuece()
		Player.__j+=1
		print "This is mistake number",Player.__j,"for the match in total"
		print "New statistics of the ongoing match are:"
	def game(self,winner):
		self.gameCount=1+self.gameCount
		print winner," won the game "
	def setWin(self):
		self.setCount+=1
class Tennis(Player):
	i=1;
	deuce=0;
	count=1;
	server=1;
	setNumber=1;
	gameNumber=1;
	striker=1;

def reDeuce():
	player1.score=40
	player2.score=40
def ace(): 
	if Tennis.server==1:
		Tennis.striker=1
		player1.point()
	if Tennis.server==2:
		Tennis.striker=2
		player2.point()
	Tennis.count=Tennis.server;
def fault():
   if Tennis.server==1:
		Tennis.striker=1
		player2.point()
   if Tennis.server==2:
		Tennis.striker=2
		player1.point()
   Tennis.count=Tennis.server
def nonDeuce():
	if player2.score=="Game" and player1.score!=40:
	   player2.game("Player2")
	   Tennis.gameNumber+=1
   	   player1.score=0;
   	   player2.score=0;
	 #  P2winsGame=1;
	if player1.score=="Game" and player2.score!=40:
	   player1.game("Player1")
	   Tennis.gameNumber+=1
   	   player1.score=0;
   	   player2.score=0;
#	   P1winsGame=1
def checkDeuce():
	if player2.score==40 and player1.score==40:
		Tennis.count=Tennis.server
		Tennis.deuce=1
	if player1.score==40 and player2.score=="A":
		player1.score=" "
	if player2.score==40 and player1.score=="A":
		player2.score=" "
	if player1.score=="win":
		player1.score=0
		player2.score=0
		player1.game("Player1")
		Tennis.gameNumber+=1
		P1winsGame=1;
		Tennis.deuce=0;
	if player2.score=="win":
		player1.score=0
		player2.score=0
		player2.game("Player2")
		Tennis.gameNumber+=1
		P2winsGame=1;
		Tennis.deuce=0;
def maintainServe():
		if (Tennis.gameNumber%2==1 and Tennis.setNumber%2==1) or (Tennis.gameNumber%2==0 and Tennis.setNumber%2==0):
			Tennis.server=1;
		else:
			Tennis.server=2;

def checkSet():
	if player1.gameCount==6 and player2.gameCount<5:
		player1.gameCount=0
		player2.gameCount=0
		player1.setWin()
		P1winsSet=1;
		Tennis.gameNumber=1;
		if Tennis.setNumber%2==0:
			Tennis.server=2
			Tennis.count=2
		else:
			Tennis.server=1
			Tennis.count=1
		Tennis.setNumber+=1
	elif player2.gameCount==6 and player1.gameCount<5:
		player2.setWin()
		Tennis.gameNumber=1;
		if Tennis.setNumber%2==0:
			Tennis.server=2
			Tennis.count=2
		else:
			Tennis.server=1
			Tennis.count=1
		player1.gameCount=0
		player2.gameCount=0
		P2winsSet=1;
		Tennis.setNumber+=1
	elif player1.gameCount==7:
		player1.gameCount=0
		player2.gameCount=0
		player1.setWin()
		Tennis.gameNumber=1;
		if Tennis.setNumber%2==0:
			Tennis.server=2
			Tennis.count=2
		else:
			Tennis.server=1
			Tennis.count=1
		Tennis.setNumber+=1
	elif player2.gameCount==7:
		player1.gameCount=0
		player2.gameCount=0
		player2.setWin()
		Tennis.gameNumber=1;
		if Tennis.setNumber%2==0:
			Tennis.server=2
			Tennis.count=2
		else:
			Tennis.server=1
			Tennis.count=1
		Tennis.setNumber+=1
def printFunction(x,Tstriker,i):
           if Tennis.deuce==1:
                        print "DEUCE SITUATION"
           print "Iteration:",i
           print "Player",Tstriker,":",x
           print "P1 Score: ",player1.score
           print "P2 Score: ",player2.score
           print "P1 Game Win Count: ",player1.gameCount
           print "P2 Game Win Count: ",player2.gameCount
           print "P1 Set Win Count: ",player1.setCount
           print "P2 Set Win Count: ",player2.setCount
           print "-------------------------------------------------"
player1=Player(0,0,0)
player2=Player(0,0,0)
