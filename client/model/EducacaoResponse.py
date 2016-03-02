#!/usr/bin/env python


class EducacaoResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'ano': 'int',
            'codigo_regiao': 'int',
            'descricao_regiao': 'str',
            'escala_grupo': 'str',
            'regime': 'str',
            'nome_unidade_escolar': 'str',
            'bairro': 'str',
            'descricao': 'str'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'ano': 'ano',
            'codigo_regiao': 'codigoRegiao',
            'descricao_regiao': 'descricaoRegiao',
            'escala_grupo': 'escalaGrupo',
            'regime': 'regime',
            'nome_unidade_escolar': 'nomeUnidadeEscolar',
            'bairro': 'bairro',
            'descricao': 'descricao'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #Ano do registro.
        
        self.ano = None # int
        
        #CÃ³digo da regiÃ£o.
        
        self.codigo_regiao = None # int
        
        #DescriÃ§Ã£o da regiÃ£o.
        
        self.descricao_regiao = None # str
        
        #CÃ³digo do grupo escolar.
        
        self.escala_grupo = None # str
        
        #DescriÃ§Ã£o do regime escolar.
        
        self.regime = None # str
        
        #Nome da Unidade escolar.
        
        self.nome_unidade_escolar = None # str
        
        #Nome do bairro onde a unidade escolar se encontra.
        
        self.bairro = None # str
        
        #DescriÃ§Ã£o da demanda.
        
        self.descricao = None # str
        
