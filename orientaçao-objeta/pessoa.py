# Definindo a classe Pessoa 
class Pessoa: 
    def __init__(self, nome, idade): 
        self.nome = nome 
        self.idade = idade 

# Importando as outras classes 
from endereco import endereco 
from contato import Contato
from dados_pessoais import DadosPessoais 
from escolaridade import escolaridade 
from portfolio import portfolio 
