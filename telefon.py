#test
#opg 5 tror jeg idk

telefonbok = []
person1 = {"navn": "Nora", "nummer": "41326696"}
person2 = {"navn": "Edvin", "nummer": "46403456"}

telefonbok.append(person1)
telefonbok.append(person2)

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


# ---- #meny# ---- #

while True:
    print("(--- Telefonbok ---)")
    print("1. Vis liste")
    print("2. Legg til i liste")
    print("3. Søk")
    print("4. Exit")
    print("(---(          )---)")

    valg = input("Hva vil du gjøre? (Tall eller navn)").lower()

    if valg == "1" or valg == "vis" or valg =="vis liste":
        vis_alle()

    elif valg == "2" or valg == "legg til" or valg == "Legg til i liste":
        legg_til()

    elif valg == "3" or valg == "søk":
        search()

    elif valg == "4" or valg == "exit":
        print("Avslutter, ha en fin dag!")
        break

    # ----- # ----- #
