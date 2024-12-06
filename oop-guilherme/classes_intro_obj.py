from classes_intro_blueprints import Pessoa
from classes_intro_blueprints import Camera
from classes_intro_blueprints import Stock
from classes_intro_blueprints import Vendas

 #importar classes
 
pessoa = Pessoa("Utilizador", 9843)
camera = Camera("hikvision", "4MP DeepinView ANPR Moto Varifocal Bullet Camera")
stock = Stock(293, 352)
vendas = Vendas(642, 854, 222)
 
#print(pessoa.saudacao())
#print(camera.informacao_de_stock_da_camera())
#print(stock.informacao_de_stock())

print(vendas.soma_vendas)