from bs4 import BeautifulSoup
from collections import namedtuple
import requests


class Session(object):
    def __init__(self, settings):
        self.settings = settings
        self.req = requests.Session()
        self.req.headers.update({
            'User-Agent': self.settings.user_agent,
        })

    # TODO: add support for relative URLs
    @staticmethod
    def __form_data(text, formid, params, soup=None):
        if soup is None:
            soup = BeautifulSoup(text, 'html.parser')
        form = soup.find('form', attrs={'id': formid})
        action = form.attrs.get('action')
        inputs = form.find_all('input') + form.find_all('textarea')
        for i in inputs:
            try:
                name = i.attrs['name']
                type_ = i.attrs['type']
                if type_ == 'submit':
                    continue
                elif type_ == 'hidden':
                    value = i.attrs['value']
                else:
                    value = params.get(name)
                    if value is None:
                        raise ValueError('Parameter dictionary is missing a '
                                         'value for a non-hidden field.')
            except KeyError:
                pass
            else:
                params[name] = value
        return namedtuple('FormInfo', ['params', 'post_url'])(params=params,
                                                              post_url=action)

    def login(self):
        lp = self.req.get('https://mbasic.facebook.com/login.php')
        fd = Session.__form_data(lp.text, 'login_form', {
            'email': self.settings.username,
            'pass': self.settings.password,
        })
        self.req.post(fd.post_url, data=fd.params)

    def message(self, user_id, body):
        mp = self.req.get('https://mbasic.facebook.com/messages/compose/',
                          params={'ids': user_id})
        fd = Session.__form_data(mp.text, 'composer_form', {
            'body': body,
        })
        # bodge because __form_data doesn't support relative urls yet
        self.req.post('https://mbasic.facebook.com' +
                      fd.post_url, data=fd.params)


class Settings(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user_agent = "Mozilla/5.0"
