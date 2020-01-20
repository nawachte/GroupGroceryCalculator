def main():
    trip_total = float(input("What was your trip total? "))
    tax = float(input("what was the cost of tax? "))
    calc_total = 0
    costPerPerson = {}
    items_and_their_cost_per_person = {}
    items_each_person_bought = {}
    numPeople = input("How many people? ")
    numPeople = int(numPeople)
    names = [None for x in range(numPeople)]
    # get list of people
    for i in range(numPeople):
        names[i] = input("Person "+str(i+1)+": ")
        costPerPerson[names[i]] = 0
        items_each_person_bought[names[i]] = []
    # numGroceries = int(input("How many grocery items? "))
    numGroceries = 0
    groceries = {}
    # get each item and their cost
    # for i in range(numGroceries):
    #     item = input("Item "+str(i+1)+": ")
    #     cost = float(input("Cost of "+item+": "))
    #     groceries[item] = cost
    item = ""
    print("Enter items and their total. When done enter \"done\"")
    while item!="done":
        numGroceries+=1
        item = input("Item "+str(numGroceries)+": ")
        if item != "done":
            cost = float(input("Cost of "+item+": $"))
            groceries[item] = cost
    print("")
    print("For each item presented, enter the names for that item")
    print("when youre done, enter \"done\"")
    print("To remove a name type \"del\" followed by that persons name")
    for item in groceries.keys():
        print("")
        print("Enter names for who is buying: "+item)
        # place maker for entered name
        name = ""
        # total number of people for the item
        totalPeople = 0
        # list of people buying the item
        people = []
        delFlag = False
        while name != "done":
            if totalPeople >= numPeople and delFlag == False:
                ifdone = input("Are all people buy this item[y/n]? ")
                while ifdone!='y' and ifdone!= 'no':
                    print("enter \"y\" or \"n\"")
                    ifdone = input("Are all people buy this item[y/n]? ")
                if ifdone == "y":
                    name = "done"
                else:
                    delFlag = True
            else:
                if delFlag == False:
                    name = input("Enter name: ")
                else:
                    delFlag = False
                    name = "del "+input("Who would you like to delete? ")
                if name not in names and name!= "done" and name.split()[0]!= "del":
                    print("That is not one of the names")
                    print("Please enter a name or enter \"done\"")
                elif name.split()[0] == "del":
                    delname = name.strip("del ")
                    if delname in names:
                        people.remove(delname)
                        print(delname+" has been removed")
                        totalPeople-=1
                    else:
                        print(delname+" is not a valid name")
                        print("The intended person has NOT been removed")
                else:
                    if name!="done":

                        people.append(name)
                        totalPeople+=1
        # what it costs for each person to buy the item
        if totalPeople!=0:
            itemCostPerPerson = groceries[item]/totalPeople
        else:
            itemCostPerPerson = 0
        items_and_their_cost_per_person[item] = itemCostPerPerson
        for person in people:
            costPerPerson[person] += itemCostPerPerson
            items_each_person_bought[person].append(item)
    for item in groceries.keys():
        calc_total+=groceries[item]
    for person in names:
        temp_total = costPerPerson[person]
        costPerPerson[person] += tax*(temp_total/calc_total)
        print("")
        print("")
        print(person+" bought:")
        for item in items_each_person_bought[person]:
            print(item+": $"+str(round(items_and_their_cost_per_person[item],2)))
        print("-----------------")
        print("Tax contribution: $"+str(round(tax*(temp_total/calc_total),2)))
        print(person+"\'s total is: "+str(round(costPerPerson[person],2)))
        print("")
    paid_total = 0
    for person in costPerPerson.keys():
        paid_total += costPerPerson[person]
    print("Calculated total: $"+str(round(calc_total,2)))
    if paid_total>(trip_total+.5):
        print("Your paid total appears to be $"+str(paid_total-trip_total)+"above the actual total.")
    elif paid_total<(trip_total-.5):
        print("Your paid total appears to be $"+str(trip_total-paid_total)+"below the actual total.")
    else:
        print("Your paid and trip total have been calculated as accurate.")



main()
