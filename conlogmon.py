import socket
import csv
import time


def is_connected_to_internet():
  REMOTE_SERVER = "www.google.com"
  try:
    # Resolve the hostname
    host = socket.gethostbyname(REMOTE_SERVER)
    # Attempt to create a socket
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

while(True):
    now = time.strftime("%c")
    connection_status = is_connected_to_internet()

    print(now),
    print(" "),
    print(connection_status)

    row = {'time':now, 'connection_status':connection_status}
    with open('some.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        writer.writerows([row])

    time.sleep(1)




