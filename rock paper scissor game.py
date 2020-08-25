import random 
lis = ["rock","paper","scissor"]
win = ("you win")
losse = ("you loose")
win_n=0
com_s =0
print("welcome to rock paper scissor game")

for i in range(10):
	random.shuffle(lis)
	com = random.choice(lis)		
	user = input("enter your choice:  ")
	print("com choice is",com,"and your choice is",user)

	if user == "paper" and com == "scissor":
		print(losse)
		com_s = com_s+1

	elif user == "scissor" and com == "paper":
		print(win)
		win_n = win_n+1


	elif user =="scissor" and com == "rock":
		print(losse)
		com_s = com_s+1


	elif user == "rock" and com  == "scissor":
		print(win)
		win_n = win_n+1

	elif user == "paper" and com == "rock":
		print(win)
		win_n = win_n+1

	elif user == "rock" and com == "paper":
		print(losse)
		com_s = com_s+1


	elif user == com:
		print("draw")

	else:
		print("please enter correct choice")
		

if win_n > com_s:
	print(f"your score is {win_n}")
	print(f"com score is {com_s}")
	print("you are the winner of the game")
elif win_n == com_s:
	print(f"your score is {win_n}")
	print(f"com score is {com_s}")
	print("the game was draw")
else :
	print(f"your score is {win_n}")
	print(f"com score is {com_s}")
	print("you loose the game")
i = input()