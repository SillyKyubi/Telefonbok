#test
telefonbok = []

person1 = {"navn": "Nora", "nummer": "41326696"}

person2 = {"navn": "Edvin", "nummer": "46403456"}

telefonbok.append(person1)
telefonbok.append(person2)

print("Hei, dette er telefonboka:")
print(telefonbok)

def legg_til():
    navn = input("Hva er navnet til personen?")
    nummer = input("Hva er nummeret deres?")

    ny_venn = {"navn": navn, "nummer": nummer}
    telefonbok.append(ny_venn)
    print(f"{navn} ble lagt til i telefonboka!")

#steg 2
def vis_alle():
    for person in telefonbok:
        print(f"{person["navn"]}: {person["nummer"]}")

#steg 3
def search():
    search_navn = input("Skriv inn et navn som du leter etter: ")
    er_der = False

    for person in telefonbok:
        if person["navn"].lower() == search_navn.lower():
            print(f"her er: {person["navn"]}: {person["nummer"]}")
            er_der = True
    
    if not er_der:
        print("Det er ingen i telefonboken med det navnet.")




legg_til()
vis_alle()
search()