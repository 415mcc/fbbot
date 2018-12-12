import functools

from collections import namedtuple
from urllib.parse import urljoin, urlsplit

import requests

from bs4 import BeautifulSoup


def only_if_logged_in(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if (not self._logged_in):
            raise PermissionError('must login before calling {}()'
                                  .format(func.__name__))
        return func(self, *args, **kwargs)
    return wrapper


class Session:
    FormInfo = namedtuple('FormInfo', ['params', 'post_url'])

    def __init__(self, settings):
        self._logged_in = False
        self._settings = settings
        self.req = requests.Session()
        self.req.headers.update({
            'User-Agent': self._settings.user_agent,
        })

    @staticmethod
    def __form_data(text, formid, params, soup=None, form_url=None):
        if type(params) is not dict:
            raise TypeError('Params must be a dict')
        if soup is None:
            soup = BeautifulSoup(text, 'html.parser')
        form = soup.find('form', attrs={'id': formid})
        action = form.attrs.get('action')
        if not urlsplit(action).netloc:
            if form_url is None or not urlsplit(form_url).netloc:
                raise ValueError('kwarg form_url must be specified if form '
                                 'action lacks a host')
            action = urljoin(form_url, action)
        inputs = form.find_all('input') + form.find_all('textarea')
        for i in inputs:
            try:
                name = i.attrs['name']
                type_ = i.attrs['type']
                value = params.get(name)
                if type_ == 'submit':
                    continue
                elif type_ == 'hidden':
                    value = i.attrs['value'] if value is None else value
                elif value is None:
                    raise ValueError('kwarg params dictionary is missing a '
                                     'value for a non-hidden field')
            except KeyError:
                pass
            else:
                params[name] = value
        return Session.FormInfo(params=params, post_url=action)

    def __complete_form(self, form_url, form_id, params, get_params={}):
        page = self.req.get(form_url, params=get_params)
        page.raise_for_status()
        fd = Session.__form_data(page.text, form_id, params, form_url=form_url)
        post = self.req.post(fd.post_url, data=fd.params)
        post.raise_for_status()

    def login(self):
        self.__complete_form(
            'https://mbasic.facebook.com/login.php',
            'login_form',
            {
                'email': self._settings.username,
                'pass': self._settings.password,
            },
        )
        self._logged_in = True

    @only_if_logged_in
    def message(self, user_id, body):
        self.__complete_form(
            'https://mbasic.facebook.com/messages/compose/',
            'composer_form',
            {'body': body},
            get_params={'ids': user_id},
        )


class Settings:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_agent = 'Mozilla/5.0'
