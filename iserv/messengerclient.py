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

import asyncio

class MessengerClient:
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

    def __init__(self, client):
        self.client = client
        response = client.session.get(self.client.url + "iserv/messenger/authenticate", headers=self.client._headers)
        self.access_token = response.json()["access_token"]
        self.event_loop = asyncio.get_event_loop()

    def run(self):
        params = (
            ('filter', '0'),
            ('timeout', '30000'),
            ('since', 's000000_0000000_00000_0000000_00000_0000000_0_000000_0'),
            ('access_token', self.access_token),
        )
        response = self.client.session.get(self.client.url + "_matrix/client/r0/sync", headers=self.client._headers, params=params)
        self.event_loop.run_until_complete(self.message_loop(response.json()["next_batch"]))

    async def message_loop(self, since):
        while True:
            params = (
                ('filter', '0'),
                ('timeout', '30000'),
                ('since', since),
                ('access_token', self.access_token),
            )
            response = self.client.session.get('https://kwg-hx.de/_matrix/client/r0/sync', headers=self.client._headers, params=params)
            since = response.json()["next_batch"]
            print(response.text)
