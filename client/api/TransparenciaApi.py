#!/usr/bin/env python

import sys
import os

from ..model import *


class TransparenciaApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    
    def queryfiltro_acao(self, **kwargs):
        """Consulta das aÃ§Ãµes da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[AcoesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method queryfiltro_acao" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/acoes'
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

        responseObject = self.apiClient.deserialize(response, 'list[AcoesResponse]')
        return responseObject
        
        
        
    
    def queryfiltro_acao2(self, **kwargs):
        """Consulta da aÃ§Ã£o da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: AcoesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method queryfiltro_acao2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/acoes/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'AcoesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_credor(self, **kwargs):
        """Consulta de credores.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[CredorResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_credor" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/credores'
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

        responseObject = self.apiClient.deserialize(response, 'list[CredorResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_credor2(self, **kwargs):
        """Consulta de credor.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: CredorResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_credor2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/credores/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'CredorResponse')
        return responseObject
        
        
        
    
    def ptr_ft_despesa(self, **kwargs):
        """Consulta de despesas da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[despesasResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_ft_despesa" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/despesas'
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

        responseObject = self.apiClient.deserialize(response, 'list[despesasResponse]')
        return responseObject
        
        
        
    
    def ptr_ft_despesa2(self, **kwargs):
        """Consulta de uma despesa da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: despesasResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_ft_despesa2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/despesas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'despesasResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_elemento_despesa(self, **kwargs):
        """Consulta das despesas dos elementos da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[ElementoDespesaResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_elemento_despesa" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/elementos'
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

        responseObject = self.apiClient.deserialize(response, 'list[ElementoDespesaResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_elemento_despesa2(self, **kwargs):
        """Consulta da despesa do elemento da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: ElementoDespesaResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_elemento_despesa2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/elementos/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ElementoDespesaResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_ne(self, **kwargs):
        """Consulta de empenhos da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[EmpenhoResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_ne" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/empenhos'
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

        responseObject = self.apiClient.deserialize(response, 'list[EmpenhoResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_ne2(self, **kwargs):
        """Consulta de empenho da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: EmpenhoResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_ne2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/empenhos/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'EmpenhoResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_fonte_detalhada(self, **kwargs):
        """Consulta de contas das fontes da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[FontesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_fonte_detalhada" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/fontes'
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

        responseObject = self.apiClient.deserialize(response, 'list[FontesResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_fonte_detalhada2(self, **kwargs):
        """Consulta de conta da fonte da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: FontesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_fonte_detalhada2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/fontes/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'FontesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_fonte(self, **kwargs):
        """Consulta das receitas das fontes detalhadas da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[FonteDetalhadaResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_fonte" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/fontesDetalhadas'
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

        responseObject = self.apiClient.deserialize(response, 'list[FonteDetalhadaResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_fonte2(self, **kwargs):
        """Consulta da receita da fonte detalhada da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: FonteDetalhadaResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_fonte2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/fontesDetalhadas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'FonteDetalhadaResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_funcao(self, **kwargs):
        """Consulta das funÃ§Ãµes da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[FuncoesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_funcao" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/funcoes'
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

        responseObject = self.apiClient.deserialize(response, 'list[FuncoesResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_funcao2(self, **kwargs):
        """Consulta da funÃ§Ã£o da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: FuncoesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_funcao2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/funcoes/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'FuncoesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_subalinea_receita(self, **kwargs):
        """Consulta de contas das naturezas das receitas da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[naturezasResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subalinea_receita" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/naturezas'
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

        responseObject = self.apiClient.deserialize(response, 'list[naturezasResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_subalinea_receita2(self, **kwargs):
        """Consulta de conta da natureza da receita da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: naturezasResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subalinea_receita2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/naturezas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'naturezasResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_programa(self, **kwargs):
        """Consulta dos programas da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[ProgramaResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_programa" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/programas'
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

        responseObject = self.apiClient.deserialize(response, 'list[ProgramaResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_programa2(self, **kwargs):
        """Consulta do programa da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: ProgramaResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_programa2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/programas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ProgramaResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_projeto_atividade(self, **kwargs):
        """Consulta dos projetos e atividades da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[ProjetoAtividadeResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_projeto_atividade" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/projetosAtividades'
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

        responseObject = self.apiClient.deserialize(response, 'list[ProjetoAtividadeResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_projeto_atividade2(self, **kwargs):
        """Consulta do projeto e atividade da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: ProjetoAtividadeResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_projeto_atividade2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/projetosAtividades/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ProjetoAtividadeResponse')
        return responseObject
        
        
        
    
    def ptr_ft_receita(self, **kwargs):
        """Consulta das receitas da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[ReceitaResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_ft_receita" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/receitas'
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

        responseObject = self.apiClient.deserialize(response, 'list[ReceitaResponse]')
        return responseObject
        
        
        
    
    def ptr_ft_receita2(self, **kwargs):
        """Consulta da receita da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: ReceitaResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_ft_receita2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/receitas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'ReceitaResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_subitem_conta(self, **kwargs):
        """Consulta dos sub-itens das contas.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[subItensContasResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subitem_conta" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/subItensContas'
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

        responseObject = self.apiClient.deserialize(response, 'list[subItensContasResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_subitem_conta2(self, **kwargs):
        """Consulta do sub-item das contas.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: subItensContasResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subitem_conta2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/subItensContas/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'subItensContasResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_subfuncao(self, **kwargs):
        """Consulta das sub-funÃ§Ãµes da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[SubfuncoesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subfuncao" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/subfuncoes'
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

        responseObject = self.apiClient.deserialize(response, 'list[SubfuncoesResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_subfuncao2(self, **kwargs):
        """Consulta da sub-funÃ§Ã£o da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: SubfuncoesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_subfuncao2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/subfuncoes/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'SubfuncoesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_tipo_licitacao(self, **kwargs):
        """Consulta dos tipos de licitaÃ§Ãµes.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[tipoLicitacoesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_tipo_licitacao" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/tipoLicitacoes'
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

        responseObject = self.apiClient.deserialize(response, 'list[tipoLicitacoesResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_tipo_licitacao2(self, **kwargs):
        """Consulta do tipo de licitaÃ§Ã£o.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: tipoLicitacoesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_tipo_licitacao2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/tipoLicitacoes/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'tipoLicitacoesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_unidade_orcamentaria(self, **kwargs):
        """Consulta das unidades da preifeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[UnidadesResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_unidade_orcamentaria" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/unidades'
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

        responseObject = self.apiClient.deserialize(response, 'list[UnidadesResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_unidade_orcamentaria2(self, **kwargs):
        """Consulta da unidade da preifeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: UnidadesResponse
        """

        allParams = ['id', 'client_id', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_unidade_orcamentaria2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/unidades/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'UnidadesResponse')
        return responseObject
        
        
        
    
    def ptr_lkp_unidade_gestora(self, **kwargs):
        """Consulta de contas das unidades gestoras da prefeitura.
        

        Args:
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            filters, list[str]: ParÃ¢metro utilizado para pesquisar valores de campos especÃ­ficos, por exemplo, para pesquisar um id de valor 123, passar o valor id:123 (required)
            

        Returns: list[UnidadeGestoraResponse]
        """

        allParams = ['client_id', 'offset', 'limit', 'fields', 'filters']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_unidade_gestora" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/unidadesGestoras'
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

        responseObject = self.apiClient.deserialize(response, 'list[UnidadeGestoraResponse]')
        return responseObject
        
        
        
    
    def ptr_lkp_unidade_gestora2(self, **kwargs):
        """Consulta de conta da unidade gestora da prefeitura.
        

        Args:
            id, str: Identificador do registro. (required)
            client_id, str: Token disponibilizado na criaÃ§Ã£o da APP. (required)
            offset, str: ParÃ¢metro utilizado para indicar a posiÃ§Ã£o do registro inicial que serÃ¡ trazido. A primeira posiÃ§Ã£o Ã© sempre zero (0). (required)
            limit, str: ParÃ¢metro utilizado para indicar a quantidade de registros que deve ser trazido na consulta. (required)
            fields, list[str]: ParÃ¢metro utilizado para pesquisar campos especÃ­ficos (required)
            

        Returns: UnidadeGestoraResponse
        """

        allParams = ['id', 'client_id', 'offset', 'limit', 'fields']

        params = locals()
        for (key, val) in params['kwargs'].items():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method ptr_lkp_unidade_gestora2" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/transparencia/unidadesGestoras/{id}'
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

        responseObject = self.apiClient.deserialize(response, 'UnidadeGestoraResponse')
        return responseObject
        
        
        
    


