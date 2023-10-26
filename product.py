class Product:
    def __init__(self, name, bought_with=None):
        if len(name) <= 2:
            raise 'invalid name'
        self.name = name
        if bought_with is None:
            self.bought_with = {}
        else:
            self.bought_with = dict(bought_with)

    def __repr__(self):
        return f"name:{self.name} "

    def update(self, product_names):
        for product_name in product_names:
            self.bought_with[product_name] = self.bought_with.get(product_name, 0) + 1

    def get_recommendations(self, k):
        result = []
        new_dict = dict(self.bought_with)
        for i in range(k):
            max_buy = max(new_dict, key=new_dict.get)
            if new_dict[max_buy] > 0:
                result.append(max_buy)
                new_dict[max_buy] = 0
        print(result)
        return result




