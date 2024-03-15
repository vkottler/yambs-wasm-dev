/* toolchain */
#include <iostream>

/* internal */
#include "example/sample.h"

namespace Example
{

void method1(void)
{
    int a = 4;
    for (int i = 0; i < 1000; i++)
    {
        a *= 2;
    }

    std::cout << "method1 ran." << std::endl;

    (void)a;
}

void method2(void)
{
    int a = 2;
    for (int i = 0; i < 1000; i++)
    {
        a *= 2;
    }

    std::cout << "method2 ran." << std::endl;

    (void)a;
}

} // namespace Example
