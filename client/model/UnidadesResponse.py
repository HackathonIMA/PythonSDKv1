#!/usr/bin/env python


class UnidadesResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'descricao': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'descricao': 'descricao'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #DescriÃ§Ã£o da unidade
        
        self.descricao = None # str
        
