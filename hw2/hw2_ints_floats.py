# Copyright 2022 Hyunsoo Kim hkim42@bu.edu

import numpy
from time import time


def string_to_float(ret):
    
    nbyte = len(ret)/8
    float_type = None
    if nbyte == 2:
        float_type = numpy.float16
    if nbyte == 4:
        float_type = numpy.float32
    if nbyte == 8:
        float_type = numpy.float64
    
    # parse ret by bytes
    list_str = []
    while(len(list_str) < nbyte): 
        list_str.append(ret[:8])
        ret = ret[8:]
        
    # convert string to int
    list_bytes = []
    for str_bytes in list_str:
        list_bytes = [int(str_bytes, 2)] + list_bytes # reverse order to compensate endianness
        
    ret = numpy.frombuffer(bytes(list_bytes), dtype=float_type)
    return ret[0]


def float_to_string(f):

    byte_f = f.tobytes()
    nbyte = len(byte_f)
    
    ret = ""
    for i in range(0, nbyte):
        str_bytes = bin(byte_f[i])[2:] # convert each byte to string
        while(len(str_bytes) < 8):
            str_bytes = "0" + str_bytes # pad with 0s on MSB side
        ret = str_bytes + ret # concat all
    return ret


def show_integer_properties():
    Table = "{:<6} {:<22} {:<22} {:<22}"
    print(Table.format("Bytes","Largest Unsigned Int","Minimum Signed Int","Maximum Signed Int"))
    
    for ii in range(1, 9):
        int_largest_unsigned_int = 2**(8*ii)-1
        int_minimum_signed_int = -(int_largest_unsigned_int+1 >> 1)
        int_maximum_signed_int = (int_largest_unsigned_int-1) >> 1
        print(Table.format(str(ii), str(int_largest_unsigned_int), str(int_minimum_signed_int), str(int_maximum_signed_int)))


def estimate_wrap_around():
    
    m = numpy.array([1], dtype=numpy.int16)
    seconds_start = time()
    while m[0] > 0:
        m[0] += 1
    seconds_runtime = time() - seconds_start
    str_line1 = "measured 16-bit time (microseconds): " + str(seconds_runtime * 1e6)
    
    str_line0 = "estimated 8-bit time (nanoseconds): " + str(seconds_runtime * 2**(8-16) * 1e9)
    str_line2 = "estimated 32-bit time (seconds): " + str(seconds_runtime * 2**(32-16))
    str_line3 = "estimated 64-bit time (years): " + str(seconds_runtime * 2**(64-16) /60/60/365)
    
    print(str_line0)
    print(str_line1)
    print(str_line2)
    print(str_line3)


def maximum_consecutive_int_value(arg):
    fbits = None
    ebias = None
    nbyte = None
    
    if arg == numpy.float16:
        fbits = 10
        ebias = -15
        nbyte = 2
        
    if arg == numpy.float32:
        fbits = 23
        ebias = -127
        nbyte = 4
        
    if arg == numpy.float64:
        fbits = 52
        ebias = -1023
        nbyte = 8
        
    ret = bin(fbits-ebias+1)[2:] # compute exponent into string
    ret = "0" + ret + "0"*fbits # "bitshift" exponent to right place
    
    return string_to_float(ret)


def largest_double():
    
    fbits = 52
    ebits = 11
    
    ret = bin((2**ebits)-2)[2:] # compute exponent into string
    ret = "0" + ret + "1"*fbits # "bitshift" exponent to right place and pad with 1s
    
    return string_to_float(ret)


def smallest_double():
    
    nbyte = 8
    
    ret = "0"*(nbyte*8-1) + "1" # all 0s except the LSB
    
    return string_to_float(ret)    


def largest_single():
    
    fbits = 23
    ebits = 8
    
    ret = bin((2**ebits)-2)[2:] # compute exponent into string
    ret = "0" + ret + "1"*fbits # "bitshift" exponent to right place and pad with 1s
    
    return string_to_float(ret)


def smallest_single():
    
    nbyte = 4
    
    ret = "0"*(nbyte*8-1) + "1" # all 0s except the LSB
    
    return string_to_float(ret)


def breakdown_float(f, /):
    
    ret = {"sign": None, "fraction": None, "exponent": None, "subnormal": None}
    fbits = None
    ebits = None
    
    if type(f) == numpy.float16:
        fbits = 10
        ebits = 5
    
    if type(f) == numpy.float32:
        fbits = 23
        ebits = 8
    
    if type(f) == numpy.float64:
        fbits = 52
        ebits = 11

    str_f = float_to_string(f)
    
    ret["sign"] = int(str_f[0], 2)
    ret["exponent"] = int(str_f[1:1+ebits], 2)
    ret["fraction"] = int(str_f[2+ebits:2+ebits+fbits], 2)
    ret["subnormal"] = ret["exponent"] == 0
    
    return ret


def construct_float(float_parms, /, *, float_type=float, subnormal=False):
    
    fbits = None
    ebits = None
    
    if float_type == numpy.float16:
        fbits = 10
        ebits = 5
    
    if float_type == numpy.float32 or float_type == float:
        fbits = 23
        ebits = 8
    
    if float_type == numpy.float64:
        fbits = 52
        ebits = 11
    
    sign = float_parms["sign"]
    if subnormal:
        exponent = 0
    else:
        exponent = float_parms["exponent"]
    fraction = float_parms["fraction"]
    
    sign = str(sign)
    exponent = bin(exponent)[2:]
    fraction = bin(fraction)[2:]
    
    if(len(exponent) > ebits or len(fraction) > fbits):
        raise ValueError("inconstructible float!")
    
    while(len(exponent) < ebits):
        exponent = "0" + exponent
    while(len(fraction) < fbits):
        fraction = "0" + fraction
        
    str_f = sign+exponent+fraction
    
    return string_to_float(str_f)


def get_next_float(start_float, /, *, index=1):
    
    restore_type = False
    float_type = type(start_float)
    
    if(float_type == float):
        start_float = numpy.float32(start_float)
        restore_type = True
    elif(float_type != numpy.float16 and
        float_type != numpy.float32 and
        float_type != numpy.float64):
        raise TypeError("wrong start_float type!", float_type)
        
    if(index <= 0):
        raise ValueError("non-positive index!", index)
       
    index_type = type(index)
    if(index_type != int and
      index_type != numpy.intx):
        raise TypeError("wrong index type!", index_type)
    
    str_ret = float_to_string(start_float)
    list_ret = list(str_ret)
    
    while(index > 0):
        for i in range(len(list_ret)-1, -1, -1):
            if list_ret[i] == "0":
                list_ret[i] = "1"
                index -= 1
                break
            else:
                list_ret[i] = "0"
            
    str_ret = "".join(list_ret)
    ret = string_to_float(str_ret)
    
    if restore_type:
        return float(ret)
    else:
        return ret


def main():
    show_integer_properties()
    estimate_wrap_around()
    print(maximum_consecutive_int_value(numpy.float16))
    print(maximum_consecutive_int_value(numpy.float32))
    print(maximum_consecutive_int_value(numpy.float64))
    print(largest_double())
    print(smallest_double())
    print(largest_single())
    print(smallest_single())
    print(breakdown_float(numpy.float64(2.5)))
    print(construct_float({'sign': 0, 'fraction': 1125899906842624, 'exponent': 1024}, float_type=numpy.float64))
    print(get_next_float(2.5))

if __name__ == "__main__":
    main()