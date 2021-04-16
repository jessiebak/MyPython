
def DisplayName(_name):
	print(f"Votre nom est {_name}")
def DisplayFirstName(_firstname):
	print(f"Votre nom est {_firstname}")

def DisplayFullName(_name,_firstname):
	print(f"Vous vous appelez {_firstname} {_name}") if _name != "Bakashika" and _firstname !="Jessie" else print(f"Bonjour votre majesté {_firstname} {_name} ")

name = input("Quel est ton nom de famille? \t")
firstname = input("Quel est ton prénom? \t")

DisplayName(name)
DisplayFirstName(firstname)
DisplayFullName(name, firstname)