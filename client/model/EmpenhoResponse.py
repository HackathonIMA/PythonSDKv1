#!/usr/bin/env python


class EmpenhoResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'codigo_funcao': 'int',
            'processo': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'codigo_funcao': 'codigoFuncao',
            'processo': 'processo'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #CÃ³digo da funcao
        
        self.codigo_funcao = None # int
        
        #Procesos de compra
        
        self.processo = None # str
        
