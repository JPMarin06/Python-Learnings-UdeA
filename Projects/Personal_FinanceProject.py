# This is the code that you can use to manage your personal finances.
# First, we need to import the libraries that we use in the code
from tkinter import *
from datetime import datetime


# These are some default functions that I usually use


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


# These are like the main instructions to use the code correctly
instructions = "This is an app that control\n the expenses registered.\nInstructions of PerFin App:\n\n" \
               "1.First you are " \
               "going to introduce \nthe initial budget that you have. \nPay attention to your number.\n\n2.Then, " \
               "you will have a part where\n you can introduce the\n expenses like transport,\n feeding, fun, " \
               "payments or " \
               "others.\n\n3.Later, you will have a part to see\n all the payments that you\n have done of this " \
               "type.\n\n4.After " \
               "this, you will have a part\n where you can\n introduce monthly expenses \nlike your services, " \
               "mortgages.\n\n5.Later, you will have a part to see\n all the payments that you\n have done of this " \
               "type.\n\n6.Always at right top of the screen\n you have your money. If it is green, you\n do not owe " \
               "money. " \
               "If it is red, \nyou owe money or you need more.\n\n7.Finally, you have a button to\n " \
               "get out from the " \
               "app at the bottom right. "

# As in this code we need to register a list of several monthly expenses, we need to create lists and
# some variables that change constantly

records_monthly_expenses_names = []
records_monthly_expenses_prices = []
monthly_expenses_total = 0
budget = 0

# We open the tab and the put a title and dimensions
root = Tk()
root.title("Admin personal finances")
menu_bar = Menu(root)
root.geometry("1400x700")

# The Frame is created

main_frame = Frame(root, bg='#138A2E', height=1500, width=1500)
main_frame.pack()

# The title in the window and some labels to indicate the divisions clearly.

welcome = Label(main_frame, bg="#10BB49", fg="#FFFFFF", text="P  E  R  F  I  N  A  P  P", font=('Arial', 20))
welcome.place(x=10, y=10, width=1350, height=40)

division1 = Label(main_frame, bg="#000000").place(x=430, y=70, width=5, height=600)
division2 = Label(main_frame, bg="#000000").place(x=830, y=70, width=5, height=600)
division3 = Label(main_frame, bg="#000000").place(x=1230, y=70, width=5, height=600)

# This is to have in mind when te code starts to run, maybe somebody will use this, but
# is something aesthetic too.

all_date = datetime.now()
date = "Date of started code:\n" + str(all_date.year) + "-" + str(all_date.month) + "-" + str(all_date.day) + "-" + \
       str(all_date.hour) + ":" \
       + str(all_date.minute)
start_date = Label(main_frame, bg="#09D121", fg="#FFFFFF", text=date, font=('Arial', 9))
start_date.place(x=15, y=15, width=120, height=30)

# Title of the instructions

instruction0 = Label(main_frame, bg="#1060B1", fg="white", text="These are the instructions that\n explain how the app "
                                                                "works:\n" + instructions, font=('Arial', 11))
instruction0.place(x=10, y=70, width=255, height=600)

# The function to put the initial budget is created


def put_initial_budget():
    global budget
    budget = text_budget.get()
    text_budget.delete(0, END)
    if number_positive_entire(budget):
        always_budget.config(text=str(budget))
        budget = int(budget)
    if int(budget) > 0:
        always_budget.config(fg="#11792D")


enter_budget_text = "Enter this budget"
enter_budget = Button(main_frame, text=enter_budget_text, command=put_initial_budget)
enter_budget.place(x=275, y=150, width=100, height=20)

text_budget = Entry(main_frame)
text_budget.place(x=275, y=110, width=150, height=30)

instruction1 = Label(main_frame, text="Enter your initial budget \n without decimals here: ", font=('Arial', 9))
instruction1.place(x=275, y=70, width=150, height=30)

# Then, we have a function to add money to the initial budget


def add_money():
    global budget
    money = text_money.get()
    budget = budget + int(money)
    always_budget.config(text=str(budget))
    if budget > 0:
        always_budget.config(fg="#11792D")

# And the function to add all this money registered in a record.


money_records_list = Listbox(root, width=20)
name_counter5 = 0


def put_money_register():
    global name_counter5
    name_counter5 = name_counter5 + 1
    text_put = text_money.get()
    money_records_list.insert(name_counter5, str(name_counter5) + ".  + " + text_put)
    money_records_list.place(x=275, y=340)
    text_money.delete(0, END)


def add_and_register_money():
    add_money()
    put_money_register()


