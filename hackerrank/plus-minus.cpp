#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
using std::fixed;

int main(){
    int p = 0;
    int m = 0;
    int z = 0;
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }

    for(int arr_i = 0;arr_i < n;arr_i++){
        if (arr[arr_i] > 0)
            p += 1;
        else if (arr[arr_i] < 0)
            m += 1;
        else if (arr[arr_i] == 0)
            z += 1;
    }
    float s = (float)arr.size();
    cout << (p/s) << endl;
    cout << (m/s) << endl;
    cout << (z/s) << endl;
    return 0;
}
