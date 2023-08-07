import tkinter as tk
import random


def draw_dice(text, init=0):
    dice_size = 155

    canvas.create_rectangle(
        10 + init + (init // 15),
        10,
        dice_size + 10 + init,
        dice_size + 10,
        outline="black",
        width=2,
    )

    x_center = (dice_size / 2) + 10 + init
    y_center = (dice_size / 2) + 10

    canvas.create_text(
        x_center, y_center, text=text, fill="black", font=("Helvetica 28 bold")
    )


def roll_dice():
    canvas.delete("all")
    text_dice = random.choice(["a", "b", "c", "d", "e", "f"])
    text_dice_2 = random.choice(["1", "2", "3", "4", "5", "6"])
    result_label.config(text=f"Resultado: {text_dice} - {text_dice_2}")
    draw_dice(text_dice)
    draw_dice(text_dice_2, 155)


window = tk.Tk()
window.title("Dado")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

size = 150
canvas = tk.Canvas(frame, width=size + size + 25, height=size + 20, bg="white")
canvas.pack()

result_label = tk.Label(frame, text="Resultado: ", font=("Helvetica", 16))
result_label.pack(pady=10)

roll_button = tk.Button(frame, text="Lanzar Dado", command=roll_dice)
roll_button.pack()

window.mainloop()
