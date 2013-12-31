#!/usr/bin/env python
"""
It's a draft script for testing an API of DIFFBOT

Author: Svyatoslav Sydorenko
ODesk job URL: https://www.odesk.com/jobs/~0174c2c0c47631a817
"""

import requests


def _get(_url, **kwargs):
    """
    Sends a GET request. Returns :class:`Response` object.

    :param _url: URL for the new :class:`Request` object.
    :param **kwargs: Optional arguments that ``request`` takes.

    This function overrides default `requests.get` as a workaround for passing
    `url` argument as HTTP parameter
    """

    return requests.request('GET', _url, params=kwargs)

requests.get = _get
del _get


class Diffbot:
    """Class for interaction with diffbot API"""
    def __init__(self, token, version=2):
        self._token = token
        self._ver = version
        self._api_url = 'http://api.diffbot.com/v{ver}/{method}'
        self._last_resp = None

    def build_method_url(self, method):
        """docstring for build_method_url"""
        return self._api_url.format(ver=self._ver, method=method)

    def api_call(self, method, **params):
        """
        api_call - method for making universal calls to diffbot API
        """
        params['token'] = self._token

        # TODO: check docs regarding following
        # params['format'] = 'json'  # Looks not neccessary

        self._last_resp = requests.get(
            self.build_method_url(method), **params)

        print('Queried URL is:', self._last_resp.url)

        # Simple response status check:
        if not self._last_resp.ok:
            raise Exception('DIFFBOT wasn\'t able to process this URL.',
                            self._last_resp.json())

        return self._last_resp.json()


if __name__ == '__main__':
    # TODO: write tests intead of commandline testing

    from pprint import pprint
    from sys import argv

    Token = open('token')
    API = Diffbot(token=Token.read(32).decode())
    Token.close()

    print('Testing `frontpage` method...')
    pprint(API.api_call(method='frontpage',
                        url='http://president.gov.ua/'))

    print('\nQuerying Russian post with `article` method...')
    pprint(API.api_call(method='article',
                        url='http://habrahabr.ru/post/119035/'))

    try:
        print('\nTesting `article` method again..')
        pprint(API.api_call(method='article',
                            url='http://webknjaz.com'
                                '/2012/06/21/twitter-localization/'))
    except Exception as e:
        print('An exception caught (HTTP error 500 expected):',
              e.args[0] if len(e.args) > 0 else '',
              e.args[1] if len(e.args) > 1 else '')

    if len(argv) > 1:
        print('\nRequesting commandline passed URLs with `article` method')
        for url in argv[1:]:
            print(url)
            try:
                pprint(API.api_call(method='article', url=url))
            except Exception as e:
                print('An exception caught:',
                      e.args[0] if len(e.args) > 0 else '')
