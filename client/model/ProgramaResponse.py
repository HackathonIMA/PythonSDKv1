#!/usr/bin/env python


class ProgramaResponse:

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
        
        #Descricao do Programa
        
        self.descricao = None # str
        
