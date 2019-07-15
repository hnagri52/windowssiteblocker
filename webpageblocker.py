import time
from datetime import datetime as dt

host_temp = "hosts"
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
bad_sites = ['facebook.com', 'www.facebook.com',
             'www.gmail.com', 'www.twitter.com', 'instagram.com']
print(dt.now())

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours!")
        try:
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for site in bad_sites:
                    if site in content:
                        pass
                    else:
                        file.write(redirect+" "+site+"\n")
        except Exception as e:
            print(e)
    else:
        try:
            with open(hosts_path, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(site in line for site in bad_sites):
                        file.write(line)
                file.truncate()
            print("Time to do whatever")
        except Exception as e:
            print(e)
    time.sleep(10)
