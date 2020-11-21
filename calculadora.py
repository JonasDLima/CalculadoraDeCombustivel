from operator import itemgetter


class Calculadora:
    __distancia_a_percorrer: float
    __consumo_por_litro: int
    __tipos_de_combustivel: dict = {
        'Álcool': 2.74,
        'Díesel': 3.24,
        'Gasolina': 4.17
    }

    def __init__(self, distancia_a_percorrer, consumo_por_litro):
        self.__distancia_a_percorrer = float(distancia_a_percorrer)
        self.__consumo_por_litro = int(consumo_por_litro)

    def calcular_combustivel_necessario_para_viagem(self):
        combustivel_necessario_para_viagem = self.__distancia_a_percorrer / self.__consumo_por_litro

        return combustivel_necessario_para_viagem

    def calcular_valor_necessario_para_combustivel(self, combustivel_necessario_para_viagem):
        valor_necessario_para_combustivel = {

        }

        for tipo, val in self.__tipos_de_combustivel.items():
            valor_necessario_para_combustivel[tipo] = combustivel_necessario_para_viagem * val

        sorted(valor_necessario_para_combustivel.items(), key=itemgetter(1), reverse=True)

        return valor_necessario_para_combustivel
