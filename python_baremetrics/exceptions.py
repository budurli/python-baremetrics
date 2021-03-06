# -*- coding: utf-8 -*-

from simplejson import JSONDecodeError


class BaremetricsException(Exception):
    pass


class APICallNotImplemented(BaremetricsException):
    pass


class BaremetricsAPIException(BaremetricsException):
    def __init__(self, r_message):
        try:
            json_data = r_message.json()
        except JSONDecodeError:
            error = r_message.text
        else:
            error = json_data.get('error')

        message = 'Got [{}] "{}" when calling {} {}'.format(
            r_message.status_code,
            error,
            r_message.request.method,
            r_message.request.url,
        )
        super(BaremetricsAPIException, self).__init__(message)
