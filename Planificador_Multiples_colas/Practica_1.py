import customtkinter as CTk

class progressBar(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("300x300")
        self.title("Barra de progreso")
        
        self.bar = CTk.CTkProgressBar(self, orientation="vertical", width=20, height=200)
        self.bar.place(x=140, y=10)
        self.bar.set(0)

        CTk.CTkButton(self, text="Iniciar", command=self.start, width=40, height=30).place(x=125, y=220)
    
    def start(self):
        iter_step = 1 / 100
        progress_step = iter_step
        self.bar.start()

        for count in range(100):
            self.bar.set(progress_step)
            progress_step += iter_step
            self.update_idletasks()
        
        self.bar.stop()

        
if __name__ == "__main__":

    app = progressBar()
    app.mainloop()