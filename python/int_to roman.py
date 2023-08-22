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