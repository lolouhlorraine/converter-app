class Converter:

    def __init__(self, decimal_val):
        self.decimal = decimal_val

    def convert_decimal(self):
        decimal = self.decimal
        radix = 16

        dict_val = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        rem_list =[]
        hex = ""

        # if decimal is negative value
        decimal = abs(decimal) if decimal < 0 else decimal

        if decimal < radix:
            if decimal in dict_val:
                return dict_val[decimal]
            else:
                return decimal
        
        if decimal >= radix:
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
