#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    int n, m ;
    cin  >> n >> m;

    vector<int> A(n,0);

    for(int i = 0 ; i< n ; i++){
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    int count = 0;
    int start = 0;
    int end = n-1;
    while(start < end){
        if(A[start] + A[end] < m){
            start ++;
        }else if(A[start] + A[end] > m){
            end --;
        }else{
            count ++;
            start ++;
            end --;
        }
    }

    cout << count << "\n";

}