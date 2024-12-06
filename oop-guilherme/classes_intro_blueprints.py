class Pessoa:
    def __init__(self, nome, n_utilizador):
        self.nome = nome
        self.n_utilizador = n_utilizador
       
  #diz no terminal o nome utilizador e o seu numero
    def saudacao(self):
        return f"Olá {self.nome} {self.n_utilizador}, bem-vindo de volta."
 
 
class Camera:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
  #diz no terminal a  marca e o modelo
    def informacao_de_stock_da_camera(self):
        return f"A camera {self.marca} {self.modelo} nao esta disponivel no stock."

class Stock:
    def __init__(self, cameras_modelos, alarmes_modelos):
        self.cameras_modelos = cameras_modelos
        self.alarmes_modelos = alarmes_modelos
    
    def informacao_de_stock(self):
        return f'''quantidade de modelos de cameras em stock: {self.cameras_modelos}
quantidade de modelos de alarmes em stock: {self.alarmes_modelos}'''

class Vendas:
    def __init__(self, n_de_vendas_cameras, n_de_vendas_alarmes, n_de_vendas_total):
        self.nº_de_vendas_cameras = n_de_vendas_cameras
        self.nº_de_vendas_alarmes = n_de_vendas_alarmes
        self.nº_de_vendas_total = n_de_vendas_total

    def soma_vendas(self, n_de_vendas_cameras, n_de_vendas_alarmes):
        return n_de_vendas_cameras + n_de_vendas_alarmes    
    
    def informacao_de_vendas(self):
        return f'''nº de vendas cameras: {self.nº_de_vendas_cameras}
nº de vendas alarmes: {self.nº_de_vendas_alarmes}
nº de vendas total: {self.nº_de_vendas_total}'''