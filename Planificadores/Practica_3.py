import customtkinter
import threading
import time
from tkinter import ttk


class scheduling_algorithm:

    def SJF(processes, config=[]):
        previousTime = 0
        for process in processes:
            acurrentProcess = process.split(",")
            acurrentTime = int(acurrentProcess[config[1]])
            if ((acurrentTime < previousTime) or (previousTime == 0)):
                previousTime = acurrentTime
                previousProcess = acurrentProcess

        processes.remove((",".join(previousProcess)))
        return previousProcess, processes

    def Priority(processes, config=[]):
        firstIterationFlag = True
        descending_priority = config[2]
        previousPriority = 0
        for process in processes:
            acurrentProcess = process.split(",")
            acurrentPriority = int(acurrentProcess[config[0]])
            if (descending_priority):
                if ((acurrentPriority > previousPriority) or (firstIterationFlag)):
                    previousPriority = acurrentPriority
                    previousProcess = acurrentProcess
            else:
                if ((acurrentPriority < previousPriority) or (firstIterationFlag)):
                    previousPriority = acurrentPriority
                    previousProcess = acurrentProcess

            firstIterationFlag = False
        processes.remove((",".join(previousProcess)))
        return previousProcess, processes

    def FIFO(processes, config=[]):
        process = processes[0].split(",")
        processes.pop(0)
        return process, processes

    def Round_Robin(processes, config=[]):
        process = processes[0].split(",")
        processTime = int(process[config[1]])
        if (processTime > config[3]):
            process[config[1]] = config[3]
            processes.append(
                f"{process[0]},{process[1]},{processTime - config[3]}")
        processes.pop(0)
        return process, processes

    def get_id_treeview(self, column):
        positions = [256, 16, 1]
        letter = ["A", "B", "C", "D", "E", "F"]
        id = "I"
        for position in positions:
            result = int(column / position)
            if result > 0:
                id += str(result) if result < 10 else letter[int(result-10)]
                column -= (position * result)
            else:
                id += "0"
        return id

    def add_process(self, list, name, priority, time, position):
            new_process = name + ", " + priority + ", " + time
            if position == "Inicio":
                list.insert(0, new_process)
            else:
                list.append(new_process)
    
            return list


