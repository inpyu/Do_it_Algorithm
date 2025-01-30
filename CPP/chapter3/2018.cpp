#include <iostream>

using namespace std;

int main(){

    int n;
    int start_index = 1;
    int end_index = 1;
    int count = 1;
    int sum = 1;

    cin >> n;

    while(end_index != n){

        if(sum == n){
            count ++;
            end_index ++;
            sum = sum + end_index;
        }

        else if(sum > n){
            sum = sum - start_index;
            start_index ++;
        }
        else{
            end_index++;
            sum  = sum + end_index;
        }

    }

    cout << count << "\n";

}