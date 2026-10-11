"""Form handling written before cgi was removed in Python 3.13."""

import cgi


def read_form(environ):
    return cgi.FieldStorage(environ=environ)
