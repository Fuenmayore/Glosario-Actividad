import multiprocessing


def worker(num, queue):
    result = num * num # Calcular el cuadrado del número
    queue.put((num, result))  

def main():
    # Pedir al usuario que ingrese una lista de números
    numbers = input("Ingrese una lista de números separados por comas: ")
    numbers = [int(x) for x in numbers.split(',')]

   
    queue = multiprocessing.Queue()

    # Crear y comenzar los procesos esclavos
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=worker, args=(num, queue))
        processes.append(p)
        p.start()

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    # Recoger los resultados
    results = []
    while not queue.empty():
        results.append(queue.get())

    # Mostrar resultados
    print("Resultados:")
    for num, result in results:
        print(f"El cuadrado de {num} es {result}")

if __name__ == "__main__":
    main()
