#include <iostream>
#include <cmath>

int main()
{
    float a, b, c;
    std::cout << "please enter a, b, and c:\n";
    std::cin >> a >> b >> c;

    // solve
    float disc;
    disc = b*b - 4*a*c;

    // (-b + sqrt(disc)) / 2a
    std::cout << disc << "\n";

    float root1, root2;
    root1 = (-b + sqrt(disc)) / 2*a;
    root2 = (-b - sqrt(disc)) / 2*a;
    std::cout << root1 << root2;
}