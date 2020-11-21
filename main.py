from calculadora import Calculadora


'''
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
'''


def main():

    print(f'\n'
          f'                    Essa aplicação tem como finalidade demonstrar os valores que serão gastos \n'
          f'                    com combustível durante uma viagem, com base no consumo de seu veículo, e \n'
          f'                    com a distância determinada por você! \n'
          f'\n'
          f'Os combustíveis disponíveis para esse cálculo são: \n'
          f'        º Álcool \n'
          f'        º Díesel \n'
          f'        º Gasolina \n')

    calc = Calculadora(
        input('Distância em quilômetros a ser percorrida \n'),
        input('Consumo de combustível do veículo (km/l) \n')
    )

    combustivel_necessario_para_viagem = calc.calcular_combustivel_necessario_para_viagem()

    valor_necessario_para_combustivel = calc.calcular_valor_necessario_para_combustivel(
        combustivel_necessario_para_viagem)

    print(f'                    O valor total gasto será de: \n')

    for tipo, val in valor_necessario_para_combustivel.items():
        print(f'                    {tipo}:{val:.2f}')


if __name__ == '__main__':
    main()
