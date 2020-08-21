from tkinter import *
from PIL import ImageTk, Image
from fetch_data import parse, get_image
from io import BytesIO

root = Tk()

# title
title = Label(root, text='GitHub User Finder!')
title.grid(row=0, column=0, columnspan=2)

user_label = Label(root, text='Enter username')
user_label.grid(row=1, column=0)

# entry for username
user_e = Entry(root)
user_e.grid(row=2, column=0)

def display_user():
	username = user_e.get()
	data = parse(username)
	if data != -1:
		i = 3
		for (key, value) in data.items():
			if key == 'avatar_url':
				image = get_image(value)
				image = Image.open(image)
				image = image.resize((120, 120))

				img = ImageTk.PhotoImage(image)
				panel = Label(root, image=img)
				panel.image = img
				panel.grid(row=i, column=0)
			else:
				# formatting string:
				key_2_label = key.split('_')
				key_2_label = [word.capitalize() for word in key_2_label]
				key_2_label = ' '.join(key_2_label)

				Label(root, text=key_2_label).grid(row=i, column=0)
				l = Label(root, text=value, width=30)
				l.grid(row=i, column=1)
			i += 1


# submit button
btn = Button(root, text='search', command=display_user)
btn.grid(row=2, column=1)


root.mainloop()
