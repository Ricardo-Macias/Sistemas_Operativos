import customtkinter
import time
from PIL import Image, ImageTk

class FCFS_planner:
    def __init__(self, window, image, list_process):
        self.window = window
        self.image = image
        self.list_process = list_process

        self.frame = customtkinter.CTkFrame(self.window, fg_color="green", width=900, height=400)
        self.frame.place(x=0, y=0)

        self.frame_time = customtkinter.CTkFrame(self.window, fg_color="lightblue", width=200, height=120)
        self.frame_time.place(x=230, y=410)

        self.frame_process = customtkinter.CTkFrame(self.window, fg_color="gray", width=250, height=120)
        self.frame_process.place(x=450, y=410)

        button_start = customtkinter.CTkButton(self.window, text="Iniciar", command=self.FCFS, width=200, height=120, font=("Arial",30))
        button_start.place(x=10, y=410)

    def FCFS(self):
        date_x = 0
        date_y = 10
        complete_y = 5
        count_time = 0

        while len(self.list_process) != 0:
            lbl_process = customtkinter.CTkLabel(self.frame, image=self.image, text="", fg_color="transparent")
            lbl_process.place(x=date_x, y=date_y)

            process = self.list_process[0].split(",")
            progress = 820/int(process[2])

            self.label(process[0], process[3], process[4])
            self.window.update()

            for count in range(int(process[2])):
                time.sleep(1)
                count_time += 1
                date_x += progress

                lbl_process.destroy()
                lbl_process = customtkinter.CTkLabel(self.frame, image=self.image, text="", fg_color="transparent")
                lbl_process.place(x=date_x, y=date_y)

                lbl_count_time = customtkinter.CTkLabel(self.frame_time, text=f"Tiempo:            {count_time}", fg_color="lightblue")
                lbl_count_time.place(x=20, y=70)

                self.window.update()

            self.end(process[0], complete_y)
            time.sleep(1)
            self.list_process.pop(0)

            complete_y += 22
            date_y += 75
            date_x = 0

        
    def label(self, name_process, start_process, end_process):
        lbl_process = customtkinter.CTkLabel(self.frame_time, text=f"Proceso:           {name_process}", fg_color="lightblue")
        lbl_process.place(x=20, y=10)

        lbl_start_time = customtkinter.CTkLabel(self.frame_time, text=f"Inicio:                {start_process}", fg_color="lightblue")
        lbl_start_time.place(x=20, y=30)

        lbl_end_time = customtkinter.CTkLabel(self.frame_time, text=f"Final:                 {end_process}", fg_color="lightblue")
        lbl_end_time.place(x=20, y=50)
    
    def end(self, name_process, date_y):
        lbl_process = customtkinter.CTkLabel(self.frame_process, text=f"El {name_process} llego al final")
        lbl_process.place(x=20, y=date_y)

if __name__ == "__main__":

    app = customtkinter.CTk()
    app.geometry("900x540")
    app.title("Planificador FCFS")

    image_horse = customtkinter.CTkImage(
        light_image=Image.open("Planificador_FCFS/caballo.png"),
        size=(75,75)
    )

    list_process = [
        "Caballo A,0,3,0,3",
        "Caballo B,1,5,3,8",
        "Caballo C,3,2,8,10",
        "Caballo D,9,5,10,15",
        "Caballo E,12,5,15,20"
    ]

    FCFS_planner(app, image_horse, list_process)

    app.mainloop()