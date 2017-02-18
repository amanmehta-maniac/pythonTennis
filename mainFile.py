import funcsAndClasses,sys
infile=sys.argv[1]
from funcsAndClasses import *
	reader = csv.reader(f, delimiter=' ')
	for row in reader:
		x=row[1]
		if Tennis.count%2==1:
			if x=="Serve":
				Tennis.count+=1
#				print "server",Tennis.server
				Tennis.striker=Tennis.server
			if x=="Backhand" or x=="Forehand":
			   Tennis.count+=1
			   Tennis.striker=1
			if x=="Fault":
				fault()
			if x=="Nets" or x=="PointLost-Out" or x=="PointLost-SameSide":
				player1.point()
				Tennis.striker=2
				Tennis.count=Tennis.server
			if x=="PointLost-CouldNotReach":
				player2.point()
				Tennis.striker=1
			if x=="Ace":
				ace();
			nonDeuce()
			checkDeuce()
			checkSet()
			printFunction(x,Tennis.striker,Tennis.i)
		else:
			if x=="Serve":
				Tennis.count+=1
				Tennis.striker=Tennis.server
			if x=="Backhand" or x=="Forehand":
			   Tennis.count+=1
			   Tennis.striker=2
			if x=="Fault":
				fault();
			if x=="Nets" or x=="PointLost-Out" or x=="PointLost-SameSide": 
				player2.point()
				Tennis.striker=1
				Tennis.count=Tennis.server
			if x=="PointLost-CouldNotReach":
				player1.point()
				Tennis.striker=2
			if x=="Ace":
				ace();
			nonDeuce()
			checkDeuce()
			checkSet()
			printFunction(x,Tennis.striker,Tennis.i)
		maintainServe()
		Tennis.i+=1
if player1.setCount>player2.setCount:
	print "Finally! Player 1 wins: (with these number of inputs)"
if player2.setCount>player1.setCount:
	print "Finally! Player 2 wins: (with these number of inputs)"
if player1.setCount==player2.setCount:
	if player1.gameCount>player2.gameCount:
		print "Finally! Player 1 wins: (with these number of inputs)"
	if player1.gameCount<player2.gameCount:
		print "Finally! Player 2 wins: (with these number of inputs)"
