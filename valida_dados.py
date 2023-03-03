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
        if 10 <= len(telefone) <= 11:
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
