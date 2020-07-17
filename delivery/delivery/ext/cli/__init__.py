from flask import Flask
from delivery.ext.db import db

def init_app(app: Flask):

    @app.cli.command()
    def create_db():
        """
            Este comando inicia o Banco de Dados
        """    
        try:
            db.create_all()

            a = 0/0

        except Exception as e:
            print("Não foi possível criar o Banco de Dados")

            with open('./Erros.txt', 'w') as err:
                err.write(f'{e}')
                print(f'Por favor, veja as informações de erro no arquivo {err}')



    @app.cli.command()
    def listar_pedidos():
        lista_de_pedidos = ['Pedido1', 'Pedido2', 'Pedido3']
        return lista_de_pedidos


    @app.cli.command()
    def listar_usuarios():
        lista_de_usuarios = ['Usuário1', 'Usuário2', 'Usuário3']
        return lista_de_usuarios

