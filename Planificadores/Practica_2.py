import time

class scheduling_algorithm:

    def SJF(self, processes, position):
        previousTime = 0
        for process in processes:
            acurrentProcess = process.split(",")
            acurrentTime = int(acurrentProcess[position])
            if ((acurrentTime < previousTime) or (previousTime == 0)):
                previousTime = acurrentTime
                previousProcess = acurrentProcess

        processes.remove((",".join(previousProcess)))
        return previousProcess, processes

    def Priority(self, processes, position, descending_priority=False):
        firstIterationFlag = True
        previousPriority = 0
        for process in processes:
            acurrentProcess = process.split(",")
            acurrentPriority = int(acurrentProcess[position])
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

    def FIFO(self, processes):
        process = processes[0].split(",")
        processes.pop(0)
        return process, processes

    def Round_Robin(self, processes, quantum, positionTime):
        process = processes[0].split(",")
        processTime = int(process[positionTime])
        if (processTime > quantum):
            process[positionTime] = quantum
            processes.append(f"{process[0]},{process[1]},{processTime-quantum}")
        processes.pop(0)
        return process, processes

    def Simulation(self, list_process):
        flagFollow = True
        anchor_col = 20
        progress = ""
        print(f"{'Nombre':<{anchor_col}} {'Prioridad':<{anchor_col}} {'Tiempo':<{anchor_col}}")
        print("-" * (anchor_col * 3 + 2))

        while flagFollow:
            process, list_process = self.Round_Robin(list_process, 3, 2)

            for countTime in range(int(process[2])):
                progress += "="
                time.sleep(1)

            print(f"{process[0]:<{anchor_col}} {process[1]:<{anchor_col}} {progress:<{anchor_col}}")
            progress = ""
            flagFollow = False if len(list_process) == 0 else True


if __name__ == "__main__":
    with open("Planificadores/procesos.txt", "r") as file:
        file = file.readlines()

    algorithm = scheduling_algorithm()
    algorithm.Simulation(file)
