#!/usr/bin/env python


class ProjetoAtividadeResponse:

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
        
        #descriÃ§Ã£o do projeto atividade
        
        self.descricao = None # str
        
