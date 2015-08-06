import anydbm

db = anydbm.open('captions.db','c')
print db['cleese.png']

db.close()