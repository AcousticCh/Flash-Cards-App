from tkinter import *
import pandas
import random
import os
BACKGROUND_COLOR = "#B1DDC6"



# get csv
if os.path.exists("data/words_to_learn.csv"):
    data_frame = pandas.read_csv("data/words_to_learn.csv")
else:
    data_frame = pandas.read_csv("data/french_words.csv")


to_learn = data_frame.to_dict(orient="records")
current_card = random.choice(to_learn)

def next_word():
    global timer, current_card
    screen.after_cancel(timer)
    current_card = random.choice(to_learn)
    card.itemconfig(current_img, image=card_front_img)
    card.itemconfig(card_text_title, text="French", fill="black")
    card.itemconfig(card_text_word, text=current_card["French"], fill="black")
    timer = screen.after(3000, flip)

def flip():
    global current_card
    card.itemconfig(current_img, image=card_back_img)
    card.itemconfig(card_text_title, text="English", fill="white")
    card.itemconfig(card_text_word, text=current_card["English"], fill="white")


def answer_right():
    global to_learn, current_card
    list_index = to_learn.index(current_card)
    to_learn.pop(list_index)
    to_learn_data_frame = pandas.DataFrame().from_records(to_learn)
    to_learn_data_frame.to_csv("data/words_to_learn.csv", index=False)
    next_word()
    # save to_learn to json or csv file





#---------------------- UI SETUP ---------------------#

screen = Tk()
screen.title("Flash Cards")
screen.config(bg=BACKGROUND_COLOR)
screen.config(padx=50, pady=50)


timer = screen.after(3000, func=flip)
# CARD
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
current_img = card.create_image(400, 270, image=card_front_img)
card_text_title = card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_text_word = card.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# BUTTONS
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
incorrect = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
correct = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=answer_right)

incorrect.grid(column=0, row=1)
correct.grid(column=1, row=1)

screen.mainloop()