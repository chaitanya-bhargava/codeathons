#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int k = 1; k <= t; k++)
    {
        string I;
        cin >> I;
        string P;
        cin >> P;
        if (P.length() < I.length())
        {
            cout << "Case #" << k << ": IMPOSSIBLE" << endl;
        }
        else
        {
            int i = 0, j = 0;
            int ans = 0;
            while (i < I.length() && j < P.length())
            {
                if (I[i] == P[j])
                {
                    i++;
                    j++;
                }
                else
                {
                    ans++;
                    j++;
                }
            }
            ans += P.length() - j;
            if (i != I.length())
            {
                cout << "Case #" << k << ": IMPOSSIBLE" << endl;
            }
            else
            {
                cout << "Case #" << k << ": " << ans << endl;
            }
        }
    }
    return 0;
}