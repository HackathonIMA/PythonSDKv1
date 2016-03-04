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
            'descricao': 'str',
            'endereco_escola_demanda': 'str',
            'logradouro_demanda': 'str',
            'municipio_demanda': 'str',
            'uf_demanda': 'str',
            'cep_demanda': 'str',
            'demanda': 'str'
            
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
            'descricao': 'descricao',
            'endereco_escola_demanda': 'endereco_escola_demanda',
            'logradouro_demanda': 'logradouro_demanda',
            'municipio_demanda': 'municipio_demanda',
            'uf_demanda': 'uf_demanda',
            'cep_demanda': 'cep_demanda',
            'demanda': 'demanda'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #Ano do registro.
        
        self.ano = None # int
        
        #CÃ³digo da regiÃ£o.
        
        self.codigo_regiao = None # int
        
        #DescriÃ§Ã£o da regiÃ£o.
        
        self.descricao_regiao = None # str
        
        #CÃ³digo do grupo escolar (AG1: 0~1,5 anos, AG2: 1,5~3 anos, AG3: 3 ~5 anos).
        
        self.escala_grupo = None # str
        
        #DescriÃ§Ã£o do regime escolar.
        
        self.regime = None # str
        
        #Nome da Unidade escolar.
        
        self.nome_unidade_escolar = None # str
        
        #Nome do bairro onde a unidade escolar se encontra.
        
        self.bairro = None # str
        
        #DescriÃ§Ã£o da demanda.
        
        self.descricao = None # str
        
        #EndereÃ§o completo da unidade onde foi registrada a demanda.
        
        self.endereco_escola_demanda = None # str
        
        #Nome do logradouro da unidade onde foi registrada a demanda.
        
        self.logradouro_demanda = None # str
        
        #Nome do municÃ­pio da unidade onde foi registrada a demanda. (sempre Campinas)
        
        self.municipio_demanda = None # str
        
        #Sigla da unidade federativa do cadastro da demanda (sempre SP)
        
        self.uf_demanda = None # str
        
        #CEP registrado do endereÃ§o da unidade onde foi registrada a demanda.
        
        self.cep_demanda = None # str
        
        #Quantidade total do registro da demanda. Cada registro do webservice traz a tipificaÃ§Ã£o da demanda e este campo mostra os valores consolidados totais para a demanda.
        
        self.demanda = None # str
        
