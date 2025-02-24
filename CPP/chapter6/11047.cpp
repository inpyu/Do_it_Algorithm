#include <iostream>
#include <vector>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int num, money;
    cin >> num >> money;

    vector<int> A(num);

    for(int i =0 ; i< num ; i++){
        cin >> A[i];
    }

    int count = 0;

    for(int i = num - 1; i >=0 ; i--){
        if(A[i] <= money){
            count += (money / A[i]);
            money = money % A[i];
        }
    }

    cout << count << "\n";


}