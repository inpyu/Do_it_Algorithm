#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int num;
    cin >> num;

    vector<int> numList(num,0);

    for(int i=0;i<num;i++){
        cin >> numList[i];
    }

    sort(numList.begin(), numList.end());

    int result = 0;

    for(int k = 0 ; k < num ; k++){
        long find = numList[k];
        int i = 0;
        int j = num - 1;

        while( i < j){
            if(numList[i] + numList[j] == find){
                if(i != k && j != k){
                    result++;
                    break;
                }else if(i == k){
                    i++;
                }else if (j == k){
                    j--;
                }
            }else if(numList[i] + numList[j] < find){
                i ++;
            }else{
                j--;
            }
            
        }

    }

    cout << result;

}