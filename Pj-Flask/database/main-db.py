import oracledb

connection = oracledb.connect(
    user="willianUserTestes",
    password="senha",
    dsn="localhost/xe")

print("\n\nSuccessfully connected to Oracle Database\n")

cursor = connection.cursor()
# DROP TABLE AMOSTRAS PURGE;
try:
    cursor.execute("""
        create table amostras (
        id number generated always as identity,
        co number(*),
        so2 number(*),
        no2 number(*),
        o3 number(*),
        mp25 number(*),
        mp10 number(*),
        primary key (id))""")
except:
    print("Table already created\n")

def insertSamplesDb(co, so2, no2, o3, mp25, mp10):
    cursor.executemany(f"INSERT into amostras(co, so2, no2, o3, mp25, mp10) values ({co}, {so2}, {no2}, {o3}, {mp25}, {mp10})")
    print(cursor.rowcount, "Rows Inserted\n")
    connection.commit()

def deleteSample(id):
    cursor.execute(f'DELETE from amostras where ID={id}')
    connection.commit()

def updateSamples(id,co, so2, no2, o3, mp25, mp10):
    cursor.execute(f'UPDATE amostras set co={co}, so2={so2}, no2={no2}, o3={o3}, mp25={mp25}, mp10={mp10} where id={id}')
    connection.commit()

def printSamples():
    samplesDb=[]
    for row in cursor.execute('SELECT * from amostras'):
        print(row,"\n")
        samplesDb.append(row)
    return samplesDb
