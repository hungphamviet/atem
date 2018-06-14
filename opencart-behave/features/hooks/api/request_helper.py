import json
import logging
import requests
from conf.env_setup import EnvSetup

class RequestHelper(object):
    logger = logging.getLogger(__name__)

    @staticmethod
    def print_response_json(request):
        RequestHelper.logger.debug('Response code: %s', request.status_code)
        if request.status_code not in [204, 404]:
            RequestHelper.logger.debug(u'''Response json:
            {json}'''.format(json=request.json()))

    @staticmethod
    def send_post_request(session, end_point, data=''):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending POST request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        response = requests.post(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_put_request(session, end_point, data=''):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending PUT request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        response = requests.put(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_patch_request(session, end_point, data):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending PATCH request
        URL  = {url}
        Data = {data}'''.format(url=url, data=data))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_delete_request(session, end_point):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending DELETE request
        URL  = {url}'''.format(url=url))
        headers = session.get_auth_token()
        headers.update({'content-type': 'application/json'})
        response = requests.delete(url, headers=headers)
        RequestHelper.print_response_json(response)
        return response

    @staticmethod
    def send_get_request(session, end_point):
        url = EnvSetup.API_HOST + end_point
        RequestHelper.logger.debug(u'''Sending GET request
        URL  = {url}'''.format(url=url))
        response = requests.get(url, headers=session.get_auth_token())
        RequestHelper.print_response_json(response)
        return response
