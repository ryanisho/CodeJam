#include <bits/stdc++.h>

using namespace std;

int sqr[51][51], n, k, t;
bool row_safe[51][51], col_safe[51][51], solved;

void solver(int row, int col, int m)
{
    if (row == n && col == n + 1 && m == k && !solved)
    {
        solved = true;
        cout << "Case #" << t << ": "
            << "POSSIBLE\n";
        for (int i = 1; i <= n; ++i)
        {
            for (int j = 1; j <= n; ++j)
            {
            cout << sqr[i][j] << " ";
        }
        cout << "\n";
    }
    return;
}
else if (row > n)
{
    return;
}
else if (col > n)
{
    solver(row +1, 1, m);
}
for(int i = 1; i <= n && !solved; ++i)
{
    if (!row_safe[row][i] && !col_safe[col][i])
    {
        row_safe[row][i] = col_safe[col][i] = true;
        if (row == col)
        {
            m += i;
        }
        sqr[row][col] = i;

        solver(row, col + 1, m);

        row_safe[row][i] = col_safe[col][i] = false;
        if (row == col)
        {
            m -= i;
        }
        sqr[row][col] = 0;
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (t = 1; t <= T; ++t)
    {
        cin >> n >> k;
        solver(1, 1, 0);
        if (!solved)
        {
            cout << "Case #" << t << ": "
                << "IMPOSSIBLE\n";
        }
        solved = false;
    }
    return 0;
}