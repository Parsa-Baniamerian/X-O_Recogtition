from customtkinter import *

app = CTk()
app.geometry("600x400")

set_appearance_mode("dark")
light_color = "#c9c8bf"
light_hover_color = "#a1a099"
dark_color = "#356296"
dark_hover_color = "#1e3e63"


# * HANDLING BUTTON CLICKS
def add_btn_clicked():
    #! remember to add the check bar's number!
    output_lbl.configure(text="")
    message_lbl.configure(text="The new data was saved in the dataset")


def test_btn_clicked():

    message_lbl.configure(text="")
    output_lbl.configure(text="X")


def btn_clicked():

    current_color = ""  # ! I need to get the fg_color of selected btn
    new_fg_color, new_hover_color = toggle_color(current_color)
    # ! I need to get the ID of the selected btn for the bottom line:
    btn00.configure(fg_color=new_fg_color, hover_color=new_hover_color)


def toggle_color(current_color):
    if current_color == light_color:
        return dark_color, dark_hover_color
    elif current_color == dark_color:
        return light_color, light_hover_color


# * FRAMES
frame = CTkFrame(master=app, fg_color="transparent")
frame.pack(expand=True)
frame.place(relx=0.27, rely=0.4, anchor="center")

#! add a check bar to label that the new data is X or O


# * BUTTONS
# ROW0
btn00 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn00.grid(row=0, column=0)

btn01 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn01.grid(row=0, column=1)

btn02 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn02.grid(row=0, column=2)

btn03 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn03.grid(row=0, column=3)

btn04 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn04.grid(row=0, column=4)

# ROW1
btn10 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn10.grid(row=1, column=0)

btn11 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn11.grid(row=1, column=1)

btn12 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn12.grid(row=1, column=2)

btn13 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn13.grid(row=1, column=3)

btn14 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn14.grid(row=1, column=4)

# ROW2
btn20 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn20.grid(row=2, column=0)

btn21 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn21.grid(row=2, column=1)

btn22 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn22.grid(row=2, column=2)

btn23 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn23.grid(row=2, column=3)

btn24 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn24.grid(row=2, column=4)

# ROW3
btn30 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn30.grid(row=3, column=0)

btn31 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn31.grid(row=3, column=1)

btn32 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn32.grid(row=3, column=2)

btn33 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn33.grid(row=3, column=3)

btn34 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn34.grid(row=3, column=4)

# ROW4
btn40 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn40.grid(row=4, column=0)

btn41 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn41.grid(row=4, column=1)

btn42 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn42.grid(row=4, column=2)

btn43 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn43.grid(row=4, column=3)

btn44 = CTkButton(master=frame, text="", corner_radius=7, fg_color=dark_color, hover_color=dark_hover_color,
                  width=50, height=50, command=btn_clicked)
btn44.grid(row=4, column=4)


add_btn = CTkButton(master=app, text="Add to dataset", corner_radius=7,
                    width=80, height=30, border_width=2, command=add_btn_clicked)
add_btn.place(relx=0.75, rely=0.45, anchor="center")
test_btn = CTkButton(master=app, text="Test", corner_radius=7,
                     width=80, height=30, border_width=2, command=test_btn_clicked)
test_btn.place(relx=0.75, rely=0.68, anchor="center")


# * LABELS
title_lbl = CTkLabel(master=app, width=270, height=100, text="X/O Recognition",
                     font=("Atrial", 32, "bold"), fg_color="transparent", text_color=light_color)
title_lbl.place(relx=0.75, rely=0.15, anchor="center")

message_lbl = CTkLabel(master=app, width=300, height=10, text="",
                       font=("Atrial", 13), fg_color="transparent", text_color=light_color)
message_lbl.place(relx=0.75, rely=0.52, anchor="center")

output_lbl = CTkLabel(master=app, width=40, height=15,
                      text="", font=("Atrial", 20, "bold"), fg_color="transparent", text_color=light_color)
output_lbl.place(relx=0.87, rely=0.68, anchor="center")


app.mainloop()
