checklist = []
 
def create(item):
    checklist.append(item)
    return "Added {} to checklist".format(item)
def read(index):
    print(checklist[index])
    return checklist[index]
def update(index, item):
    old = checklist[index]
    checklist[index] = item
    return "Changed {} to {}".format(old, item)
def destroy(index):
    removed = checklist[index]
    checklist.pop(index)
    return "Removed {} from checklist".format(removed)

#see all items
def all_items():
    items  = []
    for element in checklist:
        print(element)
        items.append(element)

#add check mark to items
def checked():
    index=0
    for all_items in checklist:
        print('√' + " " + all_items)
        index += 1

#user input function
def user_input(prompt):
    entry = input(prompt)
    return entry

def user_choice():

    #initialize variable for while loop
    editing = True

    while editing:

        choice = input("What function you would like to use? Enter C for create, R for read, U for update, and D for destroy, A to view all items currently in the checklist, and S to select an item with a checkmark. ")
        
        if choice == "C" or choice == "c":
            item = input("What item do you want to creat? ")
            create(item)
            print(checklist)

            continue

        elif choice == "R" or choice == "r":
            index = input("What index do you want to read? ")
            read(int(index))

            continue

        elif choice == "U" or choice == "u":
            update_index = input("What index do you want to update? ")
            new_item = input("What item do you want to update? ")
            update(int(update_index), new_item)

            continue

        elif choice == "D" or choice == "d": 
            delete_index = input("What index do you want to delete? ")
            destroy(int(delete_index))

            continue
        elif choice == "A" or choice == "a":
            all_items()

            continue

        elif choice == "S" or choice == "s":
            checked_index = input("What index do you want to check off? ")
            checked(int(checked_index))

            continue

        else:
            end = input("Do you wish to quit? Enter Y for yes or N for no. ")

            if end == "Y" or end == "y":
                print(checklist)
                editing = False

            else:
                continue
            

def test():
    #create("purple sox")
    #create("red cloak")

    #print(read(0))
    #print(read(1))

    #update(0, "purple socks")
    #destroy(1)

    #print(read(0))
    #print(read(1))
    #print(all_items())
    #checked()
    #print(user_input("Is this working? "))
    user_choice()
user_choice()


