// Copyright 2022 Hyunsoo Kim hkim42@bu.edu

#include <iostream>

#define TYPE    long unsigned int

using namespace std;

int main()
{
    while(1)
    {
        // init
        TYPE input;
        std::cout << "\n";
        std::cin >> input;

        // we will only do first half of divisors
        TYPE *_2nd_half = (TYPE*) malloc(0);
        int len_half = 0;

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
            while(divisor*divisor < input)
            {
                TYPE quotient = input / divisor;

                // if input is evenly divisible by divisor, quotient will not lose precision
                if(input == quotient * divisor)
                {
                    std::cout << "+" << divisor;
                    divsum += divisor + quotient;

                    // since 2nd half is computed out of order, save them in an array
                    _2nd_half = (TYPE*) realloc(_2nd_half, ++len_half*sizeof(TYPE));
                    _2nd_half[len_half-1] = quotient;
                }
                ++divisor;
            }

            // handle edge case where input is integer-squared
            if(divisor*divisor == input)
                std::cout << "+" << divisor;

            // append other half of divisors computed before
            for(int i = 0; i < len_half; ++i)
                std::cout << "+" << _2nd_half[len_half-1-i];

            // final output
            std::cout << " = " << divsum;
        }
    }
}