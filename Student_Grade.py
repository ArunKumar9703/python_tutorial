student=[{"Std_Name": "John Doe", "Std_Grade": "A"},
         {"Std_Name": "Jane Smith", "Std_Grade": "B"},
         {"Std_Name": "Alice Johnson", "Std_Grade": "C"}]
print(student[0]["Std_Name"],student[0]["Std_Grade"])
student[0]["Std_Grade"]= "B"
print(student[0]["Std_Name"],student[0]["Std_Grade"])
if (student[0]["Std_Grade"] == "A"):
    print("Excellent")
else:
    print("Good")
print(type(student[0].keys()))
print(type(student[0].values()))
