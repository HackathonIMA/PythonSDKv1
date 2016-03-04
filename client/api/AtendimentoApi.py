#!/usr/bin/env python

import sys
import os

from ..model import *


class AtendimentoApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def atendimento_get(self, **kwargs):
        """Dados sobre atendimentos
        O recurso 156 foi projetado para retornar todas as informaÃ§Ãµes sobre solicitaÃ§Ãµes e atendimentos realizados pela prefeitura de Campinas. Ã recomendado o uso de filtros passados na query param para retornar conjuntos de informaÃ§Ãµes especificas.\n

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            nome_regiao, str: Filtra os resultados por Ã¡rea regional. (Exemplo > 'LESTE') (required)
            ano_solicitacao, int: Filtra os resultados por ano em que a solicitaÃ§Ã£o foi feita. (required)
            codigo_cep, str: Filtra os resultados pelo CEP em que a solicitacao estÃ¡ cadastrada. (required)
            descricao_status, str: Filtra os resultados por status, passado o tipo de status referente. (Exemplo > 'EXECUTADO') (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[SolicitacaoResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'nome_regiao', 'ano_solicitacao', 'codigo_cep', 'descricao_status', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method atendimento_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/atendimento'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
        if ('nome_regiao' in params):
            queryParams['nomeRegiao'] = self.apiClient.toPathValue(params['nome_regiao'])
        
        if ('ano_solicitacao' in params):
            queryParams['anoSolicitacao'] = self.apiClient.toPathValue(params['ano_solicitacao'])
        
        if ('codigo_cep' in params):
            queryParams['codigoCEP'] = self.apiClient.toPathValue(params['codigo_cep'])
        
        if ('descricao_status' in params):
            queryParams['descricaoStatus'] = self.apiClient.toPathValue(params['descricao_status'])
        
        if ('fields' in params):
            queryParams['fields'] = self.apiClient.toPathValue(params['fields'])
        
        if ('filters' in params):
            queryParams['filters'] = self.apiClient.toPathValue(params['filters'])
        

        
        if ('client_id' in params):
            headerParams['client_id'] = params['client_id']
        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[SolicitacaoResponse]')
        return responseObject
        
        
        
    
    def atendimento_id_get(self, **kwargs):
        """Dado de um atendimento especifico.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            id, str: Identificador da solicitaÃ§Ã£o (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: SolicitacaoResponse
        """

        allParams = ['client_id', 'id', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method atendimento_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/atendimento/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('fields' in params):
            queryParams['fields'] = self.apiClient.toPathValue(params['fields'])
        
        if ('filters' in params):
            queryParams['filters'] = self.apiClient.toPathValue(params['filters'])
        

        
        if ('client_id' in params):
            headerParams['client_id'] = params['client_id']
        

        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'SolicitacaoResponse')
        return responseObject
        
        
        
    


