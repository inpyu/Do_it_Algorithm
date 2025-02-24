#include <iostream>
#include <vector>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m ;

    vector<int> A(n);
    int start = 0;
    int end = 0;

    for(int i = 0 ; i< n ; i++){
        cin >> A[i];
        if(start < A[i]){
            start = A[i];
        }
        end = end + A[i];
    }

    while(start <= end){
        int middle = (start + end) / 2;
        int sum = 0;
        int count = 0;

        for(int i = 0 ; i < n ; i++){
            if(sum + A[i]  > middle){
                count ++;
                sum = 0;
            }
            sum = sum + A[i];
        }
        if( sum != 0){
            count ++;
        }
        if( count > m){
            start = middle + 1;
        }
        else{
            end = middle -1;
        }
    }

    cout << start << "\n";




}