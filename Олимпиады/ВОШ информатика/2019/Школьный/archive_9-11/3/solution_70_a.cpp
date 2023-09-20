#include<iostream>
using namespace std;

int main()
{
    int a, b, ans;
    cin >> a >> b;
    ans = 1;
    while (ans % b != b - 1)
        ans += a;
    cout << ans << endl;
}
