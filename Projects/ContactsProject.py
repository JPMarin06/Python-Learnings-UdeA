# Welcome to the ContactsProject. With this app you can add all the contacts that you want.
# All the contacts will be saved in a long list and you can do different actions with the menu options.
# The menu options includes: add, search, modify, delete a contact or get out from the app.
# Thanks for use it. I appreciate it.

# First of all, is a need to create some functions that will be used later


def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def number_positive_entire(number):
    if is_number(number):
        if int(number) >= 0 and int(number) % 1 == 0:
            return True
        else:
            return False
    else:
        return False


# The list of the contacts is created

contacts_list = {0: {"name": "SupportTeam", "email": "jpmarim06@gmail.com", "phone": 3145401702, "age": 17}}

# The welcome is given
print("Welcome to the app where you could save all the contacts that you want.\n"
      "The first contact is our line of supporting.\n")


# Now, the creation of the other functions.


def confirm(message):
    while True:
        # This one is to reconfirm an action, asking for a y or a n, simulating a yes and a no
        wish = input(message + ". If confirm, type a y, if not, type a n: ")
        if wish == "y":
            return True
        if wish == "n":
            return False
        else:
            print("Correct what you typed")


def set_contact(code, name, email, phone, age):
    # This one is to set a contacts. Then this will be used for functions like add or modify
    contacts_list[code] = {"name": name, "email": email, "phone": phone, "age": age}


# Now, the creations of the functions of the menu, using the others created before


def verify_number(number_type, contact):
    while True:
        # This one if only to see if the number typed is correct
        variable = input("Type the " + number_type + " of " + contact + ": ")
        if number_positive_entire(variable):
            break
        else:
            print("Please correct the " + number_type + " of " + contact + ": ")
    return variable


def add_contact():
    print("\n===============ADDING CONTACT===============")
    while True:
        # This one works like this. First the app see if the identifier contact already exists.
        # If exists, need to type another one, otherwise, start to add the contact.
        contact_code = input("Type a number which you can identify the contact: ")
        if number_positive_entire(contact_code):
            contact_code = int(contact_code)
            if contact_code in contacts_list:
                print("This code number already exists")
                break
            else:
                name1 = input("Type the name of your contact: ")
                email1 = input("Type the email of " + name1 + ": ")
                phone1 = verify_number("phone number", name1)
                age1 = verify_number("age", name1)
                save_all = confirm("Are you sure to the contact " + name1 + "?: ")
                if save_all:
                    set_contact(contact_code, name1, email1, phone1, age1)
                    print("¡The contact " + name1 + " was saved successfully!")
                    break
                if not save_all:
                    print("The contact " + name1 + " was not saved")
                    break

        else:
            print("Please correct the code, remember is a positive and entire number")


def search_contact():
    print("\n===============SEARCHING CONTACT===============")
    while True:
        # This one works like this. See if the identifier requested exists and then show it.
        searched = input("Type the code of the contact that you want to search: ")
        if number_positive_entire(searched):
            searched = int(searched)
            if searched in contacts_list:
                print("This is the contact that you were looking for" + '\n' +
                      "Name: " + contacts_list[searched]['name'] + '\n' +
                      "Email: " + contacts_list[searched]['email'] + '\n' +
                      "Phone number: " + str(contacts_list[searched]['phone']) + '\n' +
                      "Age: " + str(contacts_list[searched]['age']))
                break
            else:
                print("This contact does not exist")
                break
        else:
            print("Correct what you typed")


def modify_contact():
    print("\n===============MODIFYING CONTACT===============")
    while True:
        # This is like a combination of the last two functions. Search and then change the contact.
        modified = input("Type the code of the contact that you want to modify: ")
        if number_positive_entire(modified):
            modified = int(modified)
            if modified in contacts_list:
                print("This is the contact that you are going to modify" + '\n' +
                      "Name: " + contacts_list[modified]['name'] + '\n' +
                      "Email: " + contacts_list[modified]['email'] + '\n' +
                      "Phone number: " + str(contacts_list[modified]['phone']) + '\n' +
                      "Age: " + str(contacts_list[modified]['age']))
                name2 = contacts_list[modified]['name']
                name1 = input("Type the new name of the contact: ")
                email1 = input("Type the new email of " + name1 + ": ")
                phone1 = verify_number("new phone number", name1)
                age1 = verify_number("new age", name1)
                save_all = confirm("Are you sure to change the contact " + name2 + "?: ")
                if save_all:
                    set_contact(modified, name1, email1, phone1, age1)
                    print("¡The contact " + name2 + " was changed successfully!")
                    break
                if not save_all:
                    print("The contact " + name2 + " was not changed")
                    break
            else:
                print("This contact does not exist")
                break
        else:
            print("Correct what you typed")


def delete_contact():
    print("\n===============DELETING CONTACT===============")
    while True:
        # Now to delete only is confirm the decision of the user and no more.
        deleted = input("Type the code of the contact that you want to delete: ")
        if number_positive_entire(deleted):
            deleted = int(deleted)
            if deleted in contacts_list:
                print("This is the contact that you are going to delete" + '\n' +
                      "Name: " + contacts_list[deleted]['name'] + '\n' +
                      "Email: " + contacts_list[deleted]['email'] + '\n' +
                      "Phone number: " + str(contacts_list[deleted]['phone']) + '\n' +
                      "Age: " + str(contacts_list[deleted]['age']))
                name2 = contacts_list[deleted]['name']
                save_all = confirm("Are you sure to delete the contact " + name2 + "?: ")
                if save_all:
                    del contacts_list[deleted]
                    print("¡The contact " + name2 + " was deleted successfully!")
                    break
                if not save_all:
                    print("The contact " + name2 + " was not deleted")
                    break
            else:
                print("This contact does not exist")
                break
        else:
            print("Correct what you typed")


def show_contacts():
    # I wanted to make this function with the library tabulate but I was not able to :(.
    # That is why, I decided to do it only with text.
    print("\n===============SHOWING CONTACTS===============")
    for x in contacts_list.keys():
        print("Identifier:", x,
              "|", "Name:", contacts_list[x]['name'],
              "|", "Email:", contacts_list[x]['email'],
              "|", "Phone:", contacts_list[x]['phone'],
              "|", "Age:", contacts_list[x]['age'])


# The menu of options begin.
# First, the keys are mentioned.
print("These are the keys to execute an action:\n"
      "Type a 1, if you want to add a contact.\n"
      "Type a 2, if you want to search a contact.\n"
      "Type a 3, if you want to modify a contact.\n"
      "Type a 4, if you want to delete a contact.\n"
      "Type a 5, if you want to see the list of contacts.\n"
      "Type a 6, if you want to leave the app.\n")


# Then, the menu is here.


def menu():
    while True:
        desired_option = input("Type the key of the menu here: ")
        if number_positive_entire(desired_option) and 0 < int(desired_option) < 7:
            desired_option = int(desired_option)
            if desired_option == 1:
                add_contact()
            if desired_option == 2:
                search_contact()
            if desired_option == 3:
                modify_contact()
            if desired_option == 4:
                delete_contact()
            if desired_option == 5:
                show_contacts()
            if desired_option == 6:
                break
        else:
            print("The key does not exist")

# The code starts here


menu()


# I say thanks for using the code


print("¡Thanks for use the contact book! Remember the email to send doubts or troubles: jpmarim06@gmail.com")
