from decimal import Decimal


class RationalNumber:
    def __init__(self, num1=1, denom1=1, num2=1, denom2=1) -> None:
        self.numerator1 = num1
        self.denom1 = denom1
        self.numerator2 = num2
        self.denom2 = denom2
        self.denom_mult = self.denom1 * self.denom2
        self.factorial_mult1 = (self.denom_mult // self.denom1) * self.numerator1
        self.factorial_mult2 = (self.denom_mult // self.denom2) * self.numerator2

    def __str__(self):
        gcf1 = self.det_gcf(self.numerator1, self.denom1)
        gcf2 = self.det_gcf(self.numerator2, self.denom2)
        return f"First Fraction: ({self.numerator1 // gcf1}/{self.denom1 // gcf1}), " \
               f"Second Fraction: ({self.numerator2 // gcf2}/{self.denom2 // gcf2})"

    

    def add(self):
        added_nums = self.factorial_mult1 + self.factorial_mult2
        gcf = RationalNumber.det_gcf(added_nums, self.denom_mult)
        return f"{added_nums // gcf}/{self.denom_mult // gcf}"

    def subtract(self):
        sub_nums = self.factorial_mult1 - abs(self.factorial_mult2)
        if sub_nums == 0: return 0
        gcf = self.det_gcf(sub_nums, self.denom_mult)
        return f"{sub_nums // gcf}/{self.denom_mult // gcf}"

    def multiply(self):
        mult_num = self.numerator1 * self.numerator2
        mult_denum = self.denom1 * self.denom2
        gcf = self.det_gcf(mult_num, mult_denum)
        return f"{mult_num // gcf}/{mult_denum // gcf}"

    def divide(self):
        div_num = self.numerator1 * self.denom2
        div_denum = self.denom1 * self.numerator2
        gcf = self.det_gcf(div_num, div_denum)
        numer_div = div_num // gcf
        denum_div = div_denum // gcf
        div = (numer_div) / (denum_div)
        if div.is_integer(): return f"{numer_div}/{denum_div} = {int(div)}"
        return f"{numer_div}/{denum_div}"

    @staticmethod
    def print_float(numerator, denumerator):
        return numerator / denumerator

    @staticmethod
    def det_gcf(first_num, second_num):
        common_factors = []
        for num in range(second_num):
            if not (num) or (first_num % num): continue
            if second_num % num == 0: common_factors.append(num)
            if num == first_num + 1: break

        return max(common_factors)


rational = RationalNumber()
print(RationalNumber.print_float(3,4))
print(rational)
print(rational.subtract())

# print(rational.det_gcf(70, 140))
