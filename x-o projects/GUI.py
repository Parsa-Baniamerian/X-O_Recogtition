from customtkinter import *

app = CTk()
app.geometry("600x330")

set_appearance_mode("dark")
light_color = "#c9c8bf"
light_hover_color = "#a1a099"
dark_color = "#356296"
dark_hover_color = "#1e3e63"


def prepare_data():
    new_data = []
    input_label = switch.get()
    if input_label == 0:
        input_label = -1
    new_data.append(input_label)
    for btn in buttons:
        btn_color = btn.cget("fg_color")

        if btn_color == dark_color:
            new_data.append(-1)
        elif btn_color == light_color:
            new_data.append(1)
    return new_data


def exist_same_data(file_name, new_data):
    with open(file_name, "r") as file:
        for line in file:
            existing_data = list(map(int, line.strip().split(",")))
            if new_data == existing_data:
                return True
    return False


def save_data_in_dataset(new_data):

    dataset_file = "./Dataset.txt"
    if not exist_same_data(file_name=dataset_file, new_data=new_data):
        with open(dataset_file, "a") as file:
            data_str = ",".join(map(str, new_data))
            file.write(data_str + "\n")
        return True
    return False


# * HANDLING BUTTON CLICKS
def add_btn_clicked():
    add_data_result_lbl.configure(text="")
    output_lbl.configure(text="")
    is_saved = save_data_in_dataset(prepare_data())
    reset_grid()
    if is_saved:
        add_data_result_lbl.configure(
            text="The new data was saved in the dataset")
    else:
        add_data_result_lbl.configure(
            text="This data already exists in the dataset")


def train_btn_clicked():
    algorithm = algorithms_combo.get()
    train_result_lbl.configure(text="")
    output_lbl.configure(text="")
    train_result_lbl.configure(text = algorithm +" algorithm was trained successfully")

def test_btn_clicked():

    add_data_result_lbl.configure(text="")
    train_result_lbl.configure(text="")
    output_lbl.configure(text="X")


def reset_grid():
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

train_btn = CTkButton(
    master=app,
    text="Train",
    corner_radius=7,
    width=80,
    height=30,
    border_width=2,
    command=train_btn_clicked
)
train_btn.place(relx=0.75, rely=0.68, anchor="center")

test_btn = CTkButton(
    master=app,
    text="Test",
    corner_radius=7,
    width=80,
    height=30,
    border_width=2,
    command=test_btn_clicked
)
test_btn.place(relx=0.75, rely=0.9, anchor="center")

reset_btn = CTkButton(
    master=app,
    text="Reset",
    font=("Atrial", 9),
    corner_radius=7,
    width=50,
    height=25,
    border_width=2,
    command=reset_grid
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


# *COMBOBOX
algorithms_combo = CTkComboBox(
    master=app,
    values=["Hebb", "Perceptron", "MLP", "Adaline"],
    text_color=light_color,
    font=("Atrial", 12, "bold"),
    width=105,
    border_color=dark_color,
    button_color=dark_color,
    button_hover_color=dark_hover_color
)
algorithms_combo.place(relx=0.58, rely=0.68, anchor="center")


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
    text_color=light_color
)
title_lbl.place(relx=0.75, rely=0.15, anchor="center")

add_data_result_lbl = CTkLabel(
    master=app,
    width=300,
    height=10,
    text="",
    font=("Atrial", 13),
    fg_color="transparent",
    text_color=light_color
)
add_data_result_lbl.place(relx=0.75, rely=0.53, anchor="center")

train_result_lbl = CTkLabel(
    master=app,
    width=300,
    height=10,
    text="",
    font=("Atrial", 13),
    fg_color="transparent",
    text_color=light_color
)
train_result_lbl.place(relx=0.75, rely=0.76, anchor="center")


output_lbl = CTkLabel(
    master=app,
    width=60,
    height=25,
    text="",
    font=("Atrial", 28, "bold"),
    fg_color="transparent",
    text_color=light_color
)
output_lbl.place(relx=0.87, rely=0.9, anchor="center")

app.mainloop()
