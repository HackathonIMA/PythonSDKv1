#!/usr/bin/env python


class DespesasResponse:

    def __init__(self):
        self.swaggerTypes = {
            'links': 'list[LinksModel]',
            'id': 'str',
            'ano_mes_emissao': 'int',
            'dia_lancamento': 'int',
            'dia_vencimento': 'int',
            'nota_empenho': 'str',
            'processo_descricao': 'str',
            'valor_empenho': 'int',
            'valor_liquidado': 'int',
            'valor_a_liquidar': 'int',
            'valor_pago': 'int',
            'valor_a_pagar': 'int',
            'valor_acrescimo_empenho': 'int',
            'valor_acrescimo_liquidado': 'int',
            'valor_acrescimo_a_liquidar': 'int',
            'valor_acrescimo_pago': 'int',
            'valor_acrescimo_a_pagar': 'int'
            
        }

        self.attributeMap = {
            'links': 'links',
            'id': 'ID',
            'ano_mes_emissao': 'anoMesEmissao',
            'dia_lancamento': 'diaLancamento',
            'dia_vencimento': 'diaVencimento',
            'nota_empenho': 'notaEmpenho',
            'processo_descricao': 'processoDescricao',
            'valor_empenho': 'valorEmpenho',
            'valor_liquidado': 'valorLiquidado',
            'valor_a_liquidar': 'valorALiquidar',
            'valor_pago': 'valorPago',
            'valor_a_pagar': 'valorAPagar',
            'valor_acrescimo_empenho': 'valorAcrescimoEmpenho',
            'valor_acrescimo_liquidado': 'valorAcrescimoLiquidado',
            'valor_acrescimo_a_liquidar': 'valorAcrescimoALiquidar',
            'valor_acrescimo_pago': 'valorAcrescimoPago',
            'valor_acrescimo_a_pagar': 'valorAcrescimoAPagar'
            
        }

        
        
        self.links = None # list[LinksModel]
        
        #Identificador do registro.
        
        self.id = None # str
        
        #Ano e MÃªs da EmissÃ£o da Nota de Empenho
        
        self.ano_mes_emissao = None # int
        
        #Ano , Mes e Dia do LanÃ§amento da Nota de Empenho
        
        self.dia_lancamento = None # int
        
        #Ano , Mes e Dia do Vencimento da Nota de Empenho
        
        self.dia_vencimento = None # int
        
        #Numero da Nota de Empenho
        
        self.nota_empenho = None # str
        
        #Numero do Processo de Compra
        
        self.processo_descricao = None # str
        
        #Valor Empenhado
        
        self.valor_empenho = None # int
        
        #Valor Liquidado
        
        self.valor_liquidado = None # int
        
        #Valor a Liquidar
        
        self.valor_a_liquidar = None # int
        
        #Valor Pago
        
        self.valor_pago = None # int
        
        #Valor a Pagar
        
        self.valor_a_pagar = None # int
        
        #Valor de AcrÃ©scimo do Empenho
        
        self.valor_acrescimo_empenho = None # int
        
        #Valor de AcrÃ©scimo Liquidado
        
        self.valor_acrescimo_liquidado = None # int
        
        #Valor de AcrÃ©scimo a Liquidar
        
        self.valor_acrescimo_a_liquidar = None # int
        
        #Valor de AcrÃ©cimo Pago
        
        self.valor_acrescimo_pago = None # int
        
        #Valor de AcrÃ©scimo a Pagar
        
        self.valor_acrescimo_a_pagar = None # int
        
