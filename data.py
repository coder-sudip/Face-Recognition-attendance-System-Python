def load_data(file_path):
    data = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                if ':' in line:
                    key, value = line.strip().split(':', 1)
                    data[key] = value
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return data


def save_data(file_path, data):
    with open(file_path, "w") as f:  # overwrite the file with updated data
        for key, value in data.items():
            f.write(f"{key}:{value}\n")


def add_or_update(file_path, key, value):
    data = load_data(file_path)
    data[key] = value  # add or overwrite
    save_data(file_path, data)
    print(f"Saved: {key}:{value}")


# Example usage:
file_path = "data.txt"

if __name__ == "__main__":
    user_id = input("Enter ID: ").strip()
    user_name = input("Enter Name: ")
    add_or_update(file_path, user_id, user_name)
