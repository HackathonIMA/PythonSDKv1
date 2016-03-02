#!/usr/bin/env python


class FonteDetalhadaResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'descricao': 'str',
            'codigo_grupo': 'str'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'descricao': 'descricao',
            'codigo_grupo': 'codigoGrupo'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #DescriÃ§Ã£o da fonte receita
        
        self.descricao = None # str
        
        #cÃ³digo grupo fonte receita
        
        self.codigo_grupo = None # str
        
