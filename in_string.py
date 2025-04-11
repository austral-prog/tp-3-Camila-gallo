def check_vowels():
    # Código a implementar utilizando input.
    nombre= str(input().lower())
    contA=str("a" in nombre)
    contE=str("e" in nombre)
    contI=str("i" in nombre)
    contO=str("o" in nombre)
    contU=str("u" in nombre)
    print("Contiene a: "+ contA)
    print('Contiene e: '+ contE)
    print('Contiene i: '+ contI)
    print('Contiene o: '+ contO)
    print('Contiene u: '+ contU)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
