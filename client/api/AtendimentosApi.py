#!/usr/bin/env python

import sys
import os

from ..model import *


class AtendimentosApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def 156_get(self, **kwargs):
        """Dados sobre atendimentos
        O recurso 156 foi projetado para retornar todas as informaÃ§Ãµes sobre solicitaÃ§Ãµes e atendimentos realizados pela prefeitura de Campinas. Ã recomendado o uso de filtros passados na query param para retornar conjuntos de informaÃ§Ãµes especificas.\n

        Args:
            access_token, str: Access Token com as permissÃµes de acesso. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            nome_regiao, str: Filtra os resultados por Ã¡rea regional. (Exemplo > 'LESTE') (required)
            ano_solicitacao, int: Filtra os resultados por ano em que a solicitaÃ§Ã£o foi feita. (required)
            codigo_cep, str: Filtra os resultados pelo CEP em que a solicitacao estÃ¡ cadastrada. (required)
            descricao_status, str: Filtra os resultados por status, passado o tipo de status referente. (Exemplo > 'EXECUTADO') (required)
            

        Returns: list[SolicitacaoResponse]
        """

        allParams = ['access_token', 'client_id', 'offset', 'limit', 'nome_regiao', 'ano_solicitacao', 'codigo_cep', 'descricao_status']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method 156_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/156'
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
        

        
        if ('access_token' in params):
            headerParams['access-token'] = params['access_token']
        
        if ('client_id' in params):
            headerParams['client_id'] = params['client_id']
        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[SolicitacaoResponse]')
        return responseObject
        
        
        
    
    def 156_id_get(self, **kwargs):
        """Dado de um atendimento especifico.
        

        Args:
            access_token, str: Access Token com as permissÃµes de acesso. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            id, str: Identificador da solicitaÃ§Ã£o (required)
            

        Returns: SolicitacaoResponse
        """

        allParams = ['access_token', 'client_id', 'id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method 156_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/156/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        

        
        if ('access_token' in params):
            headerParams['access-token'] = params['access_token']
        
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
        
        
        
    


