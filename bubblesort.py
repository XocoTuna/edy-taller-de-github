def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            break
        #no se como se hacen los comentarios en python
        #a ya vi como

        #Pero ya fuera de todo concepto imaginable, francamente los cuchillos si es el mejor cubierto
