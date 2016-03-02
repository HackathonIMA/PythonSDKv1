#!/usr/bin/env python


class TipoLicitacoesResponse:

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
        
        #DescriÃ§Ã£o do Tipo de LicitaÃ§Ã£o
        
        self.descricao = None # str
        
