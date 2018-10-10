class SortedCustomer(type):
    def __iter__(cls):
        all_cust = cls._all_cust
        all_cust.sort(key=lambda cust: cust.cust_prefs_count, reverse=False)
        return iter(all_cust)


class Customer(metaclass=SortedCustomer):
    _all_cust= []

    def __init__(self, cust_id, cust_prefs, cust_prefs_count):
        self._all_cust.append(self)
        self.cust_id = cust_id
        self.cust_prefs = cust_prefs
        self.cust_prefs_count = cust_prefs_count

    def print_cust_vars(self):
        print(self.cust_id, self.cust_prefs, self.cust_prefs_count)
