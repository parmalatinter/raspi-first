# -*- coding: utf-8 -*-
import requests

class Request:
    def get(self, url):

        response = requests.get(url)

        return response