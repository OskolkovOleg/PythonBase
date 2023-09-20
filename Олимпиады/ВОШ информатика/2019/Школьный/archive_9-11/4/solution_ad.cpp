#include <iostream>

using namespace std;

bool isPalindrome(string str)
{
	int l = 0;
	int h = str.length() - 1;

	while (h > l)
	{
		if (str[l++] != str[h--])
		{
			return false;
		}
	}
	return true;
}



int main(void)
{
	string s;
	int count = 0, index = -1;
	cin >> s;

	int n = s.length();

	for (int i = 0; i < n / 2; ++i) 
		if (s[i] != s[n - i - 1])
		{
			count++;
			if (index == -1) index = i;

		}

	if (count == 0)
	{
		cout << n / 2 + 1 << endl;
		return 0;
	}


	string t = s;
	t.erase(index, 1);

	if (isPalindrome(t))
	{
		cout << index + 1 << endl;
		return 0;
	}
	t = s;
	t.erase(s.length() - 1 - index, 1);

	if (isPalindrome(t))
	{
		cout << s.length() - index << endl;
		return 0;
	}

	cout << "0"<<endl;

	return 0;
}
