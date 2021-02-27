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

class IServFile():
    """Das Feedback einer Aufgabe

    Attributes
    -----------
    name: :class:`str`
        Der Dateiname.
    url: :class:`str`
        Die URL der Datei
    raw_size: :class:`int`
        Die Dateigröße in bytes.
    size: :class:`str`
        Die Dateigröße als Text, so wie sie auf IServ steht.
    time: :class:`datetime.datetime`
        Die Zeit von abgegebenen Datein,
        ``None`` falls diese nicht sichtbar ist
    """

    def __init__(self, name, url, raw_size, size, time):
        self.name = name
        self.url = url
        self.size = size
        self.raw_size = raw_size
        self.time = time

    def __repr__(self):
        return '<iserv.IServFile name="%s" url="%s" raw_size=%s>' % (self.name, self.url, self. raw_size)

    def __str__(self):
        return '<iserv.IServFile name="%s" url="%s" raw_size=%s>' % (self.name, self.url, self. raw_size)
