#include <iostream>
#include <vector>
#include <stdlib.h>
#include <ctime>
using namespace std;


int dicot_search(vector<int> &v, int x, int l, int r)
{
	while (l <= r) {
		int m = (l+r)/2;
		if (v[m] == x) return m;
		else if (v[m] < x) l = m+1;
		else r =  m-1;
	}
	return -1;
}


int main() {
  int Start = clock();
  vector<int> v(10000000);
  for (int i = 0; i < 10000000; ++i)
  	v[i] = i;
  dicot_search(v, rand()%10000000, 0, 9999999);
  cout << "--- " << (clock() - Start)/double(CLOCKS_PER_SEC) << " seconds ---" << endl;
}