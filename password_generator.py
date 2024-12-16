#Importamos la libreria de los regex
import re 
#Importamos la  libreria de secrets que selecciona caracteres random, mas seguro para los procesos de encriptacion y de creacion de contraseñas
import secrets
#Importamos la libreria de strings 
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters to create a single variable
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            #Vamos añadiendo uno a uno
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        #La función all() evalúa si todas las expresiones dentro de un iterable son True. Si alguna es False, devuelve False.
        if all(
            #Having all([expression for i in iterable]), means that a new list is created by evaluating expression for each i in iterable. 
            # After the all() function iterates over the newly created list, the list is deleted automatically, 
            # since it is no longer needed.Memory can be saved by using a generator expression. 
            # Generator expressions follow the syntax of list comprehensions but they use parentheses instead of square brackets.

            #Hacemos una comparacion, si el numero de coincidencias es menor al de las constrains, el ciclo vuelve a iniciar
            #creando una nueva contraseña
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password


##llamamos a la funcion
#El condicional es para que, en caso de ser importado, no se corra automaticamente hasta que se indique
if __name__=='__main__':
    new_password = generate_password()
    print('Generated password:', new_password)