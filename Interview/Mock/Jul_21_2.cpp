#include <vector>
#include <iostream>
#include <deque>
#include <bits/stdc++.h>
using namespace std;

int shortestSubarray(vector<int>& A, int K) {
    vector<int>Q(A.size()+1,0);
    deque<int>dq;
    int minlen=INT_MAX;
    int i;
    dq.push_back(0);
    for(i=0;i<A.size();i++)
    {
        Q[i+1]=Q[i]+A[i];
        while(!dq.empty()&&Q[i+1]<=Q[dq.back()])
        {
            dq.pop_back();
        }
        while(!dq.empty()&&(Q[i+1]-Q[dq.front()]>=K))
        {
            minlen=min(minlen,i+1-dq.front());
            dq.pop_front();
        }
        dq.push_back(i+1);
    }
    if(minlen==INT_MAX) return -1;
    return minlen;
}

int main() {
    int K;
    cin >> K;
    int i = 0, num = 0;

    vector<int> A;
    while (cin >> num) {
        cin >> A[i];
        i++;
    }

    cout << shortestSubarray(A, K);

    return 0;
}
