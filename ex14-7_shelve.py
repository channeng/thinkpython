import shelve

db = shelve.open("captions.db","c")

#Loads data into dictionary
# db['test_shelve'] = [12,23,34]
# db.close()

#Unloads data from dictionary
print db['test_shelve']