import re

class Validar():
    def __init__(self, CPF):
        self.CPF = str(CPF)
        self.validaCPF()
        self.formatacao()


    def __len__(self):
        return len(self.CPF)

    def validaCPF(self):
        CPF_valido = re.findall(r'\w{3}\.\w{3}\.\w{3}\-\w{2}', self.CPF)
        if CPF_valido or len(self.CPF) == 11:
            print('CPF Válido')
        else:
            print('CPF Inválido')

    def formatacao (self):
        if len(self.CPF) == 11:
            print(f'{self.CPF[:3]}.{self.CPF[3:6]}.{self.CPF[6:9]}-{self.CPF[9:]}')
        else:
            print(self.CPF)
