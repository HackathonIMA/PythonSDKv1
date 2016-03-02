#!/usr/bin/env python

import sys
import os

from ..model import *


class EducaoApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def educacao_get(self, **kwargs):
        """Dados sobre educaÃ§Ã£o
        O recurso de educaÃ§Ã£o retorna dados sobre instituiÃ§Ãµes educacionais na \nÃ¡rea de Campinas.\n

        Args:
            access_token, str: Access Token com as permissÃµes de acesso. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            

        Returns: list[EducacaoResponse]
        """

        allParams = ['access_token', 'client_id', 'offset', 'limit']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method educacao_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/educacao'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        

        
        if ('access_token' in params):
            headerParams['access-token'] = params['access_token']
        
        if ('client_id' in params):
            headerParams['client_id'] = params['client_id']
        

        

        postData = None

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams)

        
        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'list[EducacaoResponse]')
        return responseObject
        
        
        
    
    def educacao_id_get(self, **kwargs):
        """Retorna um dado sobre educaÃ§Ã£o especÃ­fico.
        

        Args:
            access_token, str: Access Token com as permissÃµes de acesso. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            id, int: Identificador do registro. (required)
            

        Returns: EducacaoResponse
        """

        allParams = ['access_token', 'client_id', 'id']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method educacao_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/educacao/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'EducacaoResponse')
        return responseObject
        
        
        
    


