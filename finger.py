import socket


def parse_finger_output(response_string):
  record_delimiter = '-' * 35
  records_raw = response_string.split(record_delimiter)
  # Shave off extra information
  records_raw = records_raw[1:-1]
  if not records_raw:
    return []
  record_lines = [record.split('\r\n') for record in records_raw]

  # Clean records
  record_lines_stripped = []
  for record in record_lines:
    record_stripped = []
    for item  in record:
      item_stripped = item.strip()
      if item_stripped:
        # Don't include any empty rows
        record_stripped.append(item.strip())
    record_lines_stripped.append(record_stripped)

  # Parse data and put into a list of dicts
  record_dict_list = []
  for record in record_lines_stripped:
    record_dict = {}
    for item in record:
      item_split = item.split(': ')
      record_dict[item_split[0]] = item_split[1]
    record_dict_list.append(record_dict)
  return record_dict_list

def get_finger_data(resource, server, port=79):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((server, port))
  query = resource + '\r\n'
  sock.send(query.encode('utf-8'))
  response = ''
  while True:
    part = sock.recv(1024).decode()
    if not part:
      break
    else:
      response += part
  sock.close()
  return response

def finger(resource, server, port=79):
  data = get_finger_data(resource, server, port)
  return parse_finger_output(data)

if __name__ == '__main__':
  server = input('Enter a server: ')
  resource = input('Enter a resource to lookup: ')
  finger_results = finger(resource, server)
  # print(finger(resource, server))
  print(finger_results)

