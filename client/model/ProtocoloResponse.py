#!/usr/bin/env python


class ProtocoloResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'codigo_regiao': 'int',
            'nome_regiao': 'str',
            'codigo_bairro': 'int',
            'nome_bairro': 'str',
            'codigo_expediente': 'int',
            'secretaria_expediente': 'str',
            'codigo_assunto': 'int',
            'descricao_assunto': 'str',
            'ano_processo': 'int',
            'ponto_cadastramento': 'int',
            'nome_ponto_cadastramento': 'str',
            'data_cadastro': 'DateTime',
            'data_atendimento': 'DateTime',
            'data_cancelamento': 'DateTime'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'codigo_regiao': 'codigoRegiao',
            'nome_regiao': 'nomeRegiao',
            'codigo_bairro': 'codigoBairro',
            'nome_bairro': 'nomeBairro',
            'codigo_expediente': 'codigoExpediente',
            'secretaria_expediente': 'secretariaExpediente',
            'codigo_assunto': 'codigoAssunto',
            'descricao_assunto': 'descricaoAssunto',
            'ano_processo': 'anoProcesso',
            'ponto_cadastramento': 'pontoCadastramento',
            'nome_ponto_cadastramento': 'nomePontoCadastramento',
            'data_cadastro': 'dataCadastro',
            'data_atendimento': 'dataAtendimento',
            'data_cancelamento': 'dataCancelamento'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #CÃ³digo da regiÃ£o onde foi registrado o protocolo.
        
        self.codigo_regiao = None # int
        
        #Nome da Ã¡rea onde a regiÃ£o se encontra. (Exemplo &gt; \&quot;NORTE\&quot;)
        
        self.nome_regiao = None # str
        
        #CÃ³digo de bairro referente ao protocolo.
        
        self.codigo_bairro = None # int
        
        #Nome do bairro.
        
        self.nome_bairro = None # str
        
        #CÃ³digo do expediente emissor do protocolo.
        
        self.codigo_expediente = None # int
        
        #DescriÃ§Ã£o da Secretaria expediente do protocolo.
        
        self.secretaria_expediente = None # str
        
        #CÃ³digo do assunto referente ao protocolo.
        
        self.codigo_assunto = None # int
        
        #DescriÃ§Ã£o do assunto do protocolo.
        
        self.descricao_assunto = None # str
        
        #Ano em que o processo foi iniciado.
        
        self.ano_processo = None # int
        
        #CÃ³digo do ponto onde o protocolo foi cadastrado.
        
        self.ponto_cadastramento = None # int
        
        #Nome do ponto de cadastramento.
        
        self.nome_ponto_cadastramento = None # str
        
        #Data do cadastro do protocolo.
        
        self.data_cadastro = None # DateTime
        
        #Data do atendimento.
        
        self.data_atendimento = None # DateTime
        
        #Data em que o protocolo foi cancelado.
        
        self.data_cancelamento = None # DateTime
        
