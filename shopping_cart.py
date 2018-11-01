
class ShoppingCart:

    def __init__(self,_employee_discount = None):
        self._total = 0
        self._items = []
        self._employee_discount = _employee_discount

    def get_total(self):
        return self._total

    def set_total(self,price):
        self._total += price

    total = property(get_total,set_total)
####################################################
    def get_items(self):
        return self._items

    def set_items(self,name,price):
        item = {name : price}
        self._items.append(item)

    items = property(get_items,set_items)
######################################################
    def get_employee_discount(self):
        self._employee_discount
    def set_employee_discount(self,discount):
        pass
    employee_discount = property(get_employee_discount,set_employee_discount)
####################################################################
    def add_item(self, name, price, quantity = None):
        if quantity is not None:
            totalp = price*quantity
            for i in range(0,quantity):
                self.set_items(name,price)
            self.set_total(totalp)
        else:
            self.set_total(price)
            self.set_items(name,price)
        return self.total

    def mean_item_price(self):
         return self.total/len(self.items)

    def median_item_price(self):
        import statistics
        listt = []
        for item in self.items:
            listt.append(list(item.values()).pop())
        return statistics.median(listt)
########################################################################
    def apply_discount(self):
        if self._employee_discount == None:
            return 'Sorry, there is no discount to apply to your cart :('
        else:
            return self.total - ((self._employee_discount/100)*self.total)
########################################################################
    def item_names(self):
        list_dict = self.items
        return list(map(lambda dict : (list(dict.keys())).pop(), list_dict))
########################################################################
    def void_last_item(self):
        if self.items == []:
            return "There are no items in your cart!"
        else:
            price = int(-1*((list((self.items.pop()).values())).pop()))
            self.set_total(price)
            return self.total
