#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){


    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    priority_queue<int, vector<int>> q;

    int n;

    cin >> n;
    for(int i = 0 ; i < n ; i++){
        int num;
        cin >> num;
        if(num == 0){
            if(q.empty()){
                cout << 0 << "\n";
            }else{
                cout << q.top() << "\n";
                q.pop();
            }
        }else{
            q.push(num);
        }
    }

    return 0;
}