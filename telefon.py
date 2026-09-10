#test
telefonbok = []

person1 = {"navn": "Nora", "nummer": "41326696"}

person2 = {"navn": "Edvin", "nummer": "46403456"}

telefonbok.append(person1)
telefonbok.append(person2)

print("Hei, dette er telefonboka:")
print(telefonbok)

def vis_alle():
    for person in telefonbok:
        print(f"{person["navn"]}: {person["nummer"]}")

vis_alle()