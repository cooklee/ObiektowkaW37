class Cart:

    def __init__(self):
        self.products = []

    def add(self, nazwa, cena):
        self.products.append((nazwa, cena))

    def summary(self):

        return self.products


class Discount20Percent(Cart):

    def summary(self):
        products = super().summary()
        new_proudcts = []
        for name, value in products:
            new_proudcts.append((name, 0.8 * value))

        return new_proudcts


class Above3ProductsCheapestFreeCart(Cart):

    def summary(self):

        products = super().summary()
        x = min(products, key=lambda x: x[1])
        index = products.index(x)
        products.pop(index)
        products.insert(index, (x[0], 0))
                # new_products = []
        # if len(products) >= 3:
        #     cheapest_index = 0
        #     min_price = products[0][1]
        #     new_products.append(products[0])
        #     for i in range(1, len(products)):
        #         if products[i][1] < min_price:
        #             cheapest_index = i
        #             min_price = products[i][1]
        #         new_products.append(products[i])
        #     x = new_products.pop(cheapest_index)
        #     new_products.insert(cheapest_index, (x[0], 0))
        #     return new_products
        return products


cart = Above3ProductsCheapestFreeCart()
cart.add("jabłka", 100)
cart.add("cebula", 102)
cart.add("ogórki", 10)
cart.add("koszula", 103)
for item in cart.summary():
    print(item)


