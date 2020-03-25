## SQL scripts
# INSERT INTO chitter VALUES 
# (2, 'firstuser', 'decmklfawkfle', '123@gmail.com', '2020-03-25');

# INSERT INTO chitter (username , encrypted_password )
# VALUES ('seconduser', '123u21u9u9498');

import psycopg2
import time

# Number of rows to add
n = 10000

# Generate single INSERT INTO query
single_query = '''INSERT INTO post (user_id, post_text)
                VALUES (1, 'All work and no play makes Jack a dull boy.');'''

# Generate big quer
big_query = "INSERT INTO post (user_id, post_text) VALUES"
for i in range(n):
    big_query += "(1, 'All work and no play makes Jack a dull boy.'),"

big_query = big_query.strip(',') + ';'

# Connect to database & create cursor
# password = open('password.txt','r').read()
conn = psycopg2.connect("dbname=sample_db user=postgres password=920506")
cur = conn.cursor()

# Time n individual queries
start = time.time()
for i in range(n):
    cur.execute(single_query)
conn.commit()
stop = time.time()
print("{} individual queries took {} seconds.".format(n, stop - start))

# Time the big query
start = time.time()
cur.execute(big_query)
conn.commit()
stop = time.time()
print("The big query with {} rows took {} seconds.".format(n, stop - start))

# Close both cursor and connection to database
cur.close()
conn.close()