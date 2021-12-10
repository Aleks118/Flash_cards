from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
chosen_word = {}
language_dict = {}



#------------------------------- Random Word ----------------------------------#

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = data.to_dict(orient="records")




def random_word():
    global chosen_word,flip_timer
    window.after_cancel(flip_timer)
    chosen_word = random.choice(language_dict)
    canvas.itemconfig(card_title, text="French" , fill = "black")
    canvas.itemconfig(card_word, text= chosen_word["French"], fill ="black")
    canvas.itemconfig(background, image=card_image)
    flip_timer =window.after(3000, func=flip_card)


#------------------------------- Flip Card ----------------------------------#

def flip_card():
    canvas.itemconfig(background, image=card_back)
    canvas.itemconfig(card_title, text="English" ,  fill = "white")
    canvas.itemconfig(card_word, text= chosen_word["English"], fill="white")

#-------------------------------NEW UNKNOW----------------------------------#

def is_known():
    language_dict.remove(chosen_word)
    print(len(language_dict))
    data = pandas.DataFrame(language_dict)
    data.to_csv("data/words_to_learn.csv",index=False)
    random_word()

#-------------------------------UI SETUP----------------------------------#


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000 , func=flip_card)

canvas = Canvas(width = 800 , height = 526,highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
background = canvas.create_image(400,263,image=card_image)
canvas.grid(row = 0 , column = 0 ,columnspan = 2)
canvas.config(bg = BACKGROUND_COLOR)
card_title = canvas.create_text(400,150,text = "French",fill="black", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text = "FRENCH_WORD" ,fill="black", font=("Ariel",60,"bold"))


right = PhotoImage(file="images/right.png")
button_right = Button(image=right, highlightthickness=0, bd = 0 ,command=is_known)
button_right.grid(row = 1, column = 1 )

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, bd = 0, command=chosen_word)
button_wrong.config(bg = BACKGROUND_COLOR)
button_wrong.grid(row = 1, column = 0 )

random_word()

window.after_cancel(flip_card)


window.mainloop()