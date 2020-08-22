from tkinter import *
from PIL import ImageTk, Image
from fetch_data import get_user, get_image, get_repos
from io import BytesIO

root = Tk()
root.title('GitHub Finder')

def show_repo(user):
	repos = get_repos(user)
	j = 10
	# table heading:
	Label(root, text='Name').grid(row=j, column=0)
	Label(root, text='Watchers').grid(row=j, column=1)
	Label(root, text='Forks').grid(row=j, column=2)
	j += 1
	# repo data
	for repo in repos:
		Label(root, text=repo.get("name")).grid(row=j, column=0)
		Label(root, text=repo.get("watchers")).grid(row=j, column=1)
		Label(root, text=repo.get("forks")).grid(row=j, column=2)
		j += 1
	


def display_user():
	username = user_e.get()
	data = get_user(username)
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
		Button(root, text='Show Repos', command=lambda: show_repo(username)).grid(row=i, column=0)


# title
title = Label(root, text='GitHub User Finder!')
title.grid(row=0, column=0, columnspan=3)

user_label = Label(root, text='Enter username')
user_label.grid(row=1, column=0)

# entry for username
user_e = Entry(root, width=50, borderwidth=3)
user_e.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipady=5)
# submit button
btn = Button(root, text='Search', width=30, padx=20, pady=5, fg='#ffffff', bg='#5ca9d6', command=display_user)
btn.grid(row=2, column=1, columnspan=2)

root.mainloop()
