#include <iostream>
#include <string>

using namespace std;

int main(void){

    int a;
    string numbers;
    
    cin  >> a;  
    cin >> numbers;

    int sum = 0;
    for(int i=0; i< numbers.length();i++){
        sum += stoi(numbers[i]);
    }
    
    cout << sum << "\n";

    return 0;
}