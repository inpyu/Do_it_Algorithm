#include <iostream>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, question;
    int A[100001] = {};
    cin >> n >> question;

    for (int i = 1 ; i <= n ; i ++){
        int temp;
        cin >> temp;
        A[i] = A[i-1] + temp;
    }

    for(int i = 0; i < question ; i++){
        int start, end;
        cin >> start >> end;
        cout << A[end] - A[start -1] << "\n";
    }
    
}