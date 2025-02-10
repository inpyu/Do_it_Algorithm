#include <iostream>

using namespace std;
int answerCnt[4];
int myArr[4];
int resultCnt = 0;

void add(char c);
void remove(char c);

int main(){


    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int S,P;
    string str;
    int result = 0;

    cin >> S >> P;
    cin >> str;

    for(int i= 0 ; i < 4 ; i++){
        cin >> answerCnt[i];
        if(answerCnt[i] == 0){
            resultCnt ++;
        }
    }

    for(int i = 0 ; i < P; i++){
        add(str[i]);
    }
    if(resultCnt == 4){
        result ++;
    }

    for(int i = P; i < S ; i++){
        int j = i - P;
        add(str[i]);
        remove(str[j]);

        if(resultCnt == 4){
            result++;
        }
    }

    cout << result;

}

void add(char c){
    switch(c){
        case 'A':
            myArr[0]++;
            if(myArr[0] == answerCnt[0]){
                resultCnt++;
            }
            break;
        case 'C':
            myArr[1]++;
            if(myArr[1] == answerCnt[1]){
                resultCnt++;
            }
        break;
        case 'G':
            myArr[2]++;
            if(myArr[2] == answerCnt[2]){
                resultCnt++;
            }
            break;
        case 'T':
            myArr[3]++;
            if(myArr[3] == answerCnt[3]){
                resultCnt++;
            }
            break;
    }
}

void remove(char c){
    switch(c){
        case 'A':
            if(myArr[0] == answerCnt[0]){
                resultCnt--;
            }
            myArr[0]--;
            break;
        case 'C':
            if(myArr[1] == answerCnt[1]){
                resultCnt--;
            }
            myArr[1]--;
        break;
        case 'G':
            if(myArr[2] == answerCnt[2]){
                resultCnt--;
            }
            myArr[2]--;
            break;
        case 'T':
            if(myArr[3] == answerCnt[3]){
                resultCnt--;
            }
            myArr[3]--;
            break;
    }
}