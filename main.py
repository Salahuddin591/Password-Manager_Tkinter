import json
from bisect import insort
from cProfile import label
from gettext import textdomain
from tkinter import  *
from tkinter import Entry
from tkinter import messagebox
import random
from numpy.ma.extras import row_stack
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbol + password_number
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if len(website) ==0 or password ==0 :
        messagebox.showinfo(title="OOps", message="Please make sure you havent left any fileds Empty, ")
    else:
        try:
             with open("data.json", "r") as data_file:
                    data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
             data.update(new_data)
             with open("data.json","w") as data_file:
                 json.dump(data,data_file,indent=4)
        finally:
             website_entry.delete(0, END)
             password_entry.delete(0,END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data FIle Found")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email:{email}/n Password:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No Details for {website}exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image =logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2 , column=0)

passowrd_label = Label(text="Password:")
passowrd_label.grid(row=3 , column=0)



#entries

website_entry = Entry(width=21)
website_entry.grid(row =1 ,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0, "mdsalah@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

 #buttons
search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3,column=2)

add_button = Button(text="Add" , width=36,  command= save )
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
