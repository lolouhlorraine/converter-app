class Converter:

    def __init__(self, decimal_val):
        self.decimal = decimal_val
        self.dict_val = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        self.radix = 16

    def convert_big_decimal(self):
        decimal = self.decimal
        radix = self.radix
        dict_val = self.dict_val

        rem_list =[]
        hex = ""   

        while int(decimal) > 0:
            decimal = decimal / radix
            float_val = decimal - int(decimal)
            rem_list.append(int(float_val * radix))
        rem_list.reverse()

        for rem in rem_list:
            if rem in dict_val:
                rem = dict_val[rem]
            hex += str(rem)
        return hex

    def convert_small_decimal(self):
        if self.decimal in self.dict_val:
            return self.dict_val[self.decimal]
        return str(self.decimal)
