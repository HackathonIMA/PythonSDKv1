#!/usr/bin/env python


class ReceitaResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'ano_mes_emissao': 'int',
            'codigo_origem_recurso': 'str',
            'valor_previsao': 'str',
            'valor_previsao_inicial': 'str',
            'valor_previsao_adicional': 'str',
            'valor_previsao_deducao': 'str',
            'valor_previsao_anulacao': 'str',
            'valor_realizado': 'str',
            'valor_realizado_deduzido': 'str',
            'valor_a_realizar': 'str',
            'valor_a_realizar_deduzido': 'str',
            'valor_previsao_acrescimo': 'str',
            'valor_previsao_inicial_acrescimo': 'str',
            'valor_previsao_adicional_acrescimo': 'str',
            'valor_previsao_deducao_acrescimo': 'str',
            'valor_previsao_anulacao_acrescimo': 'str',
            'valor_realizado_acrescimo': 'str',
            'valor_realizado_deduzido_acrescimo': 'str',
            'valor_a_realizar_acrescimo': 'str',
            'valor_a_realizar_deduzido_acrescimo': 'str'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'ano_mes_emissao': 'anoMesEmissao',
            'codigo_origem_recurso': 'codigoOrigemRecurso',
            'valor_previsao': 'valorPrevisao',
            'valor_previsao_inicial': 'valorPrevisaoInicial',
            'valor_previsao_adicional': 'valorPrevisaoAdicional',
            'valor_previsao_deducao': 'valorPrevisaoDeducao',
            'valor_previsao_anulacao': 'valorPrevisaoAnulacao',
            'valor_realizado': 'valorRealizado',
            'valor_realizado_deduzido': 'valorRealizadoDeduzido',
            'valor_a_realizar': 'valorARealizar',
            'valor_a_realizar_deduzido': 'valorARealizarDeduzido',
            'valor_previsao_acrescimo': 'valorPrevisaoAcrescimo',
            'valor_previsao_inicial_acrescimo': 'valorPrevisaoInicialAcrescimo',
            'valor_previsao_adicional_acrescimo': 'valorPrevisaoAdicionalAcrescimo',
            'valor_previsao_deducao_acrescimo': 'valorPrevisaoDeducaoAcrescimo',
            'valor_previsao_anulacao_acrescimo': 'valorPrevisaoAnulacaoAcrescimo',
            'valor_realizado_acrescimo': 'valorRealizadoAcrescimo',
            'valor_realizado_deduzido_acrescimo': 'valorRealizadoDeduzidoAcrescimo',
            'valor_a_realizar_acrescimo': 'valorARealizarAcrescimo',
            'valor_a_realizar_deduzido_acrescimo': 'valorARealizarDeduzidoAcrescimo'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #Ano e MÃªs da EmissÃ£o de Receita
        
        self.ano_mes_emissao = None # int
        
        #CÃ³digo da Origem do Recurso
        
        self.codigo_origem_recurso = None # str
        
        #Valor Prevista da receita
        
        self.valor_previsao = None # str
        
        #Valor de previsÃ£o inicial da Receita
        
        self.valor_previsao_inicial = None # str
        
        #Valor de previsÃ£o adicicional da receita
        
        self.valor_previsao_adicional = None # str
        
        #Valor de DeduÃ§Ã£o previsto da receita
        
        self.valor_previsao_deducao = None # str
        
        #valor de AnulaÃ§Ã£o previsto da receita
        
        self.valor_previsao_anulacao = None # str
        
        #Valor Realizado da receita
        
        self.valor_realizado = None # str
        
        #Valor Realizado Deduzido da Receita
        
        self.valor_realizado_deduzido = None # str
        
        #Valor a Realizar da Receita
        
        self.valor_a_realizar = None # str
        
        #Valor a Realizar deduzido da Receita
        
        self.valor_a_realizar_deduzido = None # str
        
        #Valor de AcrÃ©scimo previsto da receita
        
        self.valor_previsao_acrescimo = None # str
        
        #Valor de acrÃ©scimo previsto inicialmente da receita
        
        self.valor_previsao_inicial_acrescimo = None # str
        
        #Valor de AcrÃ©cimo Adicional previsto da receita
        
        self.valor_previsao_adicional_acrescimo = None # str
        
        #Valor de AcrÃ©scimo deduzido previsto da receita
        
        self.valor_previsao_deducao_acrescimo = None # str
        
        #Valor de Acrescimo anulado previsto da receita
        
        self.valor_previsao_anulacao_acrescimo = None # str
        
        #Valor de Acrescimo realizado da receita
        
        self.valor_realizado_acrescimo = None # str
        
        #Valor de Acrescimo deduzido realizado da receita
        
        self.valor_realizado_deduzido_acrescimo = None # str
        
        #Valor de Acrescimo a realizar da receita
        
        self.valor_a_realizar_acrescimo = None # str
        
        #Valor de Acrescimo deduzido a realizar da receita
        
        self.valor_a_realizar_deduzido_acrescimo = None # str
        
