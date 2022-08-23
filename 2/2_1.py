class translator:
    def deciToRoman(self, num):
        roman = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        str = ''
        while num != 0 :
            for n in roman :
                if roman[n] <= num :
                    num -= roman[n]
                    str += n
                    break
        return str
    def romanToDeci(self, s):
        roman = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        num = 0
        c = 0
        for i in range(0,len(s),1) :
            if c != 0 :
                c = 0
                continue
            for n in roman :
                if s[i] + s[i-len(s)+1] == n and i+1 < len(s) :
                    num += roman[n]
                    c = 1
                    break
                elif s[i] == n :
                    num += roman[n]
                    break
        return num
num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))