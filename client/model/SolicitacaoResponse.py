#!/usr/bin/env python


class SolicitacaoResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'nome_regional': 'str',
            'codigo_regiao': 'str',
            'nome_regiao': 'str',
            'secretaria': 'str',
            'codigo_bairro': 'int',
            'nome_bairro': 'str',
            'codigo_assunto': 'int',
            'descricao_assunto': 'str',
            'ano_solicitacao': 'int',
            'tipo_solicitacao': 'int',
            'descricao_tipo_solicitacao': 'str',
            'status_solicitacao': 'int',
            'descricao_status': 'str',
            'data_cadastro': 'datetime',
            'data_previsao_resposta': 'datetime',
            'data_atendimento': 'datetime',
            'data_conclusao': 'datetime',
            'cep': 'str',
            'tipo_logradouro': 'str',
            'nome_logradouro': 'str',
            'data_providencia': 'datetime'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'nome_regional': 'nomeRegional',
            'codigo_regiao': 'codigoRegiao',
            'nome_regiao': 'nomeRegiao',
            'secretaria': 'secretaria',
            'codigo_bairro': 'codigoBairro',
            'nome_bairro': 'nomeBairro',
            'codigo_assunto': 'codigoAssunto',
            'descricao_assunto': 'descricaoAssunto',
            'ano_solicitacao': 'anoSolicitacao',
            'tipo_solicitacao': 'tipoSolicitacao',
            'descricao_tipo_solicitacao': 'descricaoTipoSolicitacao',
            'status_solicitacao': 'statusSolicitacao',
            'descricao_status': 'descricaoStatus',
            'data_cadastro': 'dataCadastro',
            'data_previsao_resposta': 'dataPrevisaoResposta',
            'data_atendimento': 'dataAtendimento',
            'data_conclusao': 'dataConclusao',
            'cep': 'cep',
            'tipo_logradouro': 'tipoLogradouro',
            'nome_logradouro': 'nomeLogradouro',
            'data_providencia': 'dataProvidencia'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #Nome da administraÃ§Ã£o regional.
        
        self.nome_regional = None # str
        
        #CÃ³digo da regiÃ£o.
        
        self.codigo_regiao = None # str
        
        #Nome / DescriÃ§Ã£o da regiÃ£o.
        
        self.nome_regiao = None # str
        
        #Nome da secretÃ¡ria.
        
        self.secretaria = None # str
        
        #CÃ³digo da bairro.
        
        self.codigo_bairro = None # int
        
        #Nome do bairro.
        
        self.nome_bairro = None # str
        
        #CÃ³digo do assunto da solicitaÃ§Ã£o.
        
        self.codigo_assunto = None # int
        
        #DescriÃ§Ã£o do assunto da solicitaÃ§Ã£o.
        
        self.descricao_assunto = None # str
        
        #Ano em que a solicitaÃ§Ã£o ocorreu.
        
        self.ano_solicitacao = None # int
        
        #CÃ³digo referente ao tipo de solicitaÃ§Ã£o.
        
        self.tipo_solicitacao = None # int
        
        #DescriÃ§Ã£o do tipo de solicitaÃ§Ã£o realizada.
        
        self.descricao_tipo_solicitacao = None # str
        
        #CÃ³digo do status da solicitaÃ§Ã£o.
        
        self.status_solicitacao = None # int
        
        #DescriÃ§Ã£o do status.
        
        self.descricao_status = None # str
        
        #Data do cadastramento da solicitaÃ§Ã£o.
        
        self.data_cadastro = None # datetime
        
        #Data da previsÃ£o de resposta da solicitaÃ§Ã£o depois de executada.
        
        self.data_previsao_resposta = None # datetime
        
        #Data em que o atendimento ocorreu
        
        self.data_atendimento = None # datetime
        
        #Data em que a solicitaÃ§Ã£o foi concluÃ­da.
        
        self.data_conclusao = None # datetime
        
        #CEP
        
        self.cep = None # str
        
        #Tipo de logradouro (Exemplo &gt; Rua, Avenida, etc.)
        
        self.tipo_logradouro = None # str
        
        #Nome da rua / logradouro.
        
        self.nome_logradouro = None # str
        
        #Data da providÃªncia
        
        self.data_providencia = None # datetime
        
