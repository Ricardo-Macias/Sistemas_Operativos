import threading
import time
import datetime
import customtkinter

def process(name, size, count):
    app = customtkinter.CTk()
    app.title(name)
    app.geometry(size)

    point = "."

    for count_i in range(count):
        lbl_point = customtkinter.CTkLabel(app, text=point)
        lbl_point.pack()
        point += "."
        time.sleep(1)
        app.update()
        lbl_point.destroy()
    
    app.mainloop()


if __name__ == "__main__":
    start = datetime.datetime.now()

    thread_1 = threading.Thread(name="hilo_1", target=process, args=("Proceso 1", "200x200", 7, ))
    thread_2 = threading.Thread(name="hilo_2", target=process, args=("Proceso 2", "200x200", 5, ))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    end = datetime.datetime.now()

    print(str( end.second - start.second ))