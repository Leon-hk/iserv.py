# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2021 CaptainSword123

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class IServException(Exception):
    """Grund Exceptionklasse für iserv.py
    """
    pass

class InvalidUrlException(IServException):
    """Tritt auf, wenn die angegebene URL nicht aufgerufen werden kann

    Attributes
    -----------
    url: :class:`str`
        Die URL, die nicht aufgerufen werden kann
    """

    def __init__(self, url):
        self.url = url
        super().__init__(f"Die URL {url} ist nicht erreichbar. Versichere dich, dass sie richtig geschrieben ist und der IServ erreichbar ist.")

class IServNotFoundException(IServException):
    """Tritt auf, wenn kein IServ hinter der angegebenen URL gefunden wird

    Attributes
    -----------
    url: :class:`str`
        Die URL, hinter der kein IServ gefunden wurde
    """

    def __init__(self, url):
        self.url = url
        super().__init__(f"Die URL {url} führt nicht zu einem IServ.")

class CredentialsException(IServException):
    """Tritt auf, wenn der Benutzername oder das Passwort nicht stimmen

    Attributes
    -----------
    url: :class:`str`
        Die URL, hinter der kein IServ gefunden wurde
    """

    def __init__(self, error):
        self.error = error
        super().__init__(error)