from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator


# Initialize Tkinter
root = Tk()
root.geometry("700x400")
root.title("Language Translator")
root.config(bg='#D3D3D3')

# Header Label
Label(root, text="Language Translator - PythonFlood", font=('Arial', 20, 'bold'), 
      bg='#8B8B7A', fg='White', width=50, pady=5).pack(pady=10)

# Text Frames
f1 = Frame(root, width=320, height=200, bg='white', bd=5)
f1.place(x=15, y=70)
f2 = Frame(root, width=320, height=200, bg='white', bd=5)
f2.place(x=360, y=70)

# Text Widgets
txt1 = Text(f1, font=('Arial', 12, 'bold'), width=28, height=8)
txt1.place(x=0, y=0)
txt2 = Text(f2, font=('Arial', 12, 'bold'), width=28, height=8)
txt2.place(x=0, y=0)

# Get supported languages from googletrans
languages = googletrans.LANGUAGES
language_list = list(languages.values())

# Dropdown Menus
c1 = ttk.Combobox(root, values=language_list, font=('Arial', 12, 'bold'), width=20)
c1.place(x=60, y=290)
c1.set("english")  # Default selection

c2 = ttk.Combobox(root, values=language_list, font=('Arial', 12, 'bold'), width=20)
c2.place(x=420, y=290)
c2.set("spanish")  # Default selection

# Translator instance
translator = Translator()

# Translation Function
def trans_late():
    txt2.delete(1.0, END)
    try:
        from_language = c1.get().lower()  # Convert to lowercase
        to_language = c2.get().lower()  # Convert to lowercase

        from_language_key = next((key for key, value in languages.items() if value == from_language), None)
        to_language_key = next((key for key, value in languages.items() if value == to_language), None)

        if not from_language_key or not to_language_key:
            raise ValueError("Invalid language selection. Please choose from the dropdown list.")

        text_to_translate = txt1.get(1.0, END).strip()
        if not text_to_translate:
            raise ValueError("Please enter text to translate.")

        translated_text = translator.translate(text_to_translate, src=from_language_key, dest=to_language_key).text
        txt2.insert(1.0, translated_text)

    except Exception as e:
        messagebox.showerror("Translator Error", str(e))

# Translate Button
btn = Button(root, text="Translate", font=('Arial', 15, 'bold'), bd=5, 
             bg='#8B8B7A', fg='White', command=trans_late)
btn.place(x=290, y=320)

# Run Tkinter Main Loop
root.mainloop()
