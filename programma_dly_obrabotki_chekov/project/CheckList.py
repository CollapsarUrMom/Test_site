class CheckList:

    def __init__(self) -> list:
        """Создание для словаря покупок"""
        self.purchases = []

    def add_product(self, product) -> list:
        """Добавление покупок"""
        self.purchases.append(product)