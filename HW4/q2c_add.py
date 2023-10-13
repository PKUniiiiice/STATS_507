from collections import Counter
senders = Counter()
receivers = Counter()

ip2ip = re.compile(f"({ip}) \u2192 ({ip})")
with gzip.open("SkypeIRC.txt.gz", "rt") as f:
    for l in f:
        ips = re.search(ip2ip, l)
        if ips is not None:
           temp = ips.group().split('\u2192')
           s, r  = (u.strip() for u in temp)
           senders[s] = senders.get(s,0) + 1
           receivers[r] = receivers.get(r,0) + 1
