#include <iostream>

using namespace std;

int main(){

    long long  x, y;
    cin >> x >> y;
    long long z = (100*y) / x ;

    if(z >= 99){
        cout << -1 << endl;
        return 0;
    }

    long long right = 1000000000;
    long long left = 0, result = -1;

    while(left <= right){
        long long mid = (left + right)/2 ;
        long long temp = (100 * (y + mid)) / (x + mid);
        if(temp > z){
            result = mid;
            right = mid - 1;
        }else {
            left = mid + 1;
        }
    }

    cout << result << endl;
    return 0;

}