enter_money_text = "Enter this money"
enter_money = Button(main_frame, text=enter_money_text, command=add_and_register_money)
enter_money.place(x=275, y=270, width=100, height=20)

text_money = Entry(main_frame)
text_money.place(x=275, y=230, width=150, height=30)

# More and more instructions

instruction18 = Label(main_frame, text="The number indicates\n the number of the\n money added to the\n "
                                       "initial budget.",
                      font=('Arial', 9))
instruction18.place(x=275, y=530, width=130, height=100)

instruction13 = Label(main_frame, text="If you wanna add money\n after the initial budget\n do it here.",
                      font=('Arial', 9))
instruction13.place(x=275, y=180, width=150, height=41)

instruction13 = Label(main_frame, text="MONEY ADDED AFTER\n INITIAL BUDGET RECORD", font=('Arial', 9))
instruction13.place(x=275, y=300, width=150, height=30)

instruction2 = Label(main_frame, text="This is the space for monthly expenses", font=('Arial', 15))
instruction2.place(x=445, y=70, width=380, height=25)

instruction14 = Label(main_frame, text="These are the names of the\n monthly expenses. "
                                       "The number\n indicates the time when the\n button was pressed. "
                                       "It could\n be consider as the month\n of those expenses", font=('Arial', 8))
instruction14.place(x=445, y=550, width=160, height=100)

instruction15 = Label(main_frame, text="These are the costs of the\n monthly expenses. "
                                       "The number\n indicates the time when the\n button was pressed. "
                                       "It could\n be consider as the month\n of those expenses", font=('Arial', 8))
instruction15.place(x=630, y=550, width=160, height=100)

instruction16 = Label(main_frame, text="Remember to do it at the same time for\n the correct functioning of the code",
                      font=('Arial', 12))
instruction16.place(x=445, y=205, width=380, height=40)

# This add the name of the expenses to a list to be showed then


def put_name_monthly():
    text_put = name_monthly_expense.get()
    name_monthly_expense.delete(0, END)
    records_monthly_expenses_names.append(str(text_put))


name_monthly_expense = Entry(main_frame)
name_monthly_expense.place(x=445, y=145, width=165, height=20)

enter_name_monthly_text = "Enter"
enter_name_monthly = Button(main_frame, text=enter_name_monthly_text, command=put_name_monthly)
enter_name_monthly.place(x=445, y=175, width=50, height=20)

instruction4 = Label(main_frame, text="Introduce the name of one\n of the monthly expenses here", font=('Arial', 9))
instruction4.place(x=445, y=105, width=165, height=30)

# This add the cost of the expenses to a list to be showed then


def put_price_monthly():
    global monthly_expenses_total
    text_put = price_monthly_expense.get()
    price_monthly_expense.delete(0, END)
    records_monthly_expenses_prices.append(str(text_put))
    monthly_expenses_total += int(text_put)


price_monthly_expense = Entry(main_frame)
price_monthly_expense.place(x=620, y=145, width=165, height=20)

enter_price_monthly_text = "Enter"
enter_price_monthly = Button(main_frame, text=enter_price_monthly_text, command=put_price_monthly)
enter_price_monthly.place(x=620, y=175, width=50, height=20)

instruction5 = Label(main_frame, text="Introduce the cost of that expense\n here. Remember is a entire number",
                     font=('Arial', 9))
instruction5.place(x=620, y=105, width=200, height=30)

# This functions is designed to subtract money from the budget having the monthly expenses


def subtract_monthly_expenses_function():
    global budget
    subtracted = int(budget)
    subtracted -= int(monthly_expenses_total)
    always_budget.config(text=str(subtracted))
    budget = subtracted

    if int(budget) < 0:
        always_budget.config(fg="#E51111")

# Then we have the creation of the list boxes that later will have the records of names and prices


monthly_names_records_list = Listbox(root, width=26)
monthly_prices_records_list = Listbox(root, width=26)

name_counter = 0
name_counter2 = 0

# Then, every data digitized is add to the list boxes with an index to identify the time when the button was pressed


def put_names_records():
    global name_counter
    name_counter = name_counter + 1
    for name in range(0, int(len(records_monthly_expenses_names))):
        monthly_names_records_list.insert(name, str(name_counter) + ".  " + records_monthly_expenses_names[name])
        monthly_names_records_list.place(x=445, y=380)


def put_prices_records():
    global name_counter2
    name_counter2 = name_counter2 + 1
    for price in range(0, int(len(records_monthly_expenses_prices))):
        monthly_prices_records_list.insert(price, str(name_counter2) + ".  " +
                                           " - " + records_monthly_expenses_prices[price])
        monthly_prices_records_list.place(x=630, y=380)


