# Copyright 2022 Hyunsoo Kim hkim42@bu.edu


class Wedding:
    
    def __init__(self):
        pass
    
    
    def shuffle(self, guests):
        
        lg = len(guests)
        if(lg < 2):
            return guests
    
        l_shift = guests[1:] + guests[0]
        if(lg == 2):
            return [guests, l_shift]
        
        r_shift = guests[-1] + guests[:-1]
        
        overflow = self.__shuffle(guests[1:-1])
        for i in range(0, len(overflow)):
            overflow[i] = guests[-1] + overflow[i] + guests[0]
    
        return [l_shift, r_shift] + overflow + self.__shuffle(guests)
    
    
    def __shuffle(self, guests):
        
        if(len(guests) == 1):
            return [guests]
        if(len(guests) == 0):
            return [""]
        
        Y0 = self.__append_str_to_strs(guests[0], self.__shuffle(guests[1:]))
        Y1 = self.__append_str_to_strs(guests[1::-1], self.__shuffle(guests[2:]))
        
        return Y0 + Y1
    
    
    def __append_str_to_strs(self, string0, strings, string1=""):
        
        for ii in range(0, len(strings)):
            strings[ii] = string0 + strings[ii] + string1
            
        return strings
    
    
    def barriers(self, guests, bars):
        
        lb = len(bars)
        if(lb == 0):
            return self.shuffle(guests)
        
        bias = bars[0]
        guests = guests[bias:] + guests[:bias]
        for ii in range(0, lb):
            bars[ii] -= bias
        
        blocks = []
        if(lb < 2):
            blocks = [guests]
        else:
            blocks = self.__split_guests_with_bars(guests, bars)
        blocks = self.__expand_blocks(blocks)
        blocks = self.__barriers(blocks)
        blocks = self.__denormalize(blocks, bias)
        
        return blocks
        
#         ret = []
#         if(len(chunks) == 1):
#             ret = [self.__append_str_to_strs("|", chunks[0])]
#         else:
#             ret = self.__barriers(chunks)
            
#         return self.__denormalize(ret[0], bias)
        
    
    def __split_guests_with_bars(self, guests, bars):
        
        lb = len(bars)
        if(lb < 2):
            return [guests]
        
        ret = []
        for ii in range(0, lb-1):
            ret.append(guests[bars[ii]:bars[ii+1]])
        ret.append(guests[bars[-1]:])

        return ret
    
    
    def __expand_blocks(self, blocks):
        
        for ii in range(0, len(blocks)):
            blocks[ii] = self.__shuffle(blocks[ii])
        
        return blocks
    
    
#     def __append_strs_ot_str(self, strings, string):
        
#         if(strings == []):
#             return []
        
#         is_bar = not (strings[0][0] == "|")
        
#         return [(is_bar*"|") + strings[0] + "|" + string] + self.__append_strs_ot_str(strings[1:], string)
    
    
    def __append_strs_to_strs(self, dest_strs, src_strs):
        
        ret = []
        for dest_str in dest_strs:
            for src_str in src_strs:
                ret.append(dest_str + "|" + src_str)
        return ret
        
#         if(strs1 == []):
#             return []
        
#         return self.__append_strs_ot_str(strs0, strs1[0]) + self.__append_strs_ot_strs(strs0, strs1[1:])
    
    
    def __barriers(self, chunks):
        
        for ii in range(1, len(chunks)):
            chunks[0] = self.__append_strs_to_strs(chunks[0], chunks[ii])
        self.__append_str_to_strs("|", chunks[0])
        
        return chunks[0]
        
#         if(len(chunks) == 1):
#             return chunks
        
#         chunks[0] = self.__append_strs_to_strs(chunks[0], chunks[1])
#         chunks.pop(1)
        
#         return self.__barriers(chunks)
    
    
    def __denormalize(self, strs, shift):
        
        if(strs == []):
            return []
        
        for ii in range(0, len(strs)):
            strs[ii] = strs[ii][-shift:]+strs[ii][:-shift]
            
        return strs
        
        #return [strs[0][-shift:]+strs[0][:-shift]] + self.__denormalize(strs[1:], shift)


def  show_result(v, partial=False,ind=None):
  v.sort()
  if not partial:
    print(len(v),"\n".join(v),sep="\n")
  else:
    print(len(v),v[ind],sep="\n")




def standard_tests():
  standard = Wedding()
  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("WXYZ")
  show_result(res)

  res = standard.barriers("xyz", [0])
  show_result(res)

  res = standard.shuffle("abc")
  show_result(res)

  res = standard.shuffle("abcdefXY")
  show_result(res)

  res = standard.barriers("abcDEFxyz", [2, 5, 7])
  show_result(res)

  res = standard.barriers("ABCDef", [4])
  show_result(res)

  res = standard.barriers("bgywqa", [0, 1, 2, 4, 5])
  show_result(res)

  res = standard.barriers("n", [0])
  show_result(res)
  res = standard.shuffle("hi")
  show_result(res)



def main():

  print("""Type quit to exit.
Commands:
tests
s guests
b guests n barriers
sp guests ind
bp guests n barriers ind
""")
  w = Wedding()
  while True:
    asktype=input().split()
    if not asktype or asktype[0] == "quit":
      break;
    elif asktype[0] == "tests":
      standard_tests()
    elif asktype[0] == "s":
      guests = asktype[1]
      r = w.shuffle(guests)
      show_result(r);
    elif asktype[0] == "b":
      guests,nbar,bars = asktype[1],asktype[2],asktype[3:]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r)
    elif asktype[0] == "sp":
      guests,ind = asktype[1:]
      r = w.shuffle(guests);
      show_result(r, True, int(ind));
    elif asktype[0] == "bp":
      guests,nbar,bars,ind  = asktype[1],asktype[2],asktype[3:-1],asktype[-1]
      r = w.barriers(guests, [int(x) for x in bars])
      show_result(r, True, int(ind))
    

if __name__ == '__main__':
  main()
