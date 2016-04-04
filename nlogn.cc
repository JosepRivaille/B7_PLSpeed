#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

void merge (vector<int> &v, int e, int m, int d)
{
	vector<int> B(d - e + 1);
	int i = e;
	int j = m + 1;
	int k = 0;
	while (i <= m and j<=d) {
		if (v[i] <= v[j]) B[k++] = v[i++];
		else B[k++] = v[j++];
	}
	while (i <= m) B[k++] = v[i++];
	while (j <= d) B[k++] = v[j++];
	for (k = 0; k <= d - e; ++k) v[e+k] = B[k];
}

void mergesort(vector<int> v, int e, int d)
{
	if (e < d) {
		int m = (e + d)/2;
		mergesort(v,e,m);
		mergesort(v,m+1,d);
		merge(v,e,m,d);
	}
}

int main()
{
	int Start = clock();
	vector<int> v(10000000);
	srand(time(NULL));
	for (int i = 0; i < 10000000; i++) {
		v[i] = rand() % 10000001;
	}
	mergesort(v, 0, 9999999);
	cout << "--- " << (clock() - Start)/double(CLOCKS_PER_SEC) << " seconds ---" << endl;
}