def register_monthly_expenses():
    subtract_monthly_expenses_function()
    put_names_records()
    put_prices_records()


subtract_monthly_expenses_text = "Enter"
subtract_monthly_expenses = Button(main_frame, text=subtract_monthly_expenses_text,
                                   command=register_monthly_expenses).place(x=595, y=295, width=50, height=20)

instruction6 = Label(main_frame, text="This button subtracts all the typed monthly\n expenses that you have done from "
                                      "your budget. ", font=('Arial', 12))
instruction6.place(x=445, y=250, width=350, height=40)

instruction7 = Label(main_frame, text="MONTHLY EXPENSES RECORDS", font=('Arial', 13))
instruction7.place(x=445, y=330, width=350, height=40)

different_expenses_total = 0
different_names_records_list = Listbox(root, width=26)
different_prices_records_list = Listbox(root, width=26)

# Then, is the same but now with different expenses and we do not have a button that subtract all the money directly.

instruction2 = Label(main_frame, text="This is the space for different expenses", font=('Arial', 15))
instruction2.place(x=845, y=70, width=380, height=25)

name_counter3 = 0


def put_name_different():
    global name_counter3
    name_counter3 = name_counter3 + 1
    text_put = name_different_expense.get()
    name_different_expense.delete(0, END)
    different_names_records_list.insert(name_counter3, str(name_counter3) + ".  " + text_put)
    different_names_records_list.place(x=845, y=380)


name_different_expense = Entry(main_frame)
name_different_expense.place(x=845, y=145, width=165, height=20)

enter_name_different_text = "Enter"
enter_name_different = Button(main_frame, text=enter_name_different_text, command=put_name_different)
enter_name_different.place(x=845, y=175, width=50, height=20)

instruction12 = Label(main_frame, text="Introduce the name of one\n of the different expenses here", font=('Arial', 9))
instruction12.place(x=845, y=105, width=165, height=30)

name_counter4 = 0


def put_price_different():
    global different_expenses_total
    global name_counter4
    name_counter4 = name_counter4 + 1
    text_put = price_different_expense.get()
    price_different_expense.delete(0, END)
    global budget
    subtracted = int(budget)
    subtracted -= int(text_put)
    always_budget.config(text=str(subtracted))
    budget = subtracted

    different_prices_records_list.insert(name_counter4, str(name_counter4) + ".  - " + text_put)
    different_prices_records_list.place(x=1030, y=380)

    if int(budget) < 0:
        always_budget.config(fg="#E51111")


price_different_expense = Entry(main_frame)
price_different_expense.place(x=1020, y=145, width=165, height=20)

enter_price_different_text = "Enter"
enter_price_different = Button(main_frame, text=enter_price_different_text, command=put_price_different)
enter_price_different.place(x=1020, y=175, width=50, height=20)

instruction9 = Label(main_frame, text="Introduce the cost of that expense\n here. Remember is a entire number",
                     font=('Arial', 9))
instruction9.place(x=1020, y=105, width=200, height=30)

instruction17 = Label(main_frame, text="These are the names of the\n different expenses. "
                                       "The number\n indicates the number of the\n expense digitized.",
                      font=('Arial', 8))
instruction17.place(x=845, y=550, width=160, height=70)

instruction18 = Label(main_frame, text="These are the costs of the\n different expenses. "
                                       "The number\n indicates the number of the\n expense digitized.",
                      font=('Arial', 8))
instruction18.place(x=1030, y=550, width=160, height=70)

instruction19 = Label(main_frame, text="Remember when you press enter in the second button,\n that quantity of money "
                                       "is subtracted from the budget directly",
                      font=('Arial', 10))
instruction19.place(x=845, y=205, width=380, height=40)

instruction11 = Label(main_frame, text="DIFFERENT EXPENSES RECORDS", font=('Arial', 13))
instruction11.place(x=845, y=330, width=350, height=40)

# Finally, we have the Label that always shows the current budget and the button to exit from the app

always_budget = Label(main_frame, fg="#11792D", text="", font=("Arial", 8))
always_budget.place(x=1250, y=70, width=int(len(text_budget.get())) + 100, height=20)

exit_text = "Exit"
exit_button = Button(main_frame, bg="#910E0E", fg="white", text=exit_text, command=root.quit)
exit_button.place(x=1300, y=650, width=50, height=20)

# And the code is closed.

root.mainloop()
