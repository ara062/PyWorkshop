from sys import exit

def start():

	choice = input("There is a door to your right and left. Wich one do you take?")

	if choice == "left":
		bank_room()
	elif choice == "right":
		bear_room()
	else:
		dead("You stumble around the room until you starve.")

def bank_room():
	choice = input("This room is full of money. How many bank note bundles do you take?")

	if choice.isdigit():
		if int(choice) > 0 and int(choice) < 50:
			print("Nice, you're not greedy, you win!")
			exit(0)
		elif int(choice) > 50:
			dead("Yu gready bastard!")

	else:
		dead("Man, learn to type a numer.")

def bear_room():
	print("There is 3 box.")
	print("red box")
	print("blue box")
	print("black box")
	black_box = False

	while True:
		choice = input(">")

		if choice == "red box":
			print("You hava a car")
			exit()
		elif choice == "blue box":
			print("You have a house")
			exit()
		else:
			print("You are dead")
			exit()

def dead(why):
	print(why, "You are dead.")
	exit(0)

start()