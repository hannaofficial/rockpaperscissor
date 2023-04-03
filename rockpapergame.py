import random
from pyfiglet import figlet_format as ff
from termcolor import colored
point1 = 0
point2 = 0
round1 = 1
print("\n")
print(colored("                                           Let's play                                   ",attrs=(["bold"])))
print(colored(ff("Rock...  Paper... Scissor...",width=200),color='green',attrs=(["blink"])))
print("")
print(colored("Game Rule:",color='red'))
print("Whoever between you & computer first reached 5 point Win the game")
print("")
print("Are you ready y/n")
choice = input("").lower()
if choice =='y' or choice=='yes':
	print("Let's start ")
	print("")
	print(colored("                                          Write Rock Paper Scissor to Play",color='green'))
	print("")



if choice=="y" or choice =="yes":

	while True:
		print(colored(f"Round {round1}",color='light_blue',attrs=(["bold"])))
		print("")
		symbol = ('rock','paper','scissor')
		computer = random.choice(symbol)
		user = input("Choose Rock Paper Scissor: ").lower()
		if user not in ["rock","paper","scissor"]:
			print("Invalid Input")
			continue
		

		if user==computer:
			print("Draw")
		elif (user == "scissor") and computer=="paper":
		    
		    point1+=1
		elif user=="paper" and computer=="rock":
		    
		    point1+=1    
		elif user=="rock" and computer=="scissor":
		    
		    point1+=1        
		else:
		  
		   point2+=1  
		print(f"computer choose: {computer}") 
		print("")
		print("User point:",colored(f"{point1}",color='green'),  "Computer point: "  ,colored(f"{point2}",color='red'))
		round1+=1 
		print("")
		if point1==5 or point2==5 :

		   break
			   
	if point1==5:
	   print("You win\nHurray")
	else:
	   print("You lose\nTry again")   
elif choice=="no" or choice=="n":
     print("Bye Have a good day")	   	      	