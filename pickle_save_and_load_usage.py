import pickle

# create some object:
example_dict = {1:"f"}

# save the object to a file:
pickle_out = open("dict.picke", "wb") # wb - write bites
pickle.dump(example_dict, pickle_out)
pickle_out.close()

print("Saved to dict.picke")

# load the object:
picke_in = open("dict.picke", "rb") # rb - read bites
loaded_dict = pickle.load(picke_in)

print("Loaded!")
print(example_dict)
print(loaded_dict)