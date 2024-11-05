class SuperStr(str):

    def is_palindrom(self):
        return self[::-1] == self
    
    def is_repeatence(self, s):
        if len(self) % len(s) != 0:
            return False
        else:
            for i in range(0, len(self), len(s)):
                if self[i:len(s)+i] == s:
                    i += len(s)
                    continue
                else:
                    return False
            return True
        
stringa = SuperStr("lalal")
print(stringa.is_palindrom())
print(stringa.is_repeatence("la"))