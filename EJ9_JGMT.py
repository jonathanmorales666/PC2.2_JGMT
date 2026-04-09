# Jonathan Gabriel Morales Torres
# Ejercicio Final de Operadores
# Datos del estudiante ingresados por el sistema
nombre_estudiante = "Jonathan Morales"
promedio = 60
matricula_pagada = True
activo = True

# Datos institucionales
estudiante_registrado = nombre_estudiante
registro_official = nombre_estudiante  # misma referencia
alumnos_autorizados = ["Carlos", "Daniel", "Oscar"]

# Validaciones
promedio_valido = promedio >= 75
estado_valido = matricula_pagada and activo
mismo_registro = estudiante_registrado is registro_official
autorizado = nombre_estudiante in alumnos_autorizados

# Resultados
print("Promedio válido:", promedio_valido)
print("Estado de cuenta y activo:", estado_valido)
print("¿Es el mismo registro oficial?", mismo_registro)
print("¿Está en la lista de autorizados?", autorizado)

# Validación final combinada
puede_presentar_examen = promedio_valido and estado_valido and mismo_registro and autorizado
print("¿Puede presentar el examen final?", puede_presentar_examen)
