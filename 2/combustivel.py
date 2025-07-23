distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = round(distancia_percorrida / combustivel_gasto, 2)

print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")