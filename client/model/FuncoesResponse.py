#!/usr/bin/env python


class FuncoesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'descricao': 'str'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'descricao': 'descricao'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #DescriÃ§Ã£o da funÃ§Ã£o
        
        self.descricao = None # str
        
