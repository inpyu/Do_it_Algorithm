#include <iostream>

using namespace std;

long long gcd(long long a, long long b);

int main(){


    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long a, b;
    cin >> a >> b;

    long long result = gcd(a, b);
    while(result > 0){
        cout << 1;
        result--;
    }
    cout << endl;

}

long long gcd(long long a, long long b){
    if(b == 0){
        return a;
    }
    else{
        return gcd(b, a % b);
    }
}