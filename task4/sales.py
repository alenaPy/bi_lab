class Sales(object):

    def __init__(self, first_name, last_name, product_name,
                 product_number, cost, tax,
                 amount_sold=1):
        self.first_name = first_name
        self.last_name = last_name
        self.product_name = product_name
        self.product_number = product_number
        self.cost = cost
        self.tax = tax
        self.amount_sold = amount_sold

    def print_all_information(self):

        print(' First name: {} \n Last name: {} \n '
              'Product name: {} \n '
              'Product number: {} '
              '\n Cost: {} \n Tax: {} \n '
              'Sale: {}'.format(self.first_name, self.last_name,
                                self.product_name,
                                self.product_number, self.cost,
                                self.tax, self.amount_sold))

    def count_amount_sold(self):

        self.amount_sold = self.cost + self.tax
        return self


Sale_1 = Sales('Aryna', 'Kandrashevich', 'dress',
               150002, 20.5, 1.75)
Sale_1.print_all_information()
Sale_1.count_amount_sold()
print('___________________________')
Sale_1.print_all_information()
