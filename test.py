class PizzaMaker:
    def __make_pepperoni(self):
        pass

    def _make_barbecue(self):
        pass


maker = PizzaMaker()
maker._make_barbecue()
print(PizzaMaker.__dict__.keys())
maker._PizzaMaker__make_pepperoni()