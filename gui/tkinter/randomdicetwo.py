import tkinter as tk
import random


def draw_dice(number, initiation=0):
    dice_size = 150

    x_center = (dice_size / 2) + 10 + initiation
    y_center = (dice_size / 2) + 10

    if number == 1:
        draw_dot(x_center, y_center)
    elif number == 2:
        draw_dot(x_center - 40, y_center + 40)
        draw_dot(x_center + 40, y_center - 40)
    elif number == 3:
        draw_dot(x_center - 40, y_center + 40)
        draw_dot(x_center, y_center)
        draw_dot(x_center + 40, y_center - 40)
    elif number == 4:
        draw_dot(x_center - 40, y_center + 40)
        draw_dot(x_center + 40, y_center + 40)
        draw_dot(x_center - 40, y_center - 40)
        draw_dot(x_center + 40, y_center - 40)
    elif number == 5:
        draw_dot(x_center - 40, y_center + 40)
        draw_dot(x_center + 40, y_center + 40)
        draw_dot(x_center, y_center)
        draw_dot(x_center - 40, y_center - 40)
        draw_dot(x_center + 40, y_center - 40)
    elif number == 6:
        draw_dot(x_center - 40, y_center + 40)
        draw_dot(x_center + 40, y_center + 40)
        draw_dot(x_center - 40, y_center)
        draw_dot(x_center + 40, y_center)
        draw_dot(x_center - 40, y_center - 40)
        draw_dot(x_center + 40, y_center - 40)


def draw_dot(x, y):
    dot_radius = 15
    canvas.create_oval(
        x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill="black"
    )


def roll_dice():
    canvas.delete("all")
    canvas.create_rectangle(
        10, 10, dice_size + 10, dice_size + 10, outline="black", width=2
    )
    canvas.create_rectangle(
        170, 10, dice_size + 160, dice_size + 10, outline="black", width=2
    )
    number = random.randint(1, 6)
    number2 = random.randint(1, 6)
    result_label.config(text=f"Resultado: {number} - {number2}")
    draw_dice(number)
    draw_dice(number2, 155)


window = tk.Tk()
window.title("Dado")

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

dice_size = 150
canvas = tk.Canvas(
    frame,
    width=dice_size + dice_size + 20,
    height=dice_size + 20,
    bg="white",
)
canvas.pack()

result_label = tk.Label(frame, text="Resultado: ", font=("Helvetica", 16))
result_label.pack(pady=10)

roll_button = tk.Button(frame, text="Lanzar Dado", command=roll_dice)
roll_button.pack()

window.mainloop()
