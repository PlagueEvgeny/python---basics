row_record = '217.168.17.5 - - [ 17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
correct_request_IP_address = '217.168.17.5'
correct_request_datetime = '17/May/2015:08:05:12'

request_IP_address = row_record.split() [0]
print(request_IP_address)
request_datetime = row_record.split() [4]
print(request_datetime)

assert request_IP_address == correct_request_IP_address
assert request_datetime == correct_request_datetime


