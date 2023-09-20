#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	string s;
	cin >> s;
	for (int k = 0; k < s.size(); ++k)
	{
		int i = 0;
		int j = s.size() - 1;
		do
		{
			if (i == k)
				++i;
			if (j == k)
				--j;
			if (s[i] != s[j])
				break;
			++i;
			--j;
		}
		while (i < j);
		if (i >= j)
		{
			cout << k + 1 << endl;
			return 0;
		}
	}
	cout << 0 << endl;
}
