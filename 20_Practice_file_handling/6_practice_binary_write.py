
import pickle

name = "Jon"
age = 22
address = "KTM"

with open("info.dat", "wb") as fp:
    pickle.dump(name, fp)
    pickle.dump(age, fp)
    pickle.dump(address, fp)

print("Successful")
