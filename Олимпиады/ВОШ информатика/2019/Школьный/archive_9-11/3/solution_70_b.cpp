#include<iostream>
using namespace std;

int main()
{
    int a, b, ans;
    cin >> a >> b;
    ans = b - 1;
    while (ans % a != 1)
        ans += b;
    cout << ans << endl;
}

