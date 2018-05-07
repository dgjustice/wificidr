#include <queue>
#include <iostream>

using namespace std;


int main(){
    int t;
    cin >> t;
	// read data
    for(int a0 = 0; a0 < t; a0++){
        long n;
        cin >> n;
		// run test
        long t = 2;
        long et = 2;
        long front = 0;
        queue <long> q;
        q.push(1);
        q.push(2);
        while(t <= n){
            // discard top element
            front = q.front();
            t += front;
            if(((t & 1) == 0)&&(t <= n)){
                et += t;
            }
            q.pop();
            q.push(t);
		}	
        cout << et << endl;
    }

    return 0;
}
