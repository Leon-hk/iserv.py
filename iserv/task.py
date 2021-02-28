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

class LiteTask:
    """Die Lite-Klasse der Klasse :class:`Task`. Sie enthält nur Grundlegende Informationen der Aufgabe, um die volle Aufgabe zu bekommen ``task()`` ausführen.

    Attributes
    -----------
    title: :class:`str`
        Der Aufgabentitel, der in der Vorschau steht.
    id: :class:`int`
        Die Aufgaben ID.
    start: :class:`datetime.datetime`
        Der Starttermin der Aufgabe.
    end: :class:`datetime.datetime`
        Der Abgabetermin der Aufgabe.
    tags: List[:class:`str`]
        Eine Liste mit den Tags der Aufgabe.
    done: :class:`bool`
        ``True`` wenn die Aufgabe erledigt ist,
        ``False`` wenn sie noch nicht erledigt wurde.
    feedback: :class:`bool`
        ``True`` wenn eine Rückmeldung erfolgt ist,
        ``False`` wenn keine Rückmeldung erfolgt ist.
    """

    def __init__(self, title, id, start, end, tags, done, feedback, client=None):
        self.title = title
        self.id = id
        self.start = start
        self.end = end
        self.tags = tags
        self.done = done
        self.feedback = feedback
        self._client = client

    def task(self):
        return self._client.get_task(self.id)


class Task(LiteTask):
    """Eine IServ Aufgabe, diese kann vom Typ :class:`FileTask` oder :class:`TextTask` sein.

    Attributes
    -----------
    title: :class:`str`
        Der Aufgabentitel, der in der Vorschau steht.
    description: :class:`str`
        Die ausführliche Aufgabenbeschreibung.
    teacher: :class:`LiteUser`
        Der `LiteUser` des Lehrers, der die Aufgabe erstellt hat.
    id: :class:`int`
        Die Aufgaben ID.
    start: :class:`datetime.datetime`
        Der Starttermin der Aufgabe.
    end: :class:`datetime.datetime`
        Der Abgabetermin der Aufgabe.
    tags: List[:class:`str`]
        Eine Liste mit den Tags der Aufgabe.
    done: :class:`str`/List[:class:`IServFile`]
        ``True`` wenn die Aufgabe erledigt ist,
        ``None`` wenn sie noch nicht erledigt wurde.
    feedback: :class:`Feedback`
        ``Feedback`` wenn eine Rückmeldung gegeben wurde,
        ``None`` wenn keine Rückmeldung gegeben wurde.
    attachments: List[:class:`IServFile`]
        Eine Liste der sich im Anhang befindlichen Dateien in Form von `IServFile`s.
    """

    def __init__(self, title, description, teacher, id, start, end, tags, done, feedback, attachments):
        self.description = description
        self.teacher = teacher
        self.attachments = attachments
        super().__init__(title, id, start, end, tags, done, feedback)


class TextTask(Task):
    """Eine :class:`Task`, bei der die Abgabe in Form eines Textes erfolgt

    Attributes
    -----------
    title: :class:`str`
        Der Aufgabentitel, der in der Vorschau steht.
    description: :class:`str`
        Die ausführliche Aufgabenbeschreibung.
    teacher: :class:`User`
        Der `User` des Lehrers, der die Aufgabe erstellt hat.
    id: :class:`int`
        Die Aufgaben ID.
    start: :class:`datetime.datetime`
        Der Starttermin der Aufgabe.
    end: :class:`datetime.datetime`
        Der Abgabetermin der Aufgabe.
    tags: List[:class:`str`]
        Eine Liste mit den Tags der Aufgabe.
    done: :class:`str`
        ``str`` mit dem abgegebenen Text, wenn die Aufgabe erledigt ist,
        ``None`` wenn sie noch nicht erledigt wurde.
    feedback: :class:`Feedback`
        ``Feedback`` wenn eine Rückmeldung gegeben wurde,
        ``None`` wenn keine Rückmeldung gegeben wurde.
    attachments: List[:class:`IServFile`]
        Eine Liste der sich im Anhang befindlichen Dateien in Form von `IServFile`s.
    """

    def __init__(self, title, description, teacher, id, start, end, tags, done, feedback, attachments):
        super().__init__(title, description, teacher, id, start, end, tags, done, feedback, attachments)

    def __repr__(self):
        return '<iserv.TextTask title="%s" id=%s>' % (self.title, self.id)

    def __str__(self):
        return '<iserv.TextTask title="%s" id=%s>' % (self.title, self.id)

