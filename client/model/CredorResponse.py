#!/usr/bin/env python


class CredorResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'descricao': 'str',
            'municipio_descricao': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'descricao': 'descricao',
            'municipio_descricao': 'municipioDescricao'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #Descricao do credor
        
        self.descricao = None # str
        
        #Municipio do credor
        
        self.municipio_descricao = None # str
        
