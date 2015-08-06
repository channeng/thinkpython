import pickle
import anydbm


db = anydbm.open("captions.db","c")

# LOADING into DB
# t1 = [1,2,3]
# s= pickle.dumps(t1)
# db["test"]

#UNLOADING into DB
unload = pickle.loads(db['test'])
print unload

db.close()