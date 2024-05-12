vinhos = [
    {"nome": "Vinho 1", "preco": 45},
    {"nome": "Vinho 2", "preco": 50},
    {"nome": "Vinho 3", "preco": 55},
    {"nome": "Vinho 4", "preco": 60},
]

print(list(filter(lambda v: v["preco"] > 50, vinhos)))
