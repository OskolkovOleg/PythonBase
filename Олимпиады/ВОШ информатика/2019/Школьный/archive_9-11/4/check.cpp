#include "testlib.h"
#include<iostream>
#include<vector>

using namespace std;

// inf - input data
// ans - correct answer
// ouf - student's answer
// run: check inf ouf ans

int main(int argc, char ** argv)
{
    registerTestlibCmd(argc, argv);
    string s = inf.readLine();
    long long n = s.size();
    long long answ = ouf.readLong();
    if (answ < 0 || answ > n)
        quitf(_wa, "Incorrect value");
    long long corr = ans.readLong();
    if (answ == 0 && corr == 0)
        quitf(_ok, "");
    else if (answ == 0)
        quitf(_wa, "Program output is 0, but solution exists");
    else
    {
        s.erase(answ - 1, 1);
        string s1(s);
        reverse(s1.begin(), s1.end());
        if (s == s1)
            quitf(_ok, "");
        else
            quitf(_wa, "After removing symbol # %d, string isn't palindrome", (int)answ);
    }
}
