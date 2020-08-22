from tkinter import *
from fetch_data import get_user, get_image, get_repos
from PIL import ImageTk, Image
from io import BytesIO

class Home:
	def __init__(self, root):
		self.root = root
		
		self.parent = Frame(root)
		self.parent.grid(row=0, column=0)   # parent will contain everything		
		
		self.form = LabelFrame(self.parent, padx=20, pady=5)
		self.form.grid(row=0, column=0, pady=10., padx=10)  # first child of parent
		self.create_form_children()
		
		self.user = LabelFrame(self.parent, padx=20, pady=5)   # second child of parent, will be seen after user is requested
		self.repos = LabelFrame(self.parent, padx=20, pady=5)  #third child of parent, will be seen after...
		

	def create_form_children(self):
		self.title = Label(self.form, text='GitHub User Finder!')
		self.title.grid(row=0, column=0, columnspan=3)
		self.user_label = Label(self.form, text='Enter username')
		self.user_label.grid(row=1, column=0)
		self.user_entry = Entry(self.form, width=50, borderwidth=3)
		self.user_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipady=5)
		self.search_btn = Button(self.form, text='Search', width=30, padx=20, 
			pady=5, fg='#ffffff', bg='#5ca9d6', command=self.display_user)
		self.search_btn.grid(row=2, column=1, columnspan=2, pady=5)


	def display_user(self):
		# get the username
		username = self.user_entry.get()
		data = get_user(username)  # fetch data through api
		if data != -1:   # if data is returned
			children_u = self.user.grid_slaves()   
			for child in children_u:
				child.destroy()   # removing everything from user LabelFrame
			i = 0
			for (key, value) in data.items():
				if key == 'avatar_url':
					image = get_image(value)
					image = Image.open(image)
					image = image.resize((150, 150))

					img = ImageTk.PhotoImage(image)
					panel = Label(self.user, image=img)
					panel.image = img
					panel.grid(row=i, column=0)
				else:
					# formatting string:
					key_2_label = key.split('_')
					key_2_label = [word.capitalize() for word in key_2_label]
					key_2_label = ' '.join(key_2_label)

					Label(self.user, text=key_2_label).grid(row=i, column=0)
					l = Label(self.user, text=value, width=30)
					l.grid(row=i, column=1)
				i += 1
			self.user.grid(row=1, column=0, pady=10)
			Button(self.user, text='Show Repositories', width=30, padx=20, pady=10,
			 fg='#ffffff', bg='#5ca9d6', command=lambda: self.show_repo(username)).grid(row=i, column=0, columnspan=2)
			
			children_r = self.repos.grid_slaves()
			for child in children_r:
				child.destroy()   # removing everything from repo LabelFrame
			self.repos.grid_forget()


	def show_repo(self, user):

		repos = get_repos(user)
		j = 0
		if len(repos) == 0:
			Label(self.repos, text='No Repository found', bg='#f54049', fg='#ffffff', width=30).grid(row=0, column=0, columnspan=3)
		else:
			# table heading:
			Label(self.repos, text='Name').grid(row=j, column=0)
			Label(self.repos, text='Watchers').grid(row=j, column=1)
			Label(self.repos, text='Forks').grid(row=j, column=2)
		j += 1
		# repo data
		for repo in repos:
			Label(self.repos, text=repo.get("name")).grid(row=j, column=0)
			Label(self.repos, text=repo.get("watchers")).grid(row=j, column=1)
			Label(self.repos, text=repo.get("forks")).grid(row=j, column=2)
			j += 1
		self.repos.grid(row=2, column=0, pady=10)