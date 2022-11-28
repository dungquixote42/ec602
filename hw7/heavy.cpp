// Copyright 2022 Hyunsoo Kim hkim42@bu.edu

#include <vector>
#include <string>

using namespace std;

int cmd_to_int(char* input, int base)
{   
    int output = 0;
    int i_input = -1;
    while(input[++i_input] != '\0')
    {
        output *= base;
        output += input[i_input] - '0';
    }
    return output;
}

// better name pending
int foo(int input, int base)
{
    if(base > input)
        return input * input;
    else
        return (input % base) * (input % base) + foo(input / base, base);
}

bool is_in(vector<int> v, int number)
{
    for(int n : v)
    {
        if(n == number)
            return true;
    }
    return false;
}

int main(int argc, char** argv)
{
    // init input from command line
    int y = cmd_to_int(argv[1], 10);
    int N = cmd_to_int(argv[2], 10);

    // main loop
    std::vector<int> v  = {y};
    while(true)
    {
        if(y == 1)
            return 1;
        y = foo(y, N);
        if(is_in(v, y))
            return 0;
        v.push_back(y);
    }
}
