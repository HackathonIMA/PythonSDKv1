#!/usr/bin/env python

import sys
import os

from ..model import *


class SadeApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def saude_get(self, **kwargs):
        """Dados sobre sÃ¡ude
        O recurso sÃ¡ude tem a funÃ§Ã£o de mostrar os dados sobre atendimentos hospitalares realizados em hospitais da Ã¡rea de Campinas.\n

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[SaudeResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method saude_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/saude'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('offset' in params):
            queryParams['offset'] = self.apiClient.toPathValue(params['offset'])
        
        if ('limit' in params):
            queryParams['limit'] = self.apiClient.toPathValue(params['limit'])
        
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

        responseObject = self.apiClient.deserialize(response, 'list[SaudeResponse]')
        return responseObject
        
        
        
    
    def saude_id_get(self, **kwargs):
        """Retorna um dado hospitalar especÃ­fico.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            id, int: Identificador do protocolo. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: SaudeResponse
        """

        allParams = ['client_id', 'id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method saude_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/saude/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}

        
        if ('fields' in params):
            queryParams['fields'] = self.apiClient.toPathValue(params['fields'])
        

        
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

        responseObject = self.apiClient.deserialize(response, 'SaudeResponse')
        return responseObject
        
        
        
    


