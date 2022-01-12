class Imc:
    def __init__(self, altura, peso):
        if altura == '' or  peso == '':
            raise ValueError('Preencha as informações necessárias')
        else:
            self.__imc = round(float(peso) / float(altura)**2, 2)
        self.__classificacao = self.classifica_imc(self.__imc)
    

    @staticmethod
    def classifica_imc(imc):
        if imc < 16:
            return 'Magreza grau III'
        if 16 <= imc <= 16.9:
            return 'Magreza grau II'
        if 17 <= imc <= 18.4:
            return 'Magreza grau I'
        if 18.5 <= imc <= 24.9:
            return 'Adequado'
        if 25 <= imc <= 29.9:
            return 'Pré-obeso'
        if 30 <= imc <= 34.9:
            return 'Obesidade grau I'
        if 35 <= imc <= 39.9:
            return 'Obesidade grau II'
        else:
            return 'Obesidade grau III'
    
    @property
    def imc(self):
        return self.__imc
    

    @property
    def classificacao(self):
        return self.__classificacao