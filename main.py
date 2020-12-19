import tkinter as tk
import hashlib
from tkinter import messagebox
# import sqlite3

HEIGHT = 480
WIDTH = 360

password = ''
password_hash = ''

#Number buttons functionality
def enterNum(n):
	global password
	password += str(n)
	label['text'] += "*"
	if len(label['text']) >= 6:
		button_1['state'] = 'disabled'
		button_2['state'] = 'disabled'
		button_3['state'] = 'disabled'
		button_4['state'] = 'disabled'
		button_5['state'] = 'disabled'
		button_6['state'] = 'disabled'
		button_7['state'] = 'disabled'
		button_8['state'] = 'disabled'
		button_9['state'] = 'disabled'
		button_0['state'] = 'disabled'
	else:
		button_1['state'] = 'normal'
		button_2['state'] = 'normal'
		button_3['state'] = 'normal'
		button_4['state'] = 'normal'
		button_5['state'] = 'normal'
		button_6['state'] = 'normal'
		button_7['state'] = 'normal'
		button_8['state'] = 'normal'
		button_9['state'] = 'normal'
		button_0['state'] = 'normal'

#Password saving
def save_pass(password):
	with open('safe.txt', 'r') as file:
		if file.read() == '':
			with open('safe.txt', 'w') as file_write:
				file_write.write(str(password))
				messagebox.showinfo('Info', 'Password Saved')
		else:
			pass
# Login function to let user enter
def login(password):
	with open('safe.txt', 'r') as file:
		if file.readline() == str(password):
			messagebox.showinfo('Info', 'Authorized')
		else:
			messagebox.showerror('Error', 'Wrong password')

#Clear button
def clear():
	label['text'] = ''
	if len(label['text']) == 0:
		button_1['state'] = 'normal'
		button_2['state'] = 'normal'
		button_3['state'] = 'normal'
		button_4['state'] = 'normal'
		button_5['state'] = 'normal'
		button_6['state'] = 'normal'
		button_7['state'] = 'normal'
		button_8['state'] = 'normal'
		button_9['state'] = 'normal'
		button_0['state'] = 'normal'
# Enter button
def enter():
	global password
	global password_hash
	#Password hash
	password_hash = hashlib.sha1()
	password_hash.update(password.encode('utf-8'))
	pass_hash = password_hash.hexdigest()
	#Inserting into txt
	if len(label['text']) < 4:
		messagebox.showerror('Error', 'Password must be 4 characters or more')
	else:
		save_pass(pass_hash)
		login(pass_hash)
	#Clear label with password
	password = ''
	clear()

# VISUAL PART OF THE PROGRAM
root = tk.Tk()
root.title('Code lock')
root.geometry("360x480")
root.resizable(False, False)
root.iconbitmap('lock.ico')

canvas = tk.Canvas(root, bg="#000000")
canvas.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bd=5, bg='#FFFFFF')
frame.place(relx=0.5,rely=0.05,relwidth=0.8,relheight=0.16,anchor='n')

label = tk.Label(frame, bd=20, bg='#000000', font=('Arial', 50), justify='right', text='', anchor="e", fg="#FFFFFF")
label.place(relwidth=1,relheight=1)

lower_frame = tk.Frame(root, bg='#FFFFFF')
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.8,relheight=0.7,anchor='n')

inside_frame = tk.Frame(lower_frame, bg='#000000')
inside_frame.place(relwidth=0.96,relheight=0.96, relx=0.02,rely=0.02)

button_7 = tk.Button(lower_frame, bd=1, text='7',font=('Arial', 12), command= lambda: enterNum(7))
button_7.place(relx=0.1,rely=0.05,relheight=0.15, relwidth=0.2)

button_8 = tk.Button(lower_frame, bd=1, text='8',font=('Arial', 12),command= lambda: enterNum(8))
button_8.place(relx=0.4,rely=0.05,relheight=0.15, relwidth=0.2)

button_9 = tk.Button(lower_frame, bd=1, text='9',font=('Arial', 12), command= lambda: enterNum(9))
button_9.place(relx=0.7,rely=0.05,relheight=0.15, relwidth=0.2)

button_4 = tk.Button(lower_frame, bd=1, text='4',font=('Arial', 12), command= lambda: enterNum(4))
button_4.place(relx=0.1,rely=0.3,relheight=0.15, relwidth=0.2)

button_5 = tk.Button(lower_frame, bd=1, text='5',font=('Arial', 12), command= lambda: enterNum(5))
button_5.place(relx=0.4,rely=0.3,relheight=0.15, relwidth=0.2)

button_6 = tk.Button(lower_frame, bd=1, text='6',font=('Arial', 12), command= lambda: enterNum(6))
button_6.place(relx=0.7,rely=0.3,relheight=0.15, relwidth=0.2)

button_1 = tk.Button(lower_frame, bd=1, text='1',font=('Arial', 12), command= lambda: enterNum(1))
button_1.place(relx=0.1,rely=0.55,relheight=0.15, relwidth=0.2)

button_2 = tk.Button(lower_frame, bd=1, text='2',font=('Arial', 12), command= lambda: enterNum(2))
button_2.place(relx=0.4,rely=0.55,relheight=0.15, relwidth=0.2)

button_3 = tk.Button(lower_frame, bd=1, text='3',font=('Arial', 12), command= lambda: enterNum(3))
button_3.place(relx=0.7,rely=0.55,relheight=0.15, relwidth=0.2)

button_0 = tk.Button(lower_frame, bd=1, text='0',font=('Arial', 12), command= lambda: enterNum(0))
button_0.place(relx=0.1,rely=0.8,relheight=0.15, relwidth=0.2)

button_clear = tk.Button(lower_frame, bd=1, text='Clear',font=('Arial', 12), command=clear)
button_clear.place(relx=0.4,rely=0.8,relheight=0.15, relwidth=0.2)

button_enter = tk.Button(lower_frame, bd=1, text='Enter',font=('Arial', 12), command=enter)
button_enter.place(relx=0.7,rely=0.8,relheight=0.15, relwidth=0.2)


root.mainloop()
