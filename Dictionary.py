#Dictionary
#Define a dictionary and run multiple times
D1={"City":"Mumbai",
    "City":"Pune",  #recent value will be stored and display
    "State":"Maharashtra",
    "Country":"India"}
print(D1)
print(D1)

#define dictionary and add new elements
D2={"City":"Mumbai",
    "State":"Maharashtra",
    "Country":"India"}
print(D2)
D2["Population"]=20000000
print(D2)

#key missing but value is assigned
D3={"City":"Mumbai",
    "State":"Maharashtra", 
    "Country":"India"}
print(D3)
D3.pop("Country")
print(D3)
D3.popitem() #key missing but value is assigned
print(D3)

#printing keys and values separately
D4={"City":"Mumbai",
    "State":"Maharashtra", 
    "Country":"India"}
print(D4.keys())
print(D4.values())

#if updated once then it will be updated for all the times
D5={"City":"Mumbai",
    "State":"Maharashtra", 
    "Country":"India"}
D5["City"]="Pune"
print(D5)
D5.update({"City":"Nagpur"})
print(D5)

#check if key is present in dictionary or not
D6={"Age":30,
    "Name":"John",}
if "Age" in D6:
    print("Key is present",D6["Age"])
else:
    print("Key is not present")

#to invert the key and value in dictionary
D7={"City":"Mumbai",
    "State":"Maharashtra", 
    "Country":"India"}
D7_inverted={v:k for k,v in D7.items()}
print(D7_inverted)