from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
window=Tk()
window.title('Password Manager')

window.config(padx=50,pady=50)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    auto_generated=generate_password()
    print(auto_generated)
    password_entry.insert(0,auto_generated)
    pyperclip.copy(auto_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    print(f"searching for {website}")
    try:
        with open('data.json', 'r') as data_file:
        # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.askokcancel(title='Oops', message="No data file found!")
    else:
        if website in data:
            messagebox.askokcancel(title='Result',
                                   message=f"Your username is : {data[website]['email']} and password is : {data[website]['password']}!")
        else:
            messagebox.askokcancel(title='Oops', message=f"Record not Available for {website}!")


def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{"email":email,
                       "password":password}}
    if len(password)==0 or len(website)==0:
        messagebox.askokcancel(title='Oops', message="Please don't leave any field Empty!")
    else:
        # is_ok=messagebox.askokcancel(title=website , message=f'These are the details: \nEmail: {email}\nPasswordL{password}\n Is it ok ?')
        #if is_ok:
        try:
            with open('data.json','r') as data_file:
                #Reading old data
                data=json.load(data_file)
                #updating the data

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo_img)
#timer_text=canvas.create_text(220,250,text="My Pass",fill=GREEN,font=(FONT_NAME,24,'bold'))
canvas.grid(column=1,row=0)

#Labels
website_label=Label(text='Website:')
website_label.grid(column=0,row=1)
email_label=Label(text='Email/Username:')
email_label.grid(column=0,row=2)
password_label=Label(text='Password:')
password_label.grid(column=0,row=3)

#Entries
website_entry=Entry(width=35)
website_entry.focus()
website_entry.grid(column=1,row=1)
email_entry=Entry(width=35)
email_entry.insert(0,'faranpeerzada253@gmail.com')
email_entry.grid(column=1,row=2, columnspan=2)
password_entry=Entry(width=21)
password_entry.grid(column=1,row=3)

#Getting Values

#Buttons
generate=Button(text='Generate Password',width=17, command=generate)
generate.grid(column=2,row=3)
generate=Button(text='Add',width=36, command=save_password)
generate.grid(column=2,row=4, columnspan=2)
#Search button
generate=Button(text='Search',width=17, command=search)
generate.grid(column=2,row=1)
window.mainloop()