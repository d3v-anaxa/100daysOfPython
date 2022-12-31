# python v3.7 onwards, dictioneries are ordered 

dictionary = {
        "PRODUCT_NAME" : "TFT_1221",
        "MODEL_NAME" : "EDASCC1221"
        }

print("get() method ->", dictionary.get('ID')) # returns 'None' if key unavailabe
#print(dictionary['ID']) # returns error if key unavailabe

print("list of all keys ->", dictionary.keys()) # list of all keys
print("list of all values ->", dictionary.values()) # list of all values

# both lists above are printed in the same order

for key in dictionary.keys():
    print(f"Available key -> '{key}' & Value -> '{dictionary[key]}'")

for key, val in dictionary.items():
    print(f"{key} : {val}")
