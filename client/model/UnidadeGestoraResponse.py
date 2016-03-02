#!/usr/bin/env python


class UnidadeGestoraResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'descricao': 'str',
            'gestao': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'descricao': 'descricao',
            'gestao': 'gestao'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #DescriÃ§Ã£o da Unidade Gestora
        
        self.descricao = None # str
        
        #DescriÃ§Ã£o do tipo de gestÃ£o  ou CÃ³digo do tipo de GestÃ£o
        
        self.gestao = None # str
        
