# from PIL import Image
BACKGROUND_COLOR = "#B1DDC6"

import pandas

from tkinter import PhotoImage, Canvas
from tkinter import Button
from tkinter import *
#from pandas._libs.algos import backfill
from random import *
white = "#FFFFFF"
current_card = {}
to_learn = {}


#data = pandas.read_csv(r"C:\Users\acer\Downloads\words_to_learn.csv", encoding='utf-8-sig')
#data["arabic"] = "\u202E" + data["arabic"].apply(lambda word: word[::-1])#to make sure the arabic script isn't laterally inverted
#to_learn = data.to_dict(orient="records")
#"C:\Users\acer\Downloads\flash-card-project-start (1)"
try:
    #with open(r'words_to_learn.csv', "r") as file:
    data = pandas.read_csv(r"C:\Users\acer\Downloads\flash-card-project-start (1)\words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.DataFrame(r"C:\Users\acer\Downloads\flash-card-project-start (1)\images\word_list.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def word_change():
    global current_word, flip_time
    window.after_cancel(flip_time)
    current_word = choice(to_learn)
    canvas.itemconfig(title, fill="black")
    canvas.itemconfig(word, text=current_word["arabic"], fill="black")
    canvas.itemconfig(background, image=frontside)
    flip_time = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title, text="english", fill=white)
    canvas.itemconfig(word, text=current_word["english"], fill=white)
    canvas.itemconfig(background, image=backside)

def is_known():
    global data, to_learn
    #to_learn = data.to_dict(orient="records")
    to_learn.remove(current_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv(r"C:\Users\acer\Downloads\words_to_learn.csv", "w", index=False, encoding='utf-8-sig')
    word_change()


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_time = window.after(3000, flip_card)

frontside = PhotoImage(file=r"C:\Users\acer\Downloads\flash-card-project-start (1)\images\card_front.png")
backside = PhotoImage(file=r"C:\Users\acer\Downloads\flash-card-project-start (1)\images\card_back.png")
r_image = PhotoImage(file=r"C:\Users\acer\Downloads\flash-card-project-start (1)\images\right.png")
l_image = PhotoImage(file=r"C:\Users\acer\Downloads\flash-card-project-start (1)\images\wrong.png")

canvas = Canvas(window, width=800, height=526)
background = canvas.create_image(400, 263, image=frontside)

title = canvas.create_text(400, 150, text="arabic", font=("Arial", 30, "italic"))
word = canvas.create_text(400, 280, text="", font=("Arial", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

#new_face = canvas.itemconfig(front, image=backside, fill=white_color)
canvas.grid(column=0, row=0, columnspan=2)#this cspan makes sure the r w buttons are closer


r_button = Button(window, image=r_image, bg=BACKGROUND_COLOR, command=word_change, highlightthickness=0)
r_button.grid(column=0, row=1)

w_button = Button(window, image=l_image, command=is_known, bg=BACKGROUND_COLOR, highlightthickness=0)
w_button.grid(column=1, row=1)

word_change()

window.mainloop()
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
#
# output = ""
# word1  = "abc"
# word2 = "xyz"
# words = word1 + word2
# n_words = int(len(word1 + word2)/2)
# for (turn) in range(0, n_words):
#     output += word1[turn]
#     output += word2[turn]
# print(output)
# # print(words)
# # the_letter = ""
# # for letter in words:
# #     print(letter)
# #     if words[letter + 1] % 2 == 1:
# #         #actually odd
# #         turn = "even"
# #
# #     else:
# #         turn = "odd"
# #     print(turn)
# #     # if turn = "odd":
#     #     output += word1[letter]
#         # output = word1[]
