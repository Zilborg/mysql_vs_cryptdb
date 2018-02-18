
import MySQLdb
import sys
import time


user = 'root'
table = 'people'
db = 'TESTC'
host = '0.0.0.0'


# doc       - 2 test:
#               * clear             +
#               * encrypt coloumn   +
# doccrypt  - 1 test                +
# my        - 2 test:
#               * full encryption          

NAMES = []
ADDRESS = []
NUMBERS = []
COUNTRY = []
EMAIL = []


with open('data/names.txt', 'r') as file:
    for line in file:
        NAMES.append(line[:-1])

with open('data/address2.txt', 'r') as file:
    for line in file:
        ADDRESS.append(line[:-1])

with open('data/numbers.txt', 'r') as file:
    for line in file:
        NUMBERS.append(line[:-1])

with open('data/country.txt', 'r') as file:
    for line in file:
        COUNTRY.append(line[:-1])

with open('data/email.txt', 'r') as file:
    for line in file:
        EMAIL.append(line[:-1])

# file_ad2 = open ('data/address2.txt', 'w')
# linein = ''
# count = 0
# for line in file_ad:
#     if line != '\n':
#         linein += line[:-1]
#         count += 1
#         if count == 2:
#             count = 0
#             file_ad2.write(linein+'\n')
#             linein = ''
# file_ad2.close()
# file_ad.close()

if len(sys.argv) > 1:
    if sys.argv[1] == "doc":       
        pas = 'letmein'
        port = 32772
        conn = MySQLdb.connect(host=host, port=port,  user=user, passwd=pas, \
        db=db)
        print("Connecting to Docker")

    if sys.argv[1] == "doccrypt":
        pas = 'letmein'
        port = 32771
        db = 'TESTC'
        conn = MySQLdb.connect(host=host, port=port,  user=user, passwd=pas, \
        db=db)
        print("Connecting to Docker with CryptDB")

    if sys.argv[1] == "my":
        conn = MySQLdb.connect(user=user, db=db) 
        print("Connecting to local")

    if sys.argv[1] == "andrew":
        host="172.17.0.2"
        pas="root"
        conn = MySQLdb.connect(user=user, host=host, passwd=pas, db=db) 
        print("Connecting to local") 


else:
    conn = MySQLdb.connect(user=user)

cursor = conn.cursor()
print("Inserting...")

if len(NAMES) != len(ADDRESS) or len(NAMES) != len(NUMBERS):
    print("Wrong count of lines")
    sys.exit()

cursor.execute("CREATE TABLE people2 (name VARCHAR(50), address VARCHAR(100), cell VARCHAR(15), \
    country VARCHAR(100), email VARCHAR(50), name1 VARCHAR(50), address1 VARCHAR(100), \
    cell1 VARCHAR(15), country1 VARCHAR(100), email1 VARCHAR(50));")

count = 0
start = time.time()

while count < len(NAMES):
    cursor.execute("INSERT INTO people2 (name, address, cell, country, email, name1, address1, cell1, country1, email1) \
    VALUES ('" + NAMES[count] + "', '" + ADDRESS[count] + "', '" + NUMBERS[count] + "', \
    '" + COUNTRY[count] + "','" + EMAIL[count] + "', '" + NAMES[count] + "', \
    '" + ADDRESS[count] + "', '" + NUMBERS[count] + "', '" + COUNTRY[count] + "','" + EMAIL[count] + "');")
    count += 1
conn.commit()
conn.close()
end = time.time() - start
print("Result: " + str(end))