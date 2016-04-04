#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;


void selection_sort(vector<int>& v)
{
  for (int i = 0; i < v.size()-1; ++i) {
    int imin = i;
    for (int j = i; j < v.size(); ++j){
      if (v[j] < v[imin]) imin = j;
    }
    if (imin != i){
      int aux = v[i];
      v[i] = v[imin];
      v[imin] = aux;
    }
  }
}

int main()
{
  int Start = clock();
  vector<int> v(100000000);
  for (int i=0; i<v.size(); ++i) v[i] = rand();
  selection_sort(v);
  cout << "--- " << (clock() - Start)/double(CLOCKS_PER_SEC) << " seconds ---" << endl;
}
