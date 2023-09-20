#include<iostream>
using namespace std;

int main()
{
    int a, b;
    long long s = 0;
    cin >> a >> b;
    for (int i = a + a % 2; i <= b; i += 2)
        s += i;
    for (int i = a + 1 - a % 2; i <= b; i += 2)
        s -= i;
    cout << s << endl;
}
