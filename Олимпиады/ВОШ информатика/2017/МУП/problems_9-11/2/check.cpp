#include "testlib.h"
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
    registerTestlibCmd(argc, argv);
    const int MAXN = 2000000000;
    int n = inf.readInt(1, MAXN);
    int n3 = ouf.readInt(0, MAXN);
    int n4 = ouf.readInt(0, MAXN);
    if ((n == 1 || n == 2 || n == 5) && n3 == 0 && n4 == 0)
        quitf(_ok, "Correct answer - no solution");
    if (n3 == 0 && n4 == 0)
        quitf(_wa, "Program output \"0 0\", but solution exists");
    if (3 * n3 + 4 * n4 == n)
        quitf(_ok, "Correct answer");
    else
        quitf(_wa, "Wrong answer: %d * 3 + %d * 4 != %d", n3, n4, n);
}

