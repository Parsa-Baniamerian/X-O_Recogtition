from customtkinter import *
import time
from hebb import training as hebb_training, testing as hebb_testing
from perceptron import training as perceptron_training, testing as perceptron_testing
from multi_class_perceptron import training as multi_class_perceptron_training, testing as multi_class_perceptron_testing
from adaline import training as adaline_training, testing as adaline_testing
from MLP import training as MLP_training, testing as MLP_testing


app = CTk()
app.title("X/O Recognition")
app.geometry("600x330")
app.resizable(False, False)

set_appearance_mode("dark")
light_color = "#c9c8bf"
light_hover_color = "#a1a099"
dark_color = "#356296"
dark_hover_color = "#1e3e63"

weights, bias, current_algorithm_trained = None, None, None
l1_weights, l1_bias, l2_weights, l2_bias = None, None, None, None

algorithms_functions = {
    "Hebb": {"train": hebb_training, "test": hebb_testing},
    "Perceptron": {"train": perceptron_training, "test": perceptron_testing},
    "Multi-Class Perceptron": {"train": multi_class_perceptron_training, "test": multi_class_perceptron_testing},
    "Adaline": {"train": adaline_training, "test": adaline_testing},
    "MLP": {"train": MLP_training, "test": MLP_testing}
}


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
    dataset_file = "./Dataset/Dataset.txt"
    if not exist_same_data(file_name=dataset_file, new_data=new_data):
        with open(dataset_file, "a") as file:
            data_str = ",".join(map(str, new_data))
            file.write(data_str + "\n")
        return True
    return False


# * HANDLING BUTTON CLICKS
def add_btn_clicked():
    is_saved = save_data_in_dataset(prepare_data())
    reset_grid()
    if is_saved:
        add_data_result_lbl.configure(
            text="The new data was saved in the dataset")
    else:
        add_data_result_lbl.configure(
            text="This data already exists in the dataset")
    train_result_lbl.configure(text="")
    output_lbl.configure(text="")
    error_message_lbl.configure(text="")


def train_btn_clicked():
    global weights, bias, current_algorithm_trained, l1_weights, l1_bias, l2_weights, l2_bias
    selected_algorithm = algorithms_combo.get()
    algorithm = algorithms_functions.get(selected_algorithm)
    start_time = time.time()
    if selected_algorithm == "MLP":
        l1_weights, l1_bias, l2_weights, l2_bias = algorithm["train"](dataset_file="./Dataset/train_data.txt")
    else:
        weights, bias = algorithm["train"](dataset_file="./Dataset/train_data.txt")
    finish_time = time.time()
    runtime = (finish_time - start_time) * 1000
    print(f"{selected_algorithm} algorithm was trained in {runtime} ms")
    current_algorithm_trained = selected_algorithm
    train_result_lbl.configure(
        text=f"{selected_algorithm} algorithm was trained successfully")

    add_data_result_lbl.configure(text="")
    output_lbl.configure(text="")
    error_message_lbl.configure(text="")


def test_btn_clicked():
    global weights, bias, current_algorithm_trained, l1_weights, l1_bias, l2_weights, l2_bias
    error_message_lbl.configure(text="")
    add_data_result_lbl.configure(text="")
    train_result_lbl.configure(text="")
    output_lbl.configure(text="")
    selected_algorithm = algorithms_combo.get()

    algorithm = algorithms_functions.get(selected_algorithm)
    input_data = prepare_data()

    if all(x == -1 for x in input_data[1:]):
        error_message_lbl.configure(text="Please enter an entry in the grid!")
    else:
        if (selected_algorithm != "MLP" and weights == None):
            error_message_lbl.configure(text="Please train the model first!")
        elif selected_algorithm != current_algorithm_trained:
            error_message_lbl.configure(
                text=f"Please train the {selected_algorithm} algorithm first!")
        else:
            if selected_algorithm == "MLP":
                result = algorithm["test"](input_data[1:], l1_weights, l1_bias, l2_weights, l2_bias)
            else:
                result = algorithm["test"](input_data, weights, bias)
            output_lbl.configure(text=result)


def reset_grid():
    for btn in buttons:
        btn.configure(fg_color=dark_color, hover_color=dark_hover_color)
    add_data_result_lbl.configure(text="")
    train_result_lbl.configure(text="")
    output_lbl.configure(text="")
    error_message_lbl.configure(text="")


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
    values=["Hebb", "Perceptron", "Multi-Class Perceptron", "Adaline", "MLP"],
    text_color=light_color,
    font=("Atrial", 11, "bold"),
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
    width=95,
    height=25,
    text="",
    font=("Atrial", 22, "bold"),
    fg_color="transparent",
    text_color=light_color
)
output_lbl.place(relx=0.91, rely=0.9, anchor="center")

error_message_lbl = CTkLabel(
    master=app,
    width=300,
    height=10,
    text="",
    font=("Atrial", 13),
    fg_color="transparent",
    text_color=light_color
)
error_message_lbl.place(relx=0.75, rely=0.97, anchor="center")

app.mainloop()
