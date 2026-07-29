import threading
import time
import datetime
import customtkinter

def process(label,count):

    for i in range(count):
        time.sleep(1)

        current_text = label.cget("text")
        new_text = current_text + "."

        label.configure(text=new_text)
        


if __name__ == "__main__":
    app = customtkinter.CTk()
    app.title("Hilos")
    app.geometry("200x200")
    start = datetime.datetime.now()

    frame_thread_1 = customtkinter.CTkFrame(app)
    frame_thread_1.pack(side="left", fill="both", expand=True)
    frame_thread_2 = customtkinter.CTkFrame(app)
    frame_thread_2.pack(side="right", fill="both", expand=True)

    lbl_thread_1 = customtkinter.CTkLabel(frame_thread_1, text="Hilo 1: ")
    lbl_thread_1.pack()
    lbl_thread_2 = customtkinter.CTkLabel(frame_thread_2, text="Hilo 2: ")
    lbl_thread_2.pack()

    thread_1 = threading.Thread(name="hilo_1", target=process, args=(lbl_thread_1, 7, ))
    thread_2 = threading.Thread(name="hilo_2", target=process, args=(lbl_thread_2, 5, ))

    thread_1.start()
    thread_2.start()

    app.mainloop()

    end = datetime.datetime.now()
    print(str( end.second - start.second ))
    app.mainloop()