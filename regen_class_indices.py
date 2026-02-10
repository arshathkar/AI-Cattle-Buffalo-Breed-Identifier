import os
import json

BASE_DIR = os.path.join(os.path.dirname(__file__), "breeds")
print("Looking for classes in:", BASE_DIR)
print("Folders:", os.listdir(BASE_DIR))


# IMPORTANT: same sorting Keras uses (alphabetical)
class_names = sorted([
    d for d in os.listdir(BASE_DIR)
    if os.path.isdir(os.path.join(BASE_DIR, d))
])

class_indices = {name: idx for idx, name in enumerate(class_names)}

with open("models/class_indices.json", "w") as f:
    json.dump(class_indices, f, indent=2)

print("Saved class_indices.json")
print(class_indices)
