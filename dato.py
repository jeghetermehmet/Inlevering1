dag = int(input("Skriv måneds dag: "))
måned =int(input("Skriv måned: "))
dag1 = int(input("Skriv måneds dag: "))
måned1 =int(input("Skriv måned: "))

if måned1 > måned:
    print("Riktig Rekkefølge")
elif måned > måned1:
    print("Feil Rekkefølge")
elif måned == måned1 and dag < dag1:
    print("Riktig Rekkefølge")
elif måned1 == måned and dag1 < dag:
    print("Feil Rekkefølge")
else:
    print("Samme dato") 