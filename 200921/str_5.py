row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
correct_resault = '217.168.17.5'

resault = row_record.split() [0]
print(resault)


assert resault == correct_resault
