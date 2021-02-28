
url = ""
username = ""
pw = ""

















import iserv

client = iserv.Client(url, username, pw)

task = client.get_task(4339)
print(task.title)
print(task.description)
print(task.teacher.name)
print(task.teacher.firstname)
print(task.teacher.lastname)
print(task.teacher.username)
print(task.teacher.mail)
print(task.tags)
print(task.start)
print(task.end)
print(task.attachments)










