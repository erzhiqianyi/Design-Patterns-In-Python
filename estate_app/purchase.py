class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("Purchase details")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        return dict(
            price=input("Enter the selling price: "),
            taxes=input("Enter the estimated taxes: ")
        )
    prompt_init = staticmethod(prompt_init)
