from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk , Image
from googletrans import Translator
from tkinter import messagebox


root = tk.Tk()
root.title('Language translator')
root.geometry('530x330')  #width and height
root.maxsize(530,330)
root.minsize(530,330)


def translate():
    language_1 = t1.get('1.0','end-1c')  #getting the entry language and stroring in the language_1
    cl  = choose_language.get()

    if language_1 == '':
        messagebox.showerror('Language Translator','please fill the box')

    else:
        translator = Translator()
        output = translator.translate(language_1,Dest=cl)
        t2.insert('end',output.txt)
        
        
def clear():
    t1.delete(1.0,'end')
    t2.delete(1.0,'end')

    
img = ImageTk.PhotoImage(Image.open('translator.png'))  #opening translatoor image as img.
label = Label(image = img)  #saving the image as a label
label.place(x=230,y=3)  #placing the label


a = tk.StringVar()   #the input string that we give will be stored in a
auto_detect = ttk.Combobox(root, width = 20, textvariable = a, state='readonly', font=('verdana',10,'bold'),)
#combobox(dropdownlist) displaing list of all the languages in the combobox.


#for autodetecting the type of language that we enter
auto_detect['values'] = (
                          'Auto_Detect'
                          )
# creating the autodetect box
auto_detect.place(x=30,y=70) #placing the autodetect box
auto_detect.current(0)




l = tk.StringVar()
choose_language = ttk.Combobox(root, width = 20, textvariable = l , state= 'readonly',font = ('verdana',10,'bold'),)


choose_language['values'] = (
                              'Afrikaans',
                              'Albanian',
                              'Arabic',
                              'American',
                              'Azerbaijani',
                              'Basque',
                              'Belarusian',
                              'Bengali',
                              'Bosnian',
                              'Bulgarian',
                              'Catalan',
                              'Cebuano',
                              'Chichewa',
                              'Chinese',
                              'Corsican',
                              'croatian',
                              'Czech',
                              'Danish',
                              'Dutch',
                              'English',
                              'Esperanto',
                              'Estonian',
                              'Filipino',
                              'Finnish',
                              'French',
                              'Galician',
                              'Georgian',
                              'German',
                              'Greek',
                              'Gujarati',
                              'Haitian creole',
                              'Hausa',
                              'Hawaiian',
                              'Hebrew',
                              'Hindi',
                              'Hmong',
                              'Hungarian',
                              'Icelandic',
                              'Igbo',
                              'Indonesian',
                              'Irish',
                              'Italian',
                              'Japanese',
                              'Kannada',
                              'Kazakh',
                              'Khmer',
                              'Kinyarwanda',
                              'Korean',
                              'Kurdish',
                              'Kyrgyz',
                              'Lao',
                              'Latin',
                              'Latvian',
                              'Lithuanian',
                              'Laxembourgish'
                              'Macedonian',
                              'Malagsy',
                              'malay',
                              'Malayalam',
                              'Maltese',
                              'Maori',
                              'Marathi',
                              'Mangilian',
                              'Myanmar',
                              'Nepali',
                              'Norwegain',
                              'Odia',
                              'Pashto',
                              'Persian',
                              'Polish',
                              'Portuguese',
                              'Punjabi',
                              'Romanian',
                              'Russain',
                              'Samoan',
                              'Scots Gaelic',
                              'Serbian',
                              'Sesotho',
                              'Shona',
                              'Sindhi',
                              'Sinhala',
                              'Slovak',
                              'Slovenian',
                              'Somali',
                              'Swedish',
                              'Tajik',
                              'Tamil',
                              'Tatar',
                              'Telugu',
                              'Thai',
                              'Turkish',
                              'Turkmen',
                              'Ukrainian',
                              'Urdu',
                              'Uyghur',
                              'Uzbek',
                              'Vietnmese',
                              'Welsh',
                              'Xhosa',
                              'Yiddish',
                              'Yoruba',
                              'Zulu',
                               )


choose_language.place(x=290,y=70)
choose_language.current(0)


t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)
 

t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)

button = Button(root,text = 'Translate',relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor='hand2',command=translate)
button.place(x=150,y=280)


clear = Button(root,text = 'Clear',relief=RIDGE,borderwidth=3,font=('verdana',10,'bold'),cursor='hand2',command=clear)
clear.place(x=280,y=280)


root.mainloop()












