from validate_docbr import CPF, CNPJ
class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("NENHUM TIPO DE DOCUMENTO VÁLIDO.")

class DocCpf:
    def __init__(self):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF INVÁLIDO!")

    def __str__(self):
        return f'CPF: {self.format()}'

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ NÃO É VÁLIDO!")

    def __str__(self):
        return f'CNPJ: {self.format_cnpj()}'

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)




class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        # Chamando o CPF
        if self.tipo_documento == "cpf":
            #validando o CPF
            # se for verdadeiro
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            # se for falso
            else:
                raise ValueError("CPF inválido!")

        # Chamando o CNPJ
        # se for verdadeiro
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
        # se for falso
            else:
                raise ValueError("CNPJ inválido!")

        # Chamando nenhum documento = não foi colocado nada
        else:
            raise ValueError("Documento inválido!")

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format_cpf()

    def __str__(self):
        if self.tipo_documento == 'cpf':
            return f'CPF: {self.format_cpf()}'
        elif self.tipo_documento == 'cnpj':
            return f'CNPJ: {self.format_cnpj()}'

    def cnpj_eh_Valido(self, cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!")

documento = CpfCnpj('60338384324', 'cpf')
print(documento)

documentoCNPJ = CpfCnpj('49803521000176', 'cnpj')
print(documentoCNPJ)
