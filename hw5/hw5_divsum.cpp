// Copyright 2022 Hyunsoo Kim hkim42@bu.edu

#include <iostream>
#include <cstdint>

#define TYPE    long long unsigned int

using namespace std;

int main()
{
    while(1)
    {
        // init
        TYPE input;
        std::cin >> input;

        // exit condition
        if(input == 0)
            return 0;
        else
        {
            // exclude 1 as base case
            TYPE divsum = 1;
            std::cout << input << ": 1";

            // start from 2
            TYPE divisor = 2;

            // quit when first half of divisors are computed
            while(divisor < input)
            {
                TYPE quotient = input / divisor;

                // if input is evenly divisible by divisor, quotient will not lose precision
                if(input == quotient * divisor)
                {
                    std::cout << "+" << divisor;
                    divsum += divisor;
                }
                ++divisor;
            }

            // final output
            std::cout << " = " << divsum << "\n";
        }
    }
}