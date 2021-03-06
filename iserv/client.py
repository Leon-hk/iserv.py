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

from .errors import *
from .messengerclient import MessengerClient
from .task import LiteTask, Task, TextTask, FileTask, BoolTask
from .iservfile import IServFile
from .user import LiteUser

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
        if not url.startswith("https://"):
            url = "https://" + url
        if not url.endswith("/"):
            url = url + "/"
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
                    raise CredentialsException("Das angegebene Passwort ist falsch")
                if response.text.__contains__("Account existiert nicht!"):
                    raise CredentialsException(f"Der Benutzer {self.username} existiert nicht")
            else:
                raise IServNotFoundException(self.url)
        except requests.exceptions.ConnectionError:
            raise InvalidUrlException(self.url)
        return session

    def MessengerClient(self):
        return MessengerClient(self)

    def get_task(self, id):
        """Gibt die Aufgabe mit der ID zurück.
        Parameters
        -----------
        id: :class:`int`
            Die ID der Aufgabe, nach der gesucht werden soll.
        Returns
        --------
        :class:`Task`
            Die Aufgabe oder ``None``, falls diese nicht gefunden wird.
        """
        try:
            response = self.session.get(self.url + "iserv/exercise/show/" + str(id), headers=self._headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml")
                title = soup.find("span", {"class": "bc breadcrumb-current"}).text
                trs = soup.find("tbody", {"class": "bb0"}).find_all("tr")
                description = soup.find("div", {"class": "text-break-word p-3"}).text
                while description.startswith("\n"):
                    description = description[1:]
                while description.endswith("\n") or description[-1:].encode() == b"\xc2\xa0":
                    description = description[:-1]
                teachername = trs[0].find("td").text
                if teachername.__contains__(","):
                    split = teachername.split(", ")
                    teacher = LiteUser(split[1] + " " + split[0], trs[0].find("td").find("a")["href"].split(":")[1].split("@")[0], trs[0].find("td").find("a")["href"].split(":")[1].split("?")[0], firstname=split[1], lastname=split[0], client=self)
                else:
                    teacher = LiteUser(teachername, trs[0].find("td").find("a")["href"].split(":")[1].split("@")[0], trs[0].find("td").find("a")["href"].split(":")[1].split("?")[0], client=self)
                start = datetime.datetime.strptime(trs[1].find("td").text, '%d.%m.%Y %H:%M')
                end = datetime.datetime.strptime(trs[2].find("td").text, '%d.%m.%Y %H:%M')
                tags = []
                for a in trs[3].find("td").find_all("a"):
                    tags.append(a.text[1:])
                done = None
                feedback = None
                attachments = []
                table = soup.find("table", {"class": "table table-condensed mt0"})
                if table:
                    for a in table.find("tbody").find_all("tr"):
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

    def get_all_tasks(self, status="current", tags=None):
        """Gibt alle gefundenen Aufgaben zurück
        Parameters
        -----------
        status: Optional[:class:`str`]
            `"all"` für alle Aufgaben,
            `"current"` für aktuelle Aufgaben,
            `"past"` für vergangene Aufgaben.
        tags: Optional[List[:class:`str`]]
            Eine Liste mit Tags, nach denen die Aufgaben gefiltert werden sollen.
        Returns
        --------
        List[:class:`LiteTask`]
            Eine Liste der Aufgaben in Form von :class:`LiteTask`s.
        """
        try:
            if status in ["all", "current", "past"]:
                args = "?filter%5Bstatus%5D=" + status
                if tags is not None:
                    tag_list = {}
                    response = self.session.get(self.url + "iserv/exercise", headers=self._headers)
                    soup = BeautifulSoup(response.text, "lxml")
                    sels = soup.find("select", {"class": "form-control selectpicker show-tick", "title" : "Tags"})
                    for t in sels.find_all("option"):
                        tag_list[t.text.lower()] = t["value"]
                    for tag in tags:
                        if tag.lower() in tag_list:
                            args += "&filter%5Btag%5D%5B%5D=" + tag_list[tag.lower()]
                response = self.session.get(self.url + "iserv/exercise" + args, headers=self._headers)
                soup = BeautifulSoup(response.text, "lxml")
                table = soup.find("table", {"id": "crud-table"}).find("tbody")
                tasks = []
                for tr in table.find_all("tr"):
                    tds = tr.find_all("td")
                    title = tds[0].find("a").text
                    id = int(tds[0].find("a")["href"].split("/")[-1])
                    start = datetime.datetime.strptime(tds[1]["data-sort"], '%Y%m%d')
                    end = datetime.datetime.strptime(tds[2]["data-sort"], '%Y%m%d%H%M%S')
                    tags = []
                    for span in tds[3].find_all("span"):
                        tags.append(span.text)
                    done = tds[4].find("span") is not None
                    feedback = tds[5].find("span") is not None
                    tasks.append(LiteTask(title, id, start, end, tags, done, feedback, client=self))
                return tasks
        except:
            raise
            return []