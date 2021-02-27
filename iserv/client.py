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

import requests
from bs4 import BeautifulSoup
import datetime

from .task import Task
from.iservfile import IServFile

class Client:
    r"""Dies ist die Verbindung zum IServ.

    Diese Parameter werden zum erstellen benötigt.

    Parameters
    -----------
    url: :class:`str`
        Die URL zum IServ, zu dem eine Verbindung hergestellt werden soll.
    username: :class:`str`
        Der Benutzername der zum einloggen benutzt wird.
    password: :class:`str`
        Das dazugehörige Passwort.

    Attributes
    -----------
    session: :class:`requests.Session`
        Die Sitzung, die der Client mit dem IServ hat.
    """


    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self._headers = {'User-Agent': 'Mozilla/5.0'}
        self.session = self._get_session()

    def _get_session(self):
        session = requests.Session()
        payload = {'_username': self.username, '_password': self.password, "_remember_me": True}
        try:
            response = session.post(self.url + "iserv/app/login", headers=self._headers, data=payload)
            if response.status_code == 200:
                if response.text.__contains__("Anmeldung fehlgeschlagen!"):
                    raise Exception("Das angegebene Passwort ist falsch")
                if response.text.__contains__("Account existiert nicht!"):
                    raise Exception("Der angegebene Benutzer existiert nicht")
            else:
                raise Exception("Die angegebene URL führt nicht zu einem IServ")
        except requests.exceptions.ConnectionError:
            raise Exception("Die angegebene URL konnte nicht abgerufen werden")
        return session

    def get_task(self, id):
        """Gibt die Aufgabe mit der ID zurück.
        Parameters
        -----------
        id: :class:`int`
            The ID to search for.
        Returns
        --------
        :class:`Task`
            Die Aufgabe oder ``None``, falls diese nicht gefunden wird
        """
        try:
            response = self.session.get(self.url + "iserv/exercise/show/" + str(id), headers=self._headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml")
                title = soup.find("h1").text
                description = soup.find("td", {"class": "text-break-word"})
                if description.find("div") is None:
                    description = description.text[1:-1]
                else:
                    description = description.text[2:-2]
                teacher = None
                start = datetime.datetime.strptime(soup.find_all("td")[1].text, '%d.%m.%Y %H:%M')
                end = datetime.datetime.strptime(soup.find_all("td")[2].text, '%d.%m.%Y %H:%M')
                tags = []
                for a in soup.find_all("td")[3].find_all("a"):
                    tags.append(a.text[1:])
                done = None
                feedback = None
                attachments = []
                for a in soup.find("table", {"class": "table table-condensed mt0"}).find("tbody").find_all("tr"):
                    tds = a.find_all("td")
                    name = tds[0].text
                    url = self.url + tds[0].find("a")["href"][1:]
                    size = tds[1].text
                    if size.__contains__(" KB"):
                        raw_size = int(float(size[:-3])*1000)
                    elif size.__contains__(" MB"):
                        raw_size = int(float(size[:-3])*1000000)
                    elif size.__contains__(" Bytes"):
                        raw_size = int(size[:-6])
                    elif size.__contains__(" GB"):
                        raw_size = int(float(size[:-3])*1000000000)
                    else:
                        raw_size = 0
                    attachments.append(IServFile(name, url, raw_size, size, None))
                return Task(title, description, teacher, id, start, end, tags, done, feedback, attachments)
            else:
                return None
        except:
            raise
            return None
