# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.

 

# Example 1:

# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.

# Example 2:

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 3:

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


def intToRoman(self, num: int) -> str:
        rom = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC",
               100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        pst = 1
        vals = []
        roman = ""
        while num > 0:
            digit = num % 10
            vals.insert(0, digit*pst)
            num //= 10
            pst *= 10
        
        for i in vals:
            if i in rom:
                roman += rom[i]
            else:
                if i < 4:
                   roman += rom[1] * i
                elif i < 9:
                    roman += rom[5] + (rom[1] * (i - 5))
                elif i % 10 == 0 and i < 40:
                    roman += rom[10] * (i//10)
                elif i % 10 == 0 and i < 90:
                    roman += rom[50] + rom[10] * ((i-50)//10)
                elif i % 100 == 0 and i < 400:
                    roman += rom[100] * (i//100)
                elif i % 100 == 0 and i < 900:
                    roman += rom[500] + rom[100] * ((i-500)//100)
                elif i % 1000 == 0 and i < 4000:
                    roman += rom[1000] * (i//1000)
                elif i % 1000 == 0 and i < 9000:
                    roman += rom[5000] + rom[1000] * ((i-5000)//1000)
        return roman