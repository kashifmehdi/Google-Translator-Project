
#####LIBRARIES IMPORTED#####
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image ###PILLOW LIBRARY
from googletrans import Translator
from tkinter import messagebox

root =tk.Tk()
root.title('Language Translator')
root.geometry('700x430')
root.maxsize(700,360)      
root.minsize(400,300) 

#####FUNCTION THE TRANSLATE EVERYTHING######
def translate():
  language_1=t1.get("1.0","end-1c")
  cl = choose_language.get()
  
  if language_1 == '':
    messagebox.showerror('Language Translator','Please fill the box')
    
  else:
    t2.delete(1.0,'end')
    translator = Translator()
    output = translator.translate(language_1,dest=cl)
    t2.insert('end',output.text)

#####FUNCTION THAT CLEAR THE SENTENCE OR WORD######
def clear():
  t1.delete(1.0,'end')
  t2.delete(1.0,'end')
  
####GOOGLE IMAGE#####
img = ImageTk.PhotoImage(Image.open('google_language.png'))
label = Label(image=img)
label.place(x=287,y=3)

######USER INTERFACE CODE####### 
a = tk.StringVar()
detect_language = ttk.Combobox(root,width=25, textvariable =a,state='readonly',font=('calibre',10,'bold'))

detect_language['values'] = ('Detects language',)
detect_language.place(x = 30 , y= 75)
detect_language.current(0)


l =tk.StringVar()

####LANGUAGES WHICH CAN BE TRANSLATED####
choose_language = ttk.Combobox(root,width=25, textvariable =l ,state='readonly',font=('calibre',10,'bold'))
choose_language['values']=('Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian','Burmese','Catalan','Cebuano','Chinese','Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian','Filipino','Finnish','French','Galician','Georgian','German','Greek','Gujarati','Haitian','Creole','Hausa','Hawaiian','Hebrew','Hindi','Hungarian','Icelandic','Indonesian','Irish','Italian','Japanese','Kannada','Khmer','Korean','Kurdish','Latin','Latvian','Lithuanian','Macedonian','Malayalam','Maltese','Maori','Marathi','Mongolian','Nepali','Norwegian','Pashto','Persian','Polish','Portuguese','Punjabi','Romanian','Russian','Samoan','Scottish Gaelic','Serbian','Sindhi','Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik','Tamil','Tatar','Telugu','Thai','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek','Vietnamese','Welsh','Xhosa','Yiddish','Zulu')
choose_language.place(x=479,y=75)
choose_language.current(0)


#BOX ONE
t1= Text(root ,width =35, height=12,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=120)
#BOX TWO 
t2= Text(root ,width =35, height=12,borderwidth=5,relief=RIDGE)
t2.place(x=395,y=120)

#TRANSLATE BUTTON 
button=Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('arial',10,'bold'),cursor="hand2",command=translate)
button.place(x=309,y=155)

#CLEAR BUTTON
clear = Button(root,text="Clear",relief=RIDGE,borderwidth=3,font=('arial',10,'bold'),cursor="hand2",command=clear)
clear.place(x=319,y=205)
root.mainloop()