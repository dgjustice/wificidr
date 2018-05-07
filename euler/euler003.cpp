#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isPrime(int n){
    if(n < 2) return false;
    if(n == 2) return true;
    if((n & 1) == 0) return false;
    for(int i = 3; (i * i) <= n; i += 2){
        if(n % i == 0 ) return false;
    }
    return true;
}

long getFactor(long n){
    long o = n;
    // if n is even
    if((n & 1) == 0){
        while(n > 1){
            if((n & 1) == 0){
                n /= 2;   
            } else {
                break;
            }
        }
        if(n == 1){
            return 2;
        }
    }
    // cout << "for with :" << n << endl;
    for(long i = 3; i*i <= n; i += 2){
        if((n % i) == 0){
            // cout << "check: " << i << endl;
            n /= i;
            // because += 2 at end of for
            i = 1;
            // cout << "i: " << i << " n: " << n << endl;
        }
    }
    if(n > 2){
        return n;
    }
    else {
        return o;
    }
}

/*
1 2 5 10
1 2 4 5 10 20
1 2 4 5 10 20 25 50 100
1 2 3 6 11 22 33 66
1 2 31 62
*/

int main(){
    // get data
    int t;
    cin >> t;
    vector<long> vals;
    for(int a0 = 0; a0 < t; a0++){
        long n;
        cin >> n;
        vals.push_back(n);
    }

    // do stuff
    for(int j = 0; j < t; j++){
        long n = vals[j];
        long o = getFactor(n);
        // cout << "biggest: " << o << endl;
        cout << o << endl;
    }

    return 0;
}
