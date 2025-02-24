#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n ;
    vector<int> A(n);

    for(int i =0; i<n ; i++){
        cin >> A[i];
    }

    sort(A.begin(),A.end());

    int m;
    cin >> m;
    for(int i=0;i<m;i++){
        int number;
        cin >> number;

        int start = 0;
        int end =  A.size()-1;
        bool find= false;

        while(start <= end){
            int index = (start + end)/2;
            int value = A[index];
            if(value > number){
                end = index - 1;
            }else if(value < number){
                start = index +1;
            }else{
                find = true;
                break;
            }
        }

        if(find){
            cout << 1 << "\n";
        }else{
            cout << 0 << "\n";
        }


    }



}