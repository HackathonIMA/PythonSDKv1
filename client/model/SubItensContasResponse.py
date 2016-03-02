#!/usr/bin/env python


class SubItensContasResponse:

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
        
        #DescriÃ§Ã£o do SubItem de Despesa
        
        self.descricao = None # str
        
