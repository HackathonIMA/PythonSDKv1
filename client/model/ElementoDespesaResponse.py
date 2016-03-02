#!/usr/bin/env python


class ElementoDespesaResponse:

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
        
        #descriÃ§Ã£o do elemento de despesa
        
        self.descricao = None # str
        
