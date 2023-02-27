import re

class Cliente:

    def __init__(self, nome, telefone, email):

        if self._valida_nome(nome) and self._valida_telefone(telefone) and self._valida_email(email):
            self._nome = nome.upper()
            self._email = email.upper()
            self._telefone = telefone

    def __str__(self):
        return f"Nome: {self._nome} - Telefone: {self._telefone} - E-mail: {self._email}"

    def _valida_nome(self, nome):
        if len(nome) >= 3:
            return True
        else:
            raise ValueError("O nome deve possuir mais de 3 caracteres!")

    def _valida_email(self, email):
        padrao_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+')
        match = padrao_email.match(email)
        if match:
            return True
        else:
            raise ValueError("O email digitado é inválido!")

    def _valida_telefone(self, telefone):
        if 10 <= len(telefone) <= 11:
            return True
        else:
            raise ValueError("O telefone informado é inválido! Seguir padrão DDD+Número!")
