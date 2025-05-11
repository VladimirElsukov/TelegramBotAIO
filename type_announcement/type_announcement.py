# Пример когда без анотации типов, мы не видим явной подсказки от IDE
# def multiplying_a_string(number, word):
#     word = word.
#     return(word*number)


# Явное указание анотации типов и сразу видим подсказку
def multiplying_a_string(number: int, word: str) -> str:
    word = word.capitalize
    return(word*number)