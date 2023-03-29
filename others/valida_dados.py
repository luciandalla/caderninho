import re

class Validador:

    @staticmethod
    def valida_nome(nome):
        if len(nome) >= 3:
            return True
        else:
            return False

    @staticmethod
    def valida_telefone(telefone):
        padrao_telefone = re.compile(r'\([0-9]{2}\)[0-9]{5}-[0-9]{4,5}')
        match = padrao_telefone.match(telefone)
        if match:
            return True
        else:
            return False

    @staticmethod
    def valida_email(email):
        padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
        match = padrao_email.match(email)
        if match:
            return True
        else:
            return False
