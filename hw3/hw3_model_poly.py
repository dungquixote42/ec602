# Copyright 2022 Hyunsoo Kim hkim42@bu.edu

class Polynomial():
    
    def __init__(self, list_coeffs=[]):
        "Initialize self."
        num_coeffs = len(list_coeffs)
        self.dict_coeffs = {}
        for i in range(0, num_coeffs):
            self.dict_coeffs[i] = list_coeffs[num_coeffs-1-i]
        self.pop_zeros()
            
    def __getitem__(self, key):
        "Get self[key]"
        if key in self.dict_coeffs:
            return self.dict_coeffs[key]
        else:
            return 0
            
    def __setitem__(self, key, value):
        "Set self[key] to value."
        self.dict_coeffs[key] = value
            
    def __add__(self, poly):
        "Return self + poly."
        new_poly = Polynomial([])
        for k in self.dict_coeffs:
            new_poly[k] = self.dict_coeffs[k]
        for k in poly.dict_coeffs:
            if k in new_poly.dict_coeffs:
                new_poly[k] += poly.dict_coeffs[k]
            else:
                new_poly[k] = poly.dict_coeffs[k]
        new_poly.pop_zeros()
        return new_poly
    
    def __sub__(self, poly):
        "Return self - poly."
        new_poly = Polynomial([])
        for k in self.dict_coeffs:
            new_poly[k] = self.dict_coeffs[k]
        for k in poly.dict_coeffs:
            if k in new_poly.dict_coeffs:
                new_poly[k] -= poly.dict_coeffs[k]
            else:
                new_poly[k] = -poly.dict_coeffs[k]
        new_poly.pop_zeros()
        return new_poly
    
    def __mul__(self, poly):
        "Return self x poly."
        new_poly = Polynomial([])
        for ks in self.dict_coeffs:
            for kp in poly.dict_coeffs:
                if ks+kp in new_poly.dict_coeffs:
                    new_poly[ks+kp] += self.dict_coeffs[ks] * poly.dict_coeffs[kp]
                else:
                    new_poly[ks+kp] = self.dict_coeffs[ks] * poly.dict_coeffs[kp]
        new_poly.pop_zeros()
        return new_poly
    
    def __eq__(self, poly):
        "Return self == poly."
        for k in self.dict_coeffs:
            if k not in poly.dict_coeffs:
                return False
            if self.dict_coeffs[k] != poly.dict_coeffs[k]:
                return False
        for k in poly.dict_coeffs:
            if k not in self.dict_coeffs:
                return False
        return True
    
    def eval(self, x):
        "Evaluate Polynomial for actual value x."
        value = 0
        for k in self.dict_coeffs:
            value += self.dict_coeffs[k] * (x**k)
        return value
    
    def deriv(self):
        new_poly = Polynomial([])
        for k in self.dict_coeffs:
            new_poly[k-1] = self.dict_coeffs[k]*k
        new_poly.pop_zeros()
        return new_poly
    
    def pop(self, key):
        new_dict_coeffs = {}
        for k in self.dict_coeffs:
            if k != key:
                new_dict_coeffs[k] = self.dict_coeffs[k]
        self.dict_coeffs = new_dict_coeffs
        
    def pop_zeros(self):
        for k in self.dict_coeffs:
            if self.dict_coeffs[k] == 0:
                self.pop(k)
        

def main():
    p1 = Polynomial([4,0,1])
    print(p1[1] == 0)
    print(p1[10] == 0)
    print(p1[100000] == 0)


if __name__ == "__main__":
    main()