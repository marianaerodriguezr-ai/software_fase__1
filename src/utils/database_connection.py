import json

class DatabaseConnection:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.data = None

    def connect(self):
        try:
            with open(self.json_file_path, 'r') as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            self.data = None
            print("Error: json file not found.")

    def get_products(self):
        return self.data.get('products', []) if self.data else []

    def add_product(self, new_product):
        if not self.data:
            print("Error: something went wrong adding the product")
            return

        products = self.data.get('products', [])
        products.append(new_product)
        self.data['products'] = products

        with open(self.json_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

    def get_categories(self):
        return self.data.get('categories', []) if self.data else []

    def add_category(self, new_category):
        if not self.data:
            print("Error: something went wrong adding category")
            return

        categories = self.data.get('categories', [])
        categories.append(new_category)
        self.data['categories'] = categories

        with open(self.json_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

    def remove_category(self, category_name):
        if not self.data:
            print("Error: something went wrong removing category")
            return

        categories = self.data.get('categories', [])
        categories = [c for c in categories if c["name"] != category_name]
        self.data["categories"] = categories

        with open(self.json_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)

    def get_favorites(self):
        return self.data.get('favorites', []) if self.data else []

    def add_favorite(self, new_favorite):
        if not self.data:
            print("Error: something went wrong adding favorite product")
            return

        favorites = self.data.get('favorites', [])
        favorites.append(new_favorite)
        self.data['favorites'] = favorites

        with open(self.json_file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=4)
