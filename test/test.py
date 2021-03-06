
url = ""
username = ""
pw = ""

















import iserv

client = iserv.Client(url, username, pw)

messenger = client.MessengerClient()

messenger.run()

#response = client.session.get('https://kwg-hx.de/iserv/messenger/authenticate', headers=client._headers)
#print(response)
#print(response.text)
"""
tasks = client.get_all_tasks(tags=["chemie"])
for task in tasks:
    print(task.title)
    print(task.id)
    print(task.tags)
    print(task.start)
    print(task.end)
    print(task.done)
    print(task.feedback)


task = tasks[0].task()
print(task.title)
print(task.description)
print(task.teacher.name)
print(task.teacher.firstname)
print(task.teacher.lastname)
print(task.teacher.username)
print(task.teacher.picture.url)
print(task.teacher.mail)
print(task.tags)
print(task.start)
print(task.end)
print(task.attachments)
"""
