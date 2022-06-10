import re
strings = []
sids = []
with open("log.txt", 'r') as f:
    strings = f.readlines()
for i in strings:
    ip, data = i.split(' - - ')
    if ip == '10.1.192.38':
        res = re.search(r"sid=/(.*?)/&", data)
        sid = res.group(1)
        sids.append(sid)
print(*sorted(sids), sep="\n")
