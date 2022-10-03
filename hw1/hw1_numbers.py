# Copyright 2022 Hyunsoo Kim hkim42@bu.edu


def divisorsum(int_x):
    
    str_y = "1"
    int_sum = 1
    
    for i in range(2, int_x-1):
        if(int_x % i == 0):
            str_y += "+" + str(i)
            int_sum += i
            
    str_y += " = " + str(int_sum)
    
    return str_y


def convertbase(str_x, int_oldBase, int_newBase):
    
    int_val = 0
    
    for str_digit in str_x:
        int_val *= int_oldBase
        int_val += ord(str_digit) - ord("0")
        
    str_y = ""
        
    while(1):
        int_remainder = int_val % int_newBase
        str_y = chr(int_remainder + ord("0")) + str_y
        int_val = int_val // int_newBase
        if(int_val < int_newBase):
            str_y = chr(int_val + ord("0")) + str_y
            break
    
    return str_y


def heavy(int_y, int_N):
    
    list_prev = [int_y]
    
    while(1):
        int_next = 0
        while(int_y > 0):
            int_next += (int_y % int_N)**2
            int_y = int_y // int_N
        if(int_next == 1):
            return True
        elif int_next in list_prev:
            return False
        else:
            list_prev.append(int_next)
            int_y = int_next

def main():

    print("running test code for divisorsum")
    print("divisorsum(6)")
    print(divisorsum(6))
    print("divisorsum(888)")
    print(divisorsum(888))
    print("")

    print("running test code for convertbase")
    print("convertbase(convertbase(""8AB"", 20, 10), 10, 20)")
    print(convertbase(convertbase("8AB", 20, 10), 10, 20))
    print("convertbase(convertbase(""30"", 10, 16), 16, 10)")
    print(convertbase(convertbase('30', 10, 16), 16, 10))
    print("")

    print("running test code for heavy")
    print("heavy(4,10)")
    print(heavy(4,10))
    print("heavy(2211,10)")
    print(heavy(2211,10))
    print("heavy(23,2)")
    print(heavy(23,2))
    print("heavy(10111,2)")
    print(heavy(10111,2))
    print("heavy(12312,4000)")
    print(heavy(12312,4000))
    print("")

    print("done")

    return

if __name__ == "__main__":
    # main()
    print(type(convertbase("4291289", 10, 200)))
    print(convertbase("4291289", 10, 200))