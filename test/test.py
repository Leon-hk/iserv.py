
url = ""
username = ""
pw = ""













import iserv

client = iserv.Client(url, username, pw)

task = client.get_task(4060)
print(task.title)
print(task.description)
print(task.tags)
print(task.start)
print(task.end)
print(task.attachments)










