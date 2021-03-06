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

from .iservfile import IServFile

class LiteUser:
    """Die Lite-Klasse der Klasse :class:`User`. Sie enthält nur Grundlegende Informationen des Users, um den vollen User zu bekommen ``user()`` ausführen.

    Attributes
    -----------
    name: :class:`str`
        Der Name des Users im Format Vorname Nachname
    firstname: :class:`str`
        Der Vorname und eventuell die Zweitnamen des Users
        .. warning::
            Der Vorname ist nur Verfügbar, wenn unter Profil -> Einstellungen -> Namen von Personen anzeigen und sortieren nach -> Nachname, Vorname
            ist
    firstname: :class:`str`
        Der Nachname des Users
        .. warning::
            Der Nachname ist nur Verfügbar, wenn unter Profil -> Einstellungen -> Namen von Personen anzeigen und sortieren nach -> Nachname, Vorname
            ist
    username: :class:`str`
        Der Name des Users im Format vorname.nachname oder v.nachname (je nachdem was vor der E-Mail-Adresse steht)
    mail: :class:`str`
        Die E-Mail-Adresse des Users
    """

    def __init__(self, name, username, mail, firstname=None, lastname=None, client=None):
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.mail = mail
        self.picture = IServFile(username, client.url + "iserv/addressbook/public/image/" + username, None, None, None)
        self._client = client
