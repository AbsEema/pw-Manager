import random
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Genera una password aleatoria segun los criterios indicados.

    Args:
        leght: longitud de la password minimo 8
        use_upper: incluir mayuscula (A-Z)
        use_lower: incluir minusculas (a-z)
        use_digits: incluir numeros (0-9)
        use_symbols: incluir simboloes (!@#$% etc.)

    Returns:
        str: Password generada, o None si no se selecciono ningun tipo
    """
    if length < 8:
        length = 8

    chars = ""
    if use_upper:
        chars +=string.ascii_uppercase
    if use_lower:
        chars +=string.ascii_lowercase
    if use_digits:
        chars +=string.digits
    if use_symbols:
        chars +="!@#$%^&*()-_=+[]{}|;:,.<>?"

    if not chars:
        return None

    #Garantizar al menos un caracter de cada tipo seleccionado
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    #Completar el resto de la longitud
    remaining = length - len(password)
    password += random.choices(chars, k=remaining)

    #Mezclar para que no siempre empiece igual
    random.shuffle(password)
    return"".join(password)