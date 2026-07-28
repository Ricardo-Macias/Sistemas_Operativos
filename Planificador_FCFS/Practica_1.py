import customtkinter
import time
from PIL import Image, ImageTk

class FCFS_planner:
    def __init__(self, window, image, list_process):
        self.window = window
        self.image = image
        self.list_process = list_process

        self.frame = customtkinter.CTkFrame(self.window, fg_color="GREEN2", width=900, height=400)
        self.frame.place(x=0, y=0)


if __name__ == "__main__":

    app = customtkinter.CTk()
    app.geometry("900x540")
    app.title("Planificador FCFS")

    Image_horse = Image.open("Planificador_FCFS/caballo.png")
    Image_horse = Image_horse.resize((75,75))
    render_horse = ImageTk.PhotoImage(Image_horse)

    list_process = [
        "Caballo A,0,3,0,3",
        "Caballo B,1,5,3,8",
        "Caballo C,3,2,8,10",
        "Caballo D,9,5,10,15",
        "Caballo E,12,5,15,20"
    ]

    app.mainloop()