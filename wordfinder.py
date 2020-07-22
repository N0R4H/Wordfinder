
from tkinter import*
import tkinter as tk

root = tk.Tk()
root.title("Wordfinder")
root.geometry("300x300")

from itertools import permutations as perm
import enchant
def string():
      a = word.get()
      if a.isalpha() == False or  len(a)>7 or len(a)==1:
          l.config(text = 'thread panic')
      else:
         d=enchant.Dict("en_US")
         perms=set([''.join(p) for p in perm(a)])
         z =[]
         for x in perms:
                 if d.check(x)==True :
                     z.append(x)
         if not z:
              l.config(text = 'oops no words')
         else:
              l.config(text = 'The words is/are '+','.join(z))

word = StringVar() #string variable

#labels,buttons and entries
entry = Entry(root ,textvariable = word )
button1 = Button(root,text = 'Find',command = string)
button2 = Button(root,text = 'quit',command = root.destroy)
l = Label(root)

for i in (entry,button1,button2,l):
     i.pack()

root.mainloop()
print("Thank you for playing")
