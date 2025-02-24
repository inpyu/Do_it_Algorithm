#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int num;
    cin >> num;

    vector<pair<int,int>> A(num);

    for(int i=0;i<num;i++){

        cin >> A[i].second;
        cin >> A[i].first;
    }

    sort(A.begin(), A.end());

    int count = 0;
    int end = -1;

    for(int i = 0 ; i< num ; i++){
        if(A[i].second >= end){
            end = A[i].first;
            count ++;
        }
    }

    cout << count << "\n";


}