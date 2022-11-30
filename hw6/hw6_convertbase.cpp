// Copyright 2022 Hyunsoo Kim hkim42@bu.edu

#include <iostream>
#include <string>

using namespace std;

// count until null character
int my_strlen(char* input)
{
    int output = 0;
    while(*(input+output) != '\0')
        ++output;
    return output;
}

int my_atoi(char* input, int base)
{
    int len_input = my_strlen(input);
    int number = 0;
    for(int i = 0; i < len_input; ++i)
    {
        number *= base;
        number += *(input+i) - '0';
    }
    return number;
}

// the important part is the type conversion
// maybe casting works but i am too tired to check
char my_itoa(int input)
{
    return '0' + input;
}

void func(int input, int base)
{
    if(base > input)
    // get to msd first
        cout << my_itoa(input);
    else
    {
        // then start printing remainders
        func(input/base, base);
        cout << my_itoa(input % base);
    }
}

int main(int argc, char** argv)
{
    int old_base = my_atoi(argv[2], 10);
    int new_base = my_atoi(argv[3], 10);
    int number = my_atoi(argv[1], old_base);

    func(number, new_base);
    cout << '\n';

    return 0;
}