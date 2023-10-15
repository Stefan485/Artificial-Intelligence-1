
# Open and read the text file
with open('sample.txt', 'r') as file:
    file_content = file.readlines()

# Initialize variables to store information
name = ""
age = 0
occupation = ""
location = ""

# Parse the content and extract information
for line in file_content:
    parts = line.strip().split(': ')
    if len(parts) == 2:
        key, value = parts
        if key == "Name":
            name = value
        elif key == "Age":
            age = int(value)
        elif key == "Occupation":
            occupation = value
        elif key == "Location":
            location = value

# Print the extracted information
print("Name:", name)
print("Age:", age)
print("Occupation:", occupation)
print("Location:", location)