class FileTask(Task):
    """Eine :class:`Task`, bei der die Abgabe in Form eines Textes erfolgt

    Attributes
    -----------
    title: :class:`str`
        Der Aufgabentitel, der in der Vorschau steht.
    description: :class:`str`
        Die ausführliche Aufgabenbeschreibung.
    teacher: :class:`User`
        Der `User` des Lehrers, der die Aufgabe erstellt hat.
    id: :class:`int`
        Die Aufgaben ID.
    start: :class:`datetime.datetime`
        Der Starttermin der Aufgabe.
    end: :class:`datetime.datetime`
        Der Abgabetermin der Aufgabe.
    tags: List[:class:`str`]
        Eine Liste mit den Tags der Aufgabe.
    done: List[:class:`IServFile`]
        List[:class:`IServFile`] mit den abgegebenen Dateien, wenn die Aufgabe erledigt ist,
        ``None`` wenn sie noch nicht erledigt wurde.
    feedback: :class:`Feedback`
        ``Feedback`` wenn eine Rückmeldung gegeben wurde,
        ``None`` wenn keine Rückmeldung gegeben wurde.
    attachments: List[:class:`IServFile`]
        Eine Liste der sich im Anhang befindlichen Dateien in Form von `IServFile`s.
    """

    def __init__(self, title, description, teacher, id, start, end, tags, done, feedback, attachments):
        super().__init__(title, description, teacher, id, start, end, tags, done, feedback, attachments)

    def __repr__(self):
        return '<iserv.FileTask title="%s" id=%s>' % (self.title, self.id)

    def __str__(self):
        return '<iserv.FileTask title="%s" id=%s>' % (self.title, self.id)

class BoolTask(Task):
    """Eine :class:`Task`, bei der die Abgabe in Form von Ja/Nein erfolgt

    Attributes
    -----------
    title: :class:`str`
        Der Aufgabentitel, der in der Vorschau steht.
    description: :class:`str`
        Die ausführliche Aufgabenbeschreibung.
    teacher: :class:`User`
        Der `User` des Lehrers, der die Aufgabe erstellt hat.
    id: :class:`int`
        Die Aufgaben ID.
    start: :class:`datetime.datetime`
        Der Starttermin der Aufgabe.
    end: :class:`datetime.datetime`
        Der Abgabetermin der Aufgabe.
    tags: List[:class:`str`]
        Eine Liste mit den Tags der Aufgabe.
    done: :class:`bool`
        ``True`` wenn die Aufgabe mit "Ja" bestätigt wurde,
        ``False`` wenn sie noch nicht bestätigt wurde.
    feedback: :class:`Feedback`
        ``Feedback`` wenn eine Rückmeldung gegeben wurde,
        ``None`` wenn keine Rückmeldung gegeben wurde.
    attachments: List[:class:`IServFile`]
        Eine Liste der sich im Anhang befindlichen Dateien in Form von `IServFile`s.
    """

    def __init__(self, title, description, teacher, id, start, end, tags, done, feedback, attachments):
        super().__init__(title, description, teacher, id, start, end, tags, done, feedback, attachments)

    def __repr__(self):
        return '<iserv.BoolTask title="%s" id=%s>' % (self.title, self.id)

    def __str__(self):
        return '<iserv.BoolTask title="%s" id=%s>' % (self.title, self.id)
