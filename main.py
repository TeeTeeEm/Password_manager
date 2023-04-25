from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generator():
    password_enter.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    password_list += [choice(numbers) for sym in range(randint(2, 4))]

    shuffle(password_list)

    new_password = ''.join(password_list)
    password_enter.insert(0, new_password)
    pyperclip.copy(new_password)





# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_in_txt():
    website = website_enter.get()
    login = login_enter.get()
    password = password_enter.get()
    if website == "" or login == "" or password == "":
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty")
    else:
        yes = messagebox.askyesno(title=website, message=f"Your login is {login} and passwords is {password}")
        if yes:
            with open("Passwords.txt", "a") as file:
                file.write(
                    f"{website} | {login} | {password}\n")
            website_enter.delete(0, END)
            login_enter.delete(0, END)
            password_enter.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)
canvas = Canvas(width=200, height=200)

image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)
login = Label(text="Email/Username: ", )
login.grid(row=2, column=0)
password = Label(text="Password: ")
password.grid(row=3, column=0)

website_enter = Entry(width=39)
website_enter.grid(row=1, column=1, columnspan=2)
website_enter.focus()
login_enter = Entry(width=39)
login_enter.grid(row=2, column=1, columnspan=2)
login_enter.focus()
password_enter = Entry(width=21)
password_enter.grid(row=3, column=1)
password_enter.focus()
generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(row=3, column=2)
save_button = Button(text="Add", width=34, command=add_in_txt)
save_button.grid(row=4, column=1, columnspan=2)

# def generate():

window.mainloop()
