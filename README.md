# Sistemas Operativos

Este repositorio contiene las practicas desarrolladas durante la materia de Sistemas Operativos.

## Introducción a Java

Esta carpeta reúne las primeras prácticas realizadas para familiarizarse con la sintaxis básica del lenguaje Java.

#### Practicas
- Calcular área
- Conversor de temperaturas

## Planificador FCFS

Se implementa el algoritmo First Come First Served (FCFS) para comprender el funcionamiento de la planificación de procesos.

## Planificador de Multiples Colas

Esta carpeta reúne practicas en donde se busca ejecutar varios procesos al mismo tiempo, las tecnologías utilizas son **CustomTkinter** y **threading**

### Objetivos
- Aprender a utilizar el progressbar
- Aprender a utilizar hilos

### Practica 1

Se implementa una interfaz básica con una barra de progreso cuyo objetivo es comprender el funcionamiento del widget y su actualización durante la ejecución

### Practica 2

Se implementa una interfaz con dos etiquetas que son actualizadas desde un hilo independiente para comprender el uso de la librería **threading** en aplicaciones con interfaz

### Practica 3

Se implementa una interfaz con tres barras de progreso, cada una controlada por un hilo independiente, simulando la ejecución concurrente de multiples procesos.

## Planificadores

Estas practicas consisten en la simulación de diferentes algoritmos de planificación de procesos utilizados por los sistemas operativos. la aplicación permite visualizar la ejecución de los procesos mediante una interfaz gráfica desarrollada con **CustomTkinter**

### Objetivos
- Comprender el funcionamiento de los algoritmos de planificación
- Representar visualmente la ejecución de procesos

### Practica 1

Se diseño la interfaz grafica, en donde se puede observar información sobre el proceso, al igual un apartado en donde se pueden registrar nuevos procesos y se implemento el algoritmo SJF.

### Practica 2

Se implementaron los algoritmos FCFS, SJF, Prioridad y Round Robin sin interfaz grafica para validar su funcionamiento y se muestra su funcionamiento desde la consola.

### Practica 3

Se reutiliza las practicas anteriores, en la interfaz se implementa la elección del planificador que se desea utilizar, en el agregar un nuevo proceso ahora se pregunta si se agregara al final de la lista o al inicio, además se realizaron mejoras a la clase **scheduling_algorithm**
