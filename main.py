from tkinter import *
from gui import Home

def main():
	root = Tk()
	root.title('GitHub Finder')
	root.iconphoto(False, PhotoImage(file="github.png"))

	view = Home(root)


	root.mainloop()

if __name__ == '__main__':
	main()