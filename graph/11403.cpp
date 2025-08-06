#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> dist;

void floydwarshall(int n){

    for(int k = 0 ; k < n ; k++){
        for(int i = 0 ; i < n ; i++){
            for(int j = 0 ; j < n ; j ++){
                if(dist[i][k] == 0 || dist[k][j] == 0){
                    continue;
                }
                dist[i][j] = 1;
            }
        }
    }

}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n;
    cin >> n;

    dist.reserve(n);
    for(int i = 0 ; i < n ; i++){
        dist.emplace_back(vector<int>());
        for(int j = 0 ; j<n ; j++){
            int edge;
            cin >> edge;
            dist.back().emplace_back(edge);
        }
    }
    floydwarshall(n);

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j<n ; j++){
            cout << dist[i][j]<<' ';
        }
        cout << endl;
    }


    return 0;
}