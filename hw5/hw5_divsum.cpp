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

        TYPE checksum = 0;
        TYPE last_divisor = 0;

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

                    checksum = checksum * divisor + last_divisor;
                    last_divisor = divisor;
                }
                ++divisor;
            }

            // handle edge case where input is integer-squared
            if(divisor*divisor == input)
                std::cout << "+" << divisor;

            while(last_divisor > 0)
            {
                std::cout << "+" << (input/last_divisor);

                TYPE temp = checksum;
                checksum = checksum / last_divisor;
                last_divisor = temp % last_divisor;
            }

            // final output
            std::cout << " = " << divsum << "\n";
        }
    }
}