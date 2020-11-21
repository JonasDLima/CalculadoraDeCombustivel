distancia_a_percorrer = float(input('Distância em quilômetros a ser percorrida \n'))
consumo_por_litro = int(input('Consumo de combustível do veículo (km/l) \n'))

tipos_de_combustivel = {
    'Álcool': 2.74,
    'Díesel': 3.24,
    'Gasolina': 4.17
}

combustivel_necessario_para_viagem = distancia_a_percorrer / consumo_por_litro

valor_necessario_para_combustivel = {

}

for tipo, val in tipos_de_combustivel.items():
    valor_necessario_para_combustivel[tipo] = combustivel_necessario_para_viagem * val

for tipo, val in valor_necessario_para_combustivel.items():
    print(f'{tipo}:{val:.2f}')
