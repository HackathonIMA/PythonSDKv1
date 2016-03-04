#!/usr/bin/env python


class FonteDetalhadaResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'descricao': 'str',
            'codigo_grupo': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'descricao': 'descricao',
            'codigo_grupo': 'codigoGrupo'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #DescriÃ§Ã£o da fonte receita
        
        self.descricao = None # str
        
        #cÃ³digo grupo fonte receita
        
        self.codigo_grupo = None # str
        
