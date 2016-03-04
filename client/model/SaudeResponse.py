#!/usr/bin/env python


class SaudeResponse:

    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'distrito_vinculo': 'str',
            'municipio': 'str',
            'uf': 'str',
            'local_atendimento': 'str',
            'distrito_atendimento': 'str',
            'data_atendimento': 'DateTime',
            'codigo_tipo_atendimento': 'int',
            'descricao_tipo_atendimento': 'str',
            'descricao_grupo_atendimento': 'str',
            'codigo_grupo_atendimento_sus': 'int',
            'ocupacao_profissional': 'str',
            'descricao_tipo_vinculo_sms': 'str',
            'codigo_procedimento_sus': 'int',
            'descricao_procedimento': 'str',
            'codigo_atividade_profissional_sus': 'int',
            'descricao_atividade_profissional': 'str',
            'sexo': 'str',
            'idade': 'str',
            'hora': 'str',
            'periodo': 'str',
            'data_nascimento': 'DateTime',
            'quantidade_realizada': 'int'
            
        }

        self.attributeMap = {
            'id': 'ID',
            'distrito_vinculo': 'distritoVinculo',
            'municipio': 'municipio',
            'uf': 'uf',
            'local_atendimento': 'localAtendimento',
            'distrito_atendimento': 'distritoAtendimento',
            'data_atendimento': 'dataAtendimento',
            'codigo_tipo_atendimento': 'codigoTipoAtendimento',
            'descricao_tipo_atendimento': 'descricaoTipoAtendimento',
            'descricao_grupo_atendimento': 'descricaoGrupoAtendimento',
            'codigo_grupo_atendimento_sus': 'codigoGrupoAtendimentoSUS',
            'ocupacao_profissional': 'ocupacaoProfissional',
            'descricao_tipo_vinculo_sms': 'descricaoTipoVinculoSMS',
            'codigo_procedimento_sus': 'codigoProcedimentoSUS',
            'descricao_procedimento': 'descricaoProcedimento',
            'codigo_atividade_profissional_sus': 'codigoAtividadeProfissionalSUS',
            'descricao_atividade_profissional': 'descricaoAtividadeProfissional',
            'sexo': 'sexo',
            'idade': 'idade',
            'hora': 'hora',
            'periodo': 'periodo',
            'data_nascimento': 'dataNascimento',
            'quantidade_realizada': 'quantidadeRealizada'
            
        }

        
        #Identificador do registro.
        
        self.id = None # str
        
        #Distrito onde o antendimento foi realizado.
        
        self.distrito_vinculo = None # str
        
        #Nome do municÃ­pio
        
        self.municipio = None # str
        
        #IndicaÃ§Ã£o da unidade federal.
        
        self.uf = None # str
        
        #Nome do local onde o atendimento foi feito.
        
        self.local_atendimento = None # str
        
        #Indicacao do distrito onde o atendimento ocorreu.
        
        self.distrito_atendimento = None # str
        
        #Data e hora que o atendimento ocorreu.
        
        self.data_atendimento = None # DateTime
        
        #CÃ³digo do tipo de atendimento.
        
        self.codigo_tipo_atendimento = None # int
        
        #Descricao do tipo de atendimento.
        
        self.descricao_tipo_atendimento = None # str
        
        #DescriÃ§Ã£o do grupo de atendimento.
        
        self.descricao_grupo_atendimento = None # str
        
        #CÃ³digo do grupo de atendimento vinculado ao SUS.
        
        self.codigo_grupo_atendimento_sus = None # int
        
        #Descricao formal da ocupaÃ§Ã£o do profissional.
        
        self.ocupacao_profissional = None # str
        
        #DescriÃ§Ã£o do tipo de vinculo com a Secretaria Municipal de SaÃºde.
        
        self.descricao_tipo_vinculo_sms = None # str
        
        #CÃ³digo do procedimento realizado pelo SUS
        
        self.codigo_procedimento_sus = None # int
        
        #Descricao do procedimento.
        
        self.descricao_procedimento = None # str
        
        #CÃ³digo do profissional SUS.
        
        self.codigo_atividade_profissional_sus = None # int
        
        #IndicaÃ§Ã£o da profissÃ£o do atendente.
        
        self.descricao_atividade_profissional = None # str
        
        #DescriÃ§Ã£o do sexo. (&#39;MASCULINO&#39; ou &#39;FEMININO&#39;)
        
        self.sexo = None # str
        
        #IndicaÃ§Ã£o da idade.
        
        self.idade = None # str
        
        #IndicaÃ§Ã£o da hora da ocorrÃªncia.
        
        self.hora = None # str
        
        #Descricao do periodo (Exemplo &gt; MANHA)
        
        self.periodo = None # str
        
        #Data de nascimento do profissional.
        
        self.data_nascimento = None # DateTime
        
        #Quantidade de atendimento realizados.
        
        self.quantidade_realizada = None # int
        
