def load_id_name_dict(filename):
    id_name_dict = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                id_name_dict[key.strip()] = value.strip()
    return id_name_dict

# Load the dictionary
id_name_map = load_id_name_dict("data.txt")

# Access name using ID
user_id = "5"
if user_id in id_name_map:
    print("Name for ID", user_id, "is", id_name_map[user_id])
else:
    print("ID not found")
