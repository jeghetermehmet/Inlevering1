dato = int(input("Skriv første dato.Første to skal være måneds nummer mens de siste andre for dagen i måned: "))
dato1 = int(input("Skriv første dato.Første to skal være måneds nummer mens de siste andre for dagen i måned: "))



if dato1 > dato:
    print("Riktig Rekkefølge")
elif dato > dato1:
    print("Feil Rekkefølge")
else:
    print("SAmme dato")