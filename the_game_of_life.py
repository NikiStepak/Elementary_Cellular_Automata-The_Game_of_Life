from tkinter import *
from the_game_of_life_function import *
from tkinter import ttk
from random import randint


class GameGUI:
    font = ("Times", 12, "bold")
    box = ("Stable", "Glider", "Oscillatory", "Random", "Tick")
    cell_size = 10
    color = "white"
    running = False
    ust = False
    cell = []
    width = 600
    height = 400

    def __init__(self):
        # utworzenie widżetu okna głównego:
        self.main_window = Tk()
        self.main_window.title("Cellular Automaton - The Game of Life")

        # label frames:
        self.canvas_labelframe = LabelFrame(self.main_window, text="Canvas")
        self.options_labelframe = LabelFrame(self.main_window, text="Options")

        # labels:
        self.loop_label = Label(self.options_labelframe, font=self.font, text="\nNumber of random cells:")
        self.cell_label = Label(self.options_labelframe, font=self.font, text="\nSize of cell:")

        # entries:

        # spin boxes:
        self.loop_spinbox = Spinbox(self.options_labelframe, font=self.font, from_=300, justify=RIGHT, to=10000, width=4)
        self.cell_spinbox = Spinbox(self.options_labelframe, font=self.font, from_=4, justify=RIGHT, to=11, width=4)

        # combo boxes:
        self.condition_combobox = ttk.Combobox(self.options_labelframe, font=self.font, values=self.box)
        self.condition_combobox.current(0)

        # buttons:
        self.start_button = Button(self.options_labelframe, bg="#66809c", fg="white", command=self.start,
                                   font=self.font, text="START")
        self.stop_button = Button(self.options_labelframe, bg="#66809c", fg="white", command=self.stop, font=self.font,
                                  text="STOP")
        self.position_button = Button(self.options_labelframe, bg="#66809c", fg="white", command=self.position,
                                      font=self.font, text="POSITION")
        self.clean_button = Button(self.options_labelframe, bg="#66809c", fg="white", command=self.clean,
                                   font=self.font, text="CLEAN")

        # canvas
        self.rule_canvas = Canvas(self.canvas_labelframe, bg="white", height=400, width=600)

        # pack():
        self.canvas_labelframe.pack(side=LEFT)
        self.condition_combobox.pack()
        self.rule_canvas.bind("<ButtonRelease-1>", self.tick)
        self.rule_canvas.pack()
        self.options_labelframe.pack(side=RIGHT, fill=BOTH)
        self.cell_label.pack()
        self.cell_spinbox.pack()
        self.loop_label.pack()
        self.loop_spinbox.pack()
        self.stop_button.pack(fill=X, side=BOTTOM)
        self.start_button.pack(fill=X, side=BOTTOM)
        self.clean_button.pack(fill=X, side=BOTTOM)
        self.position_button.pack(fill=X, side=BOTTOM)
        self.main_window.after(1, self.game)
        mainloop()

    def tick(self, event):
        if self.ust:
            x1, y1 = (int(event.x/self.cell_size)*self.cell_size), (int(event.y/self.cell_size)*self.cell_size)
            x2, y2 = (x1+self.cell_size), (y1+self.cell_size)
            self.cell[int(y1/self.cell_size)][int(x1/self.cell_size)].val = 1
            self.rule_canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="blue")

    def start(self):
        if self.ust:
            self.running = True

    def stop(self):
        self.running = False

    def game(self):
        if self.running:
            self.paint()
            self.cell = game(self.width, self.height, self.cell)
        self.main_window.after(100, self.game)

    def paint(self):
        self.rule_canvas.delete("all")
        for i in range(self.height):
            y1, y2 = i * self.cell_size, i * self.cell_size + self.cell_size
            for j in range(self.width):
                x1, x2 = j * self.cell_size, j * self.cell_size + self.cell_size
                if self.cell[i][j].val == 1:
                    self.rule_canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def position(self):
        self.clean()
        self.ust = True
        self.cell_size = int(self.cell_spinbox.get())
        self.width = int(self.width/self.cell_size)
        self.height = int(self.height/self.cell_size)
        if self.condition_combobox.get() == self.box[0]:
            self.cell = stable(self.width, self.height)
        elif self.condition_combobox.get() == self.box[1]:
            self.cell = glider(self.width, self.height)
        elif self.condition_combobox.get() == self.box[2]:
            self.cell = oscillator(self.width, self.height)
        elif self.condition_combobox.get() == self.box[3]:
            self.cell = generate(self.width, self.height)
            for i in range(int(self.loop_spinbox.get())):
                self.cell[randint(0, self.height-1)][randint(0, self.width-1)].val = 1
        elif self.condition_combobox.get() == self.box[4]:
            self.cell = generate(self.width, self.height)
        self.paint()

    def clean(self):
        self.stop()
        self.ust = False
        self.width = 600
        self.height = 400
        self.rule_canvas.delete("all")


game_gui = GameGUI()
