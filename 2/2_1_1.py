class translator:
    
    def deciToRoman(self, num):

        roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        str = ''
        while num != 0 :
            for n in reversed(roman) :
                if roman[n] <= num :
                    num -= roman[n]
                    str += n
                    break
        return str

    def romanToDeci(self, s):

        roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        num = 0
        c = 0
        for i in range(0,len(s),1) :
            if c != 0 :
                c = 0
                continue
            for n in reversed(roman) : 
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