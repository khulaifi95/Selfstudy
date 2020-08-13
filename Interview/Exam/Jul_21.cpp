#include <bits/stdc++.h> 
using namespace std;

int findSmallestDifference(int A[], int B[],
							int m, int n) {
	sort(A, A+m);
	sort(B, B+n);

	int a = 0, b = 0;

	int result = INT_MAX;

	while (a < m && b < n) {
		if (abs(A[a] - B[b]) < result) {
			result = abs(A[a] - B[b]);

		if (A[a] < B[b])
			a++;

		else
			b++;
		}

	}
	return result;
}

int main()
{
	int m;
	cin >> m;
	int A[m];
	for(int i = 0;i < m;i++)	cin >> A[i];

	int n;
	cin >> n;
	int B[n];
	for(int i = 0;i < n;i++)	cin >> B[i];

	cout << findSmallestDifference(A,B,m,n);

	return 0;
}
