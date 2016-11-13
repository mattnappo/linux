from tkinter import *
from tkinter.filedialog import *
filename = None
def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)
def saveFile():
	global filename
	t = text.get(0.0, END)
	with open(filename, "w") as f:
		w.write(t)
def saveAs():
	f = asksaveasfile(mode="w", defaultextension=".py")
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(title="Oops!", message="Unable to save file.")
def openFile():
	f = askopenfile(mode="r")
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)
root = Tk()
root.title("Stealth Python Editor.")
root.minsize(width=550, height=550)
root.maxsize(width=550, height=550)
text = Text(root, width=550, height=550)
text.pack()
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.mainloop()