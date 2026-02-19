ZONE_FILE = "/etc/bind/db.networkdirection.net"

with open(ZONE_FILE, "r") as file:
    lines = file.readlines()

lines.pop()

def writeit(hostname, ip):
    to_write = f"{hostname} IN A {ip}\n"
    lines.append(to_write)

    for line in lines:
        print(line)

    with open(ZONE_FILE, "w") as file:
        file.writelines(lines)

writeit("xyz", "192.168.200.223")

