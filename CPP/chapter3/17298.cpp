#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> numList(n,0);

    for(int i=0 ; i<n ; i++){
        cin >> numList[i];
    }

    stack<int> myStack;
    vector<int> answer(n,0);

    myStack.push(0);
    for(int i = 1 ; i < n ; i++){
        while(!myStack.empty() && numList[myStack.top()] < numList[i]){
            answer[myStack.top()] = numList[i];
            myStack.pop();
        }
        myStack.push(i);
    }
    while(!myStack.empty()){
        answer[myStack.top()] = -1;
        myStack.pop();
    }

    for(int i = 0; i < n ; i++){
        cout << answer[i] << " ";
    }


}