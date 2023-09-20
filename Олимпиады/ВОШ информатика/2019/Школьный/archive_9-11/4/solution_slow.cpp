#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	string s, s1, s2;
	cin >> s;
	for (int i = 0; i < s.size(); ++i)
	{
		s1 = s;
		s1.erase(i, 1);
		s2 = s1;
		reverse(s2.begin(), s2.end());
		if (s1 == s2)
		{
			cout << i + 1 << endl;
			return 0;
		}
	}
	cout << 0 << endl;
}
