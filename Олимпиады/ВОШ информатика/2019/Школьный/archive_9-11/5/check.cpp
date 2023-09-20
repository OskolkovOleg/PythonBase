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
    int n = inf.readInt();
    int m = inf.readInt();
    int k = inf.readInt();
    vector <string> out(n);
    out[0] = ouf.readLine("IMPOSSIBLE|[LRUD]+");
    if (out[0] == "IMPOSSIBLE")
    {
        if (k == n * m - 1)
            quitf(_ok, "Impossible");
        else
            quitf(_wa, "Output is IMPOSSIBLE, but solution exists");
    }
    for (int i = 1; i < n; ++i)
        out[i] = ouf.readLine("[LRUD]+");
    for (int i = 0; i < n; ++i)
    {
        if (out[i].size() != m)
            quitf(_pe, "Line # %d has incorrent length", i + 1);
        // cerr << "Got line *" << out[i] << "*\n";
    }
    vector <vector<int> > map(n, vector<int>(m));
    const int ESCAPED = 1;
    const int PRISONED = 2;
    int count = 0;
    for (int ii = 0; ii < n; ++ii)
        for (int jj = 0; jj < m; ++jj)
        {
            int i = ii;
            int j = jj;
            if (map[i][j] == 0)
            {
                // cerr << "Starting search from (" << i << ", " << j << ")" << endl;
                int status = 0;
                vector<pair<int, int> > path;
                while (i >= 0 && i < n && j >= 0 && j < m && map[i][j] == 0)
                {
                    if (find(path.begin(), path.end(), make_pair(i, j)) != path.end())
                    {
                        status = PRISONED;
                        break;
                    }
                    path.push_back(make_pair(i, j));
                    switch (out[i][j])
                    {
                        case 'L': --j; break;
                        case 'R': ++j; break;
                        case 'U': --i; break;
                        case 'D': ++i; break;
                        default: quitf(_fail, "Failed in switch");
                    }
                }
                if (i < 0 || i >= n || j < 0 || j >= m)
                    status = ESCAPED;
                else if (status == 0)
                    status = map[i][j];
                for (int k = 0; k < path.size(); ++k)
                {
                    // cerr << "Path: (" << path[k].first << ", " << path[k].second << ") set to " << status << endl;
                    map[path[k].first][path[k].second] = status;
                }
            }
            if (map[ii][jj] == ESCAPED)
                ++count;
        }
    // for (int i = 0; i < n; ++i)
    // {
    //     for (int j = 0; j < m; ++j)
    //         cerr << map[i][j];
    //     cerr << endl;
    // }
    if (count == k)
        quit(_ok, "OK");
    else
        quitf(_wa, "Escaped %d persons, instead of %d", count, k);
}
