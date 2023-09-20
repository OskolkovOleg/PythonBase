#include<iostream>
using namespace std;

int main()
{
    int a, b, s = 0;
    cin >> a >> b;
    for (int i = a; i <= b; ++i)
        if (i % 2 == 0)
            s += i;
        else
            s -= i;
    cout << s << endl;
}
