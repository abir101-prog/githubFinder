from tkinter import *
from PIL import ImageTk, Image
from fetch_data import get_user, get_image, get_repos
from io import BytesIO

root = Tk()
root.title('GitHub Finder')
root.iconphoto(False, PhotoImage(file="github.png"))



def show_repo(user):
	repos = get_repos(user)
	j = 0
	if len(repos) == 0:
		Label(repo_group, text='No Repository found', bg='#f54049', fg='#ffffff', width=30).grid(row=0, column=0, columnspan=3)
	else:
		# table heading:
		Label(repo_group, text='Name').grid(row=j, column=0)
		Label(repo_group, text='Watchers').grid(row=j, column=1)
		Label(repo_group, text='Forks').grid(row=j, column=2)
	j += 1
	# repo data
	for repo in repos:
		Label(repo_group, text=repo.get("name")).grid(row=j, column=0)
		Label(repo_group, text=repo.get("watchers")).grid(row=j, column=1)
		Label(repo_group, text=repo.get("forks")).grid(row=j, column=2)
		j += 1
	repo_group.grid(row=4, column=0, columnspan=3, pady=10)

def display_user():
	# get the username
	username = user_e.get()
	data = get_user(username)  # fetch data through api
	if data != -1:   # if data is returned
		children_u = user_group.grid_slaves()   
		for child in children_u:
			child.destroy()   # removing everything from user LabelFrame
		i = 0
		for (key, value) in data.items():
			if key == 'avatar_url':
				image = get_image(value)
				image = Image.open(image)
				image = image.resize((120, 120))

				img = ImageTk.PhotoImage(image)
				panel = Label(user_group, image=img)
				panel.image = img
				panel.grid(row=i, column=0)
			else:
				# formatting string:
				key_2_label = key.split('_')
				key_2_label = [word.capitalize() for word in key_2_label]
				key_2_label = ' '.join(key_2_label)

				Label(user_group, text=key_2_label).grid(row=i, column=0)
				l = Label(user_group, text=value, width=30)
				l.grid(row=i, column=1)
			i += 1
		user_group.grid(row=3, column=0, columnspan=3, pady=10)
		Button(user_group, text='Show Repos', width=30, padx=20, pady=5,
		 fg='#ffffff', bg='#5ca9d6', command=lambda: show_repo(username)).grid(row=i, column=0, columnspan=2)
		
		children_r = repo_group.grid_slaves()
		for child in children_r:
			child.destroy()   # removing everything from repo LabelFrame
		repo_group.grid_forget()
		
		
		

# title
title = Label(root, text='GitHub User Finder!')
title.grid(row=0, column=0, columnspan=3)

user_label = Label(root, text='Enter username')
user_label.grid(row=1, column=0)

# entry for username
user_e = Entry(root, width=50, borderwidth=3)
user_e.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipady=5)
# submit button
search_btn = Button(root, text='Search', width=30, padx=20, pady=5, fg='#ffffff', bg='#5ca9d6', command=display_user)
search_btn.grid(row=2, column=1, columnspan=2, pady=5)

# these 2 will be displayed after they get their childs
user_group = LabelFrame(root, padx=20, pady=5)

repo_group = LabelFrame(root, padx=20, pady=5)

root.mainloop()