class interface(customtkinter.CTk):
    def __init__(self, list_process):
        super().__init__()
        self.title("Planificadores")
        self.geometry("600x340")
        self.algorithm = scheduling_algorithm()
        self.list = list_process

        self.tabview = customtkinter.CTkTabview(
            self, width=590, height=330, anchor="nw")
        self.tabview.pack()
        self.tabview.add("          Inicio          ")
        self.tabview.add("          Agregar         ")

        # ================= COMPONENTES DE INICIO ==================
            # ================= COMPONENTES PRIMER FRAME ==================
        self.frameProcess = customtkinter.CTkFrame(
            self.tabview.tab("          Inicio          "),
            width=540,
            height=60,
            border_width=1, border_color="white")
        self.frameProcess.place(x=20, y=5)

        self.currentNameProcess = customtkinter.CTkLabel(
            self.frameProcess,
            text="Proceso Actual"
        )
        self.currentNameProcess.place(x=10, y=16)

        self.pbrProcess = customtkinter.CTkProgressBar(
            self.frameProcess, orientation="horizontal", width=200, height=16, corner_radius=5)
        self.pbrProcess.place(x=130, y=22)
        self.pbrProcess.set(0)

        self.optionMenuAlgorithm = customtkinter.CTkOptionMenu(
            self.tabview.tab("          Inicio          "),
            values=["SJF", "Priority", "FIFO", "Round_Robin"],
            height=25,
            width=130
        )
        self.optionMenuAlgorithm.place(x=360, y=22)

        self.buttonStart = customtkinter.CTkButton(
            self.tabview.tab("          Inicio          "),
            text="Iniciar",
            command=self.start,
            height=25,
            width=50
        )
        self.buttonStart.place(x=500, y=22)

            # ================= COMPONENTES SEGUNDO FRAME ==================

        self.frameLabel = customtkinter.CTkFrame(
            self.tabview.tab("          Inicio          "),
            width=260,
            height=204,
            border_width=1, border_color="white")
        self.frameLabel.place(x=20, y=70)

        self.lblProcess = customtkinter.CTkLabel(
            self.frameLabel,
            text="Proceso: "
        )
        self.lblProcess.place(x=20, y=20)

        self.lblPriority = customtkinter.CTkLabel(
            self.frameLabel,
            text="Prioridad: "
        )
        self.lblPriority.place(x=20, y=50)

        self.lblTime = customtkinter.CTkLabel(
            self.frameLabel,
            text="Tiempo: "
        )
        self.lblTime.place(x=20, y=80)

        # ================= COMPONENTES TABLE ==================
        self.table = ttk.Treeview(
            self.tabview.tab("          Inicio          "),
            height=14,
            columns=("col1")
        )
        self.table.column("#0", width=205)
        self.table.column("col1", width=205, anchor="center")

        self.table.heading("#0", text="Proceso", anchor="center")
        self.table.heading("col1", text="Esatdo", anchor="center")
        self.table.place(x=430, y=105)

        # ================= COMPONENTES DE AGREGAR ==================
        customtkinter.CTkLabel(
            self.tabview.tab("          Agregar         "),
            text="Nombre del proceso"
        ).place(x=10, y=10)
        self.txtProcess = customtkinter.CTkEntry(
            self.tabview.tab("          Agregar         "),
            width=200,
            height=25,
        )
        self.txtProcess.place(x=10, y=40)

        customtkinter.CTkLabel(
            self.tabview.tab("          Agregar         "),
            text="Prioridad"
        ).place(x=10, y=70)
        self.txtPriority = customtkinter.CTkEntry(
            self.tabview.tab("          Agregar         "),
            width=200,
            height=25,
        )
        self.txtPriority.place(x=10, y=100)

        customtkinter.CTkLabel(
            self.tabview.tab("          Agregar         "),
            text="Tiempo"
        ).place(x=10, y=130)
        self.txtTime = customtkinter.CTkEntry(
            self.tabview.tab("          Agregar         "),
            width=200,
            height=25,
        )
        self.txtTime.place(x=10, y=160)

        customtkinter.CTkLabel(
            self.tabview.tab("          Agregar         "),
            text="Posición"
        ).place(x=10, y=190)
        self.optionMenu = customtkinter.CTkOptionMenu(
            self.tabview.tab("          Agregar         "),
            values=["Inicio", "Final"],
        )
        self.optionMenu.place(x=10, y=220)

        customtkinter.CTkButton(
            self.tabview.tab("          Agregar         "),
            text="Agregar",
            command=self.add_process
        ).place(x=180, y=220)

    def add_process(self):
        self.list = self.algorithm.add_process(
            self.list,
            self.txtProcess.get(),
            self.txtPriority.get(),
            self.txtTime.get(),
            self.optionMenu.get()
        )
        self.txtProcess.delete(0, customtkinter.END)
        self.txtPriority.delete(0, customtkinter.END)
        self.txtTime.delete(0, customtkinter.END)
        self.optionMenu.set("Inicio")

    def update_label(self, name, priority, time):
        self.currentNameProcess.configure(text=name)
        self.lblProcess.configure(text=f"Nombre : {name}")
        self.lblPriority.configure(text=f"Prioridad : {priority}")
        self.lblTime.configure(text=f"Tiempo : {time}")

    def update_table(self, process, id=""):
        if id == "":
            self.table.insert(id, customtkinter.END,
                              text=process, values="Ejecutando")
        else:
            self.table.set(id, column="col1", value="Finalizado")

    def start(self):
        self.chosen_Algotithm = getattr(scheduling_algorithm, self.optionMenuAlgorithm.get())
        thread = threading.Thread(
            name="Hilo Secundario", target=self.start_process)
        thread.start()

    def start_process(self):
        self.optionMenuAlgorithm.configure(state="disabled")
        self.buttonStart.configure(state="disabled")
        flagFollow = True
        while flagFollow:
            count = 0
            process, self.list = self.chosen_Algotithm(self.list, [1, 2, False, 3])
            progress = 1/int(process[2])

            self.update_label(process[0], process[1], process[2])
            self.update_table(process[0])

            for i in range(int(process[2]) + 1):
                self.pbrProcess.set(count)
                count += progress
                self.update_idletasks()
                time.sleep(1)

            idColumn = self.algorithm.get_id_treeview(
                len(self.table.get_children()))
            self.update_table(process[0], idColumn)
            flagFollow = False if len(self.list) == 0 else True
            
        self.optionMenuAlgorithm.configure(state="normal")
        self.buttonStart.configure(state="normal")

if __name__ == "__main__":
    with open("Planificadores/procesos.txt", "r") as file:
        file = file.readlines()

    app = interface(file)

    app.mainloop()

