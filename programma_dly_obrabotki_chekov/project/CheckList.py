class CheckList:

    def __init__(self) -> list:
        self.purchases = []

    def add_product(self, product) -> list:
        self.purchases.append(product)