import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# puntos del usuario
puntos = 0

questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)


# El usuario deberá contestar 3 preguntas
for question, answer, correct_answer_index in questions_to_ask:

    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = int(input("Respuesta: "))

        # punto7a
        if user_answer not in [0, 1, 2, 3]:
            print("Respuesta no válida")
            exit(1)
        else:
            user_answer = int (user_answer) - 1

        

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer_index:
            print("¡Correcto!")
            puntos += 1  # si es correcta suma 
            break
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(correct_answer_index + 1)
        puntos -= 0.5 # si es incorrecta resta

    # Se imprime un blanco al final de la pregunta
    print()
# imprime la cantidad total de puntos del usuario
print(f"el usuario tiene {puntos} puntos")