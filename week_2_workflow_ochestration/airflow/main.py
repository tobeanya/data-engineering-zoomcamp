import os
import json


url = "https://dummyjson.com/products"

os.makedirs("./data", exist_ok=True)
os.system(f"curl -o ./data/data.json {url}")

with open("./data/data.json", "r") as file:
    data = json.load(file)

columns_to_keep = ["id", "brand", "price"]

filtered_data = [
    {column: product.get(column, "N/A") for column in columns_to_keep}
    for product in data["products"]
]

with open("./data/products.json", "w") as file:
    json.dump(filtered_data, file, indent=4)