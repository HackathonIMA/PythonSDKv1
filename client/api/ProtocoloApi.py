#!/usr/bin/env python

import sys
import os

from ..model import *


class ProtocoloApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def protocolo_get(self, **kwargs):
        """Dados sobre protocolo
        O recurso de protocolo existe para fornecer informaÃ§Ãµes sobre protocolos gerados pela prefeitura.\n

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            nome_regiao, str: Filtra resultados por Ã¡rea regional. (Exemplo > 'NORTE') (required)
            codigo_bairro, int: Filtra resultados por cÃ³digo do bairro. (required)
            sigla_expediente, str: Filtra resultados pelo cÃ³digo da secretaria expediente. (required)
            ano_processo, int: Filtra resultados pelo ano em que foram lanÃ§ados. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[ProtocoloResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'nome_regiao', 'codigo_bairro', 'sigla_expediente', 'ano_processo', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method protocolo_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/protocolo'
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
        
        if ('codigo_bairro' in params):
            queryParams['codigoBairro'] = self.apiClient.toPathValue(params['codigo_bairro'])
        
        if ('sigla_expediente' in params):
            queryParams['siglaExpediente'] = self.apiClient.toPathValue(params['sigla_expediente'])
        
        if ('ano_processo' in params):
            queryParams['anoProcesso'] = self.apiClient.toPathValue(params['ano_processo'])
        
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

        responseObject = self.apiClient.deserialize(response, 'list[ProtocoloResponse]')
        return responseObject
        
        
        
    
    def protocolo_id_get(self, **kwargs):
        """Dados sobre um protocolo especifico.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            id, int: Identificador do protocolo. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: ProtocoloResponse
        """

        allParams = ['client_id', 'id', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method protocolo_id_get" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/protocolo/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ProtocoloResponse')
        return responseObject
        
        
        
    


