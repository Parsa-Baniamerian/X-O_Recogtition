from customtkinter import *

app = CTk()
app.geometry("600x330")

set_appearance_mode("dark")
light_color = "#c9c8bf"
light_hover_color = "#a1a099"
dark_color = "#356296"
dark_hover_color = "#1e3e63"


# * HANDLING BUTTON CLICKS
def add_btn_clicked():
    label_input = switch.get()  # 0 for o and 1 for x
    print(label_input)
    output_lbl.configure(text="")
    message_lbl.configure(text="The new data was saved in the dataset")


def test_btn_clicked():
    message_lbl.configure(text="")
    output_lbl.configure(text="X")


def reset_btn_clicked():
    for btn in buttons:
        btn.configure(fg_color=dark_color, hover_color=dark_hover_color)


def btn_clicked(id):
    # Get the current text color of the button
    current_color = buttons[id].cget("fg_color")
    new_fg_color, new_hover_color = toggle_color(current_color)
    buttons[id].configure(fg_color=new_fg_color, hover_color=new_hover_color)


def toggle_color(current_color):
    if current_color == light_color:
        return dark_color, dark_hover_color
    elif current_color == dark_color:
        return light_color, light_hover_color


# * FRAMES
frame = CTkFrame(master=app, fg_color="transparent")
frame.pack(expand=True)
frame.place(relx=0.27, rely=0.47, anchor="center")


# * BUTTONS
buttons = []
for row in range(5):
    for col in range(5):
        btn_id = row * 5 + col
        button = CTkButton(
            master=frame,
            text="",
            corner_radius=7,
            fg_color=dark_color,
            hover_color=dark_hover_color,
            width=50,
            height=50,
            command=lambda btn_id=btn_id: btn_clicked(btn_id),
        )
        button.grid(row=row, column=col)
        buttons.append(button)


add_btn = CTkButton(
    master=app,
    text="Add to dataset",
    corner_radius=7,
    width=80,
    height=30,
    border_width=2,
    command=add_btn_clicked,
)
add_btn.place(relx=0.75, rely=0.45, anchor="center")

test_btn = CTkButton(
    master=app,
    text="Test",
    corner_radius=7,
    width=80,
    height=30,
    border_width=2,
    command=test_btn_clicked,
)
test_btn.place(relx=0.75, rely=0.68, anchor="center")

reset_btn = CTkButton(
    master=app,
    text="Reset",
    font=("Atrial", 9),
    corner_radius=7,
    width=50,
    height=25,
    border_width=2,
    command=reset_btn_clicked,
)
reset_btn.place(relx=0.11, rely=0.92, anchor="center")


# * SWITCH
switch = CTkSwitch(
    master=app,
    width=30,
    text="X",
    font=("Atrial", 16, "bold"),
    text_color=light_color
)
switch.place(relx=0.59, rely=0.45, anchor="center")


# * LABELS
o_switch = CTkLabel(
    master=app,
    width=18,
    height=18,
    text="O",
    font=("Atrial", 16, "bold"),
    fg_color="transparent",
    text_color=light_color
)
o_switch.place(relx=0.52, rely=0.45, anchor="center")

title_lbl = CTkLabel(
    master=app,
    width=270,
    height=100,
    text="X/O Recognition",
    font=("Atrial", 32, "bold"),
    fg_color="transparent",
    text_color=light_color,
)
title_lbl.place(relx=0.75, rely=0.15, anchor="center")

message_lbl = CTkLabel(
    master=app,
    width=300,
    height=10,
    text="",
    font=("Atrial", 13),
    fg_color="transparent",
    text_color=light_color,
)
message_lbl.place(relx=0.75, rely=0.52, anchor="center")

output_lbl = CTkLabel(
    master=app,
    width=40,
    height=15,
    text="",
    font=("Atrial", 20, "bold"),
    fg_color="transparent",
    text_color=light_color,
)
output_lbl.place(relx=0.87, rely=0.68, anchor="center")

app.mainloop()
