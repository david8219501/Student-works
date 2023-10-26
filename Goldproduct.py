from product import Product


class GoldProduct(Product):
    def __init__(self, name, amount, bought_with=None):
        super().__init__(name, bought_with)
        self.amount = amount

    def __repr__(self):
        parent_repr = super().__repr__()
        return f'{parent_repr}({self.amount} units left)'

    def update(self, product_names):
        super().update(product_names)
        for i in range(len(product_names)):
            self.amount += -1

    def get_recommendations(self, k):
        result = super().get_recommendations(k)
        for i in range(len(result)):
            recommendation = result[i]
            if self.bought_with[recommendation] < 10:
                result.pop(i)
        return result


