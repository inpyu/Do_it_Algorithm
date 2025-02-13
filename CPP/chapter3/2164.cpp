#include <iostream>
#include <queue>

using namespace std;

int main(){

    int n;
    cin >> n ;

    queue<int> myQueue;

    for(int i = 1 ; i <= n ; i++){
        myQueue.push(i);
    }

    while(myQueue.size() > 1){
        myQueue.pop();
        int number;
        number = myQueue.front();
        myQueue.pop();
        myQueue.push(number);
    }
    cout << myQueue.front();
}

