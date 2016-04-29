#include <vector>
#include <stdlib.h>
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

void mergesort(vector<int> &v, int e, int d)
{
	if (e < d) {
		int m = (e + d)/2;
		mergesort(v,e,m);
		mergesort(v,m+1,d);
		merge(v,e,m,d);
	}
}

int main(int argc, char *argv[])
{
  vector<int> v(argc - 1);
	for (int i = 1; i < argc; ++i)
		v[i-1] = atoi(argv[i]);
	mergesort(v, 0, argc - 2);
}
