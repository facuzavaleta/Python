def likes(*args):
    nameList=[]
    for arg in args:
        nameList.append(arg)
    if len(nameList) == 0:
        print ("No ones like this.")
    elif len(nameList) == 1:
        print (nameList[0], "like this")
    elif len(nameList) == 2:
        print (nameList[0], "and", nameList[1], "like this.")
    elif len(nameList) == 3:
        print (nameList[0], ", ",nameList[1], " and ", nameList[2], " like this.", sep="")
    elif len(nameList) > 3:
        print (nameList[0], ", ", nameList[1], " and ", len(nameList) - 2, " others like this.", sep="")

likes("Facundo", "Lucca", "Maru")
