import tkinter as tk
import re
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
 

def replacefunction():
        T2.delete("1.0", tk.END)
        check=check_entry.get() 
        paragraph=paragraph_entry.get() 
        replace=replace_entry.get() 
        final=re.sub(check, replace, paragraph)
        T2.insert(tk.END,"OUTPUT AFTER REPLACE:\n")
        if(replace==''):
            T2.insert(tk.END,"REPLACE WITH IS EMPTY")
        elif(final == paragraph):
            T2.insert(tk.END,final+"\nString is same as before replace")
            
        else:
            T2.insert(tk.END,final)
def testmatchfunction():
        T.delete("1.0", tk.END)
        check=check_entry.get() 
        paragraph=paragraph_entry.get() 
        T.insert(tk.END,paragraph)
        p = re.compile(check) 
        k=p.findall(paragraph) 
        T.insert(tk.END,"\nTHE FOLLOWING ARE THE MATCHES:\n")
        T.insert(tk.END,k)
        if(len(k)==0):
            end="1."+str(len(paragraph))
            T.tag_add("allred","1.0",end)
            T.tag_config("allred",background="red")
            T.insert(tk.END,"\nNO MATCH FOUND")
        for j in k :
            matches=re.finditer(j,paragraph)
            matchposition=[match.start() for match in matches]
            for i in matchposition :
                start="1"+"."+str(i)
                end="1."+str(i+len(check))
                T.tag_add("change",start,end)
                T.tag_config("change",background="green")
        T.insert(tk.END,"\nMATCH FOUND,HURRAY")
        T.insert(tk.END,"\nTOTAL NUMBER OF MATCHES ARE "+str(len(k)))       
def help_messagebox():
    helptext="REGEX is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for find or find and replace operations on strings"
    messagebox.showinfo("HELP",helptext)            

        
root=tk.Tk()
root.geometry("600x400") 
root.configure()
root.title("REGEX QUERY TOOL")
check_var=tk.StringVar() 
paragraph_var=tk.StringVar() 
replace_var=tk.StringVar()

helptext="REGEX is a sequence of characters that define a search pattern. Usually such patterns are used by string searching algorithms for find or find and replace operations on strings"
messagebox.showinfo("HELP",helptext)
check_label = tk.Label(root, text = 'Regular Expression:')     
check_entry = tk.Entry(root,width=42)

paragraph_label = tk.Label(root, text ='Entry to test against:')
paragraph_entry=tk.Entry(root,width=42)

replace_label = tk.Label(root, text ='Replace with(optional):')
replace_entry=tk.Entry(root,width=42)

T = tk.Text(root,width=37,height=20,borderwidth=2)
T2= tk.Text(root,width=37,height=20)

testmatch_btn=tk.Button(root,text ='TEST MATCH', command = lambda : testmatchfunction(),relief=RAISED,height=1,width=42,bg="grey")
replace1_btn=tk.Button(root,text ='REPLACE',command = lambda : replacefunction(),relief=RAISED,height=1,width=42,bg="grey")
help_btn=tk.Button(root,text ='HELP',command = lambda : help_messagebox(),relief=RAISED,height=1,width=85,bg="grey")


var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(root, text='First occurence',variable=var1, onvalue=1, offvalue=0, command = lambda : testmatchfunction())
c2 = tk.Checkbutton(root, text='All occurence',variable=var2, onvalue=1, offvalue=0, command = lambda : testmatchfunction())


help_btn.grid(row=0,column=0,sticky=W,columnspan=2)
check_label.grid(row=1,column=0) 
check_entry.grid(row=1,column=1,sticky=W) 
paragraph_label.grid(row=2,column=0) 
paragraph_entry.grid(row=2,column=1,sticky=W)
replace_label.grid(row=3,column=0) 
replace_entry.grid(row=3,column=1,sticky=W) 
testmatch_btn.grid(row=4,column=0,sticky=W)
replace1_btn.grid(row=4,column=1,sticky=W)
c1.grid(row=5,column=0,sticky=W)
c2.grid(row=5,column=1,sticky=W)
T.grid(row=6,column=0,sticky=W)
T2.grid(row=6,column=1,sticky=W)
root.mainloop()
