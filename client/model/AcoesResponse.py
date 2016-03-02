#!/usr/bin/env python


class AcoesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'nome': 'str',
            'descricao': 'int',
            'numero': 'str'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'nome': 'nome',
            'descricao': 'descricao',
            'numero': 'numero'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #Nome da aÃ§Ã£o
        
        self.nome = None # str
        
        #DescriÃ§Ã£o da aÃ§Ã£o
        
        self.descricao = None # int
        
        #Numero da aÃ§Ã£o
        
        self.numero = None # str
        
