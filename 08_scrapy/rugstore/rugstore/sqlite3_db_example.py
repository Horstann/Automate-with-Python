import sqlite3

# Connection
conn = sqlite3.connect('sqlite3_db_example.db') # Creates a file called database.db in whichever directory your terminal is in
# Cursor
curr = conn.cursor()

### SQL statements! ###
# curr.execute("""
#     CREATE TABLE rugs(
#         title TEXT,
#         link TEXT,
#         price REAL
#     )
# """)

curr.execute("""
    INSERT INTO rugs
    values('Rug1', 'lol.com', '3.99')
""")
curr.execute("""
    SELECT * FROM rugs
""")

# Commit those SQL statements
conn.commit()
# Close connection
conn.close()