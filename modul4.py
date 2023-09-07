import random
while True:
    try:
        x=float(input("hur lång är du i meter?: "))
        break
    except:
        print("skriv tal")
        continue

if(x<1.4):
    print("Du är för kort du får inte komma in")
else:
    print("Välkommen in!")


while True:
    x1=str(input("vad heter du?: "))
    if x1.isdigit(): #kollar om det inte är bokstäver
        print("skriv namn")
        continue
    else:
        print("hej " + x1+ " välkomen till parken")
        break


while True:
    r=input("Skriv radie på cirkeln?: ")
    if not r.isdigit(): #kollar om det inte är ett nummer
        print("skriv en riktig siffra")
        continue
    else:
        print("cirkelns radie är" , (int(r)**2)*3.14)
        break

while True:
    xy=input("Skriv din vikgt i kg: ")
    if not xy.isdigit():
        print("skriv en riktig siffra")
        continue
    else:
        print("Du har " , int(xy)//(x**2) , "BMI")
        break
while True:
    try:
        nummer1=int(input("skriv ett nummer: "))
        op=str(input("skriv räkne sätt: "))
        nummer2=int(input("skriv ett till nummer: "))
    except:
        print("skriv rätt")
        continue
        
    if op == "+":                             #kollar om de skrev ett räknesätt
        print(int(nummer1) + int(nummer2))
        break
    elif op == "-":
        print(int(nummer1) - int(nummer2))
        break
    elif op == "/":
        print(int(nummer1) / int(nummer2))
        break
    elif op == "*":
        print(int(nummer1) * int(nummer2))
        break
    else:
        print("försök igen")  #om inte får de skriva om 
        continue

while True:
    try:
        die=int(input("Hur många gånger vill du slå tärning?: "))   
        break 
    except: 
        print("skriv tal")
        continue

for i in range(0, die):
    print(random.randint(1,6))
         