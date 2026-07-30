import time
import threading
import customtkinter

def create_Progressbar(app, position_x, position_y):
    progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal", width=200, height=15, corner_radius=5)
    progressbar.place(x=position_x, y=position_y)
    progressbar.set(0)

    return progressbar

def start(thread, thread_2, thread_3):
    thread.start()
    thread_2.start()
    thread_3.start()

def multiqueue_planner(app, x, y, list_process):
    progressbar = create_Progressbar(app, x, y)
    lbl_name = customtkinter.CTkLabel(app, text="")
    lbl_name.place(x=10, y=(y-7))

    while len(list_process) != 0:
        count = 0
        process = list_process[0].split(",")
        progress = 1 / int(process[2])
        lbl_name.configure(text=process[0])

        for i in range(int(process[2]) + 1):
            progressbar.set(count)
            count += progress
            app.update_idletasks()
            time.sleep(1)

        list_process.pop(0)

if __name__ == "__main__":
    app = customtkinter.CTk()
    app.title("Simulador de procesos")
    app.geometry("400x240")

    list_process_1 = [
        "Google Chrome, 11, 2",
        "Slack, 8, 3",
        "Registry, 6, 7",
        "Word, 7, 10",
        "Correo, 2, 8"
    ]

    list_process_2 = [
        "Inicio, 3, 5",
        "Shell, 6, 3",
        "Host de Servicio, 10, 3",
        "Excel, 8, 8",
        "SysMain,1 , 12"
    ]

    list_process_3 = [
        "Microsoft Text, 7, 2",
        "System, 8, 4",
        "Wininit, 1, 3",
        "smss, 2, 3",
        "Paint, 9, 13"
    ]

    thread = threading.Thread(name="Hilo 1", target=multiqueue_planner, args=(app, 120, 40, list_process_1))
    thread_2 = threading.Thread(name="Hilo 2", target=multiqueue_planner, args=(app, 120, 80, list_process_2))
    thread_3 = threading.Thread(name="Hilo 3", target=multiqueue_planner, args=(app, 120, 120, list_process_3))

    btnStart = customtkinter.CTkButton(app, text="Iniciar", command=lambda: start(thread, thread_2, thread_3), font=('Arial',20), width=100, height=50)
    btnStart.place(x=50, y=170)

    app.mainloop()