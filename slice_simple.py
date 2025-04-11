def slice_simple():
    texto = "Awesome"
    print(texto[0:3].lower())
    print(texto[2:5].lower())
    print(texto[0:5].lower()+texto[5:7].lower())


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
