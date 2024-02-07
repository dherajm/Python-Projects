from tkinter import *
import tkinter.messagebox as mb
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(4, 6))]

    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)
    final_password = ''.join(password)

    password_entry.delete(0, END)
    pyperclip.copy(final_password)
    password_entry.insert(0, final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_credentials():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if not website_text or not email_text or not password_text:
        mb.showerror("Fill in all fields", "Fill in all the fields")
    else:
        is_ok = mb.askyesno(title=website_text, message=f"Credentials: \nWebsite: {website_text} \n"
                                                        f"Email: {email_text} \nPassword: {password_text} \n\nSave Credentials?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"\n{website_text} | {email_text} | {password_text}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=add_credentials)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
