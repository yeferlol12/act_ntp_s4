def gestionar_calificaciones():
    calificaciones = []
    
    while True:
        entrada = input("Ingresa una calificación (o 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        calificaciones.append(float(entrada))
    
    if len(calificaciones) > 0:
        promedio = sum(calificaciones) / len(calificaciones)
        nota_max = max(calificaciones)
        nota_min = min(calificaciones)
        
        print("Promedio:", promedio)
        print("Nota más alta:", nota_max)
        print("Nota más baja:", nota_min)
    else:
        print("No ingresaste ninguna calificación.")

gestionar_calificaciones()