print()
print("What is your name?")

name = input(">")

print("Hello %s, welcome to the dungeon!" % (name))
print("Do you go through door 1 od door 2?")

door = input(">")

if door == "1":
	print("What is your favourite colour %s?" % (name))
	print("**white")
	print("**black")
	print("**yellow")

	colour = input("> ")

	if colour =="white":
		print("Thanks %s, you are cautious." % (name))
	elif colour =="black":
		print("Thanks %s, you are sharp." % (name))
	elif colour =="yellow":
		print("Thanks %s, you are bright." % (name))
	else:
		print("You are not so good with numbers, are you?")

elif door == "2":
	print("There is a new room with 2 doors")
	print("What do you do?")
	print("1. You take a door 1")
	print("2. You take a door 2")

	island = input(">")

	if island =="1":
		print("Congratulations, you found a island with a hotel")
	elif island =="2":
		print("Ouch, you found a desert island")
	else:
		print("You are not so good with numbers, are you?")

else:
	print("You are not so good with numbers, are you?")