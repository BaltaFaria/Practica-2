import random

questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
#Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
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

correct_answers_index = [1, 2, 0, 3, 1]
puntos = 0

for i in range(3):
    
    question_index = random.randint(0, len(questions) - 1)

    
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

   
    for intento in range(2):
        user_answer = int(input("Respuesta: ")) - 1
        
        #if user_answer != 1 or user_answer != 2 or user_answer != 3 or user_answer != 0:
        if user_answer not in [0, 1, 2, 3]:
            print("respuesta incorrecta")   
            exit(1)
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            puntos += 1
            break
    else:
       
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])
        puntos -= 0.5
    
    print()
print("los puntos son: ",puntos)    