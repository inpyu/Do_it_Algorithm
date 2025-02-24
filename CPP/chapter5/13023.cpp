#include <iostream>
#include <vector>

using namespace std;

static vector<vector<int>> A;
static vector<bool> visited;
static bool arrived;

void DFS(int n, int depth);

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int node, edge;
    cin >> node >> edge;

    A.resize(node);
    visited = vector<bool>(node, false);

    for(int i = 0 ; i < edge ; i++){
        int a, b;
        cin >> a >> b;
        A[a].push_back(b);
        A[b].push_back(a);
    }
    
    int count = 0;

    for(int i =0 ; i < node; i++){
        DFS(i, 1);
        if(arrived){
            break;
        }
    }

    if(arrived){
        cout << 1 << "\n";
    }else{
        cout << 0 << "\n";
    }

    

}

void DFS(int v, int depth){
    if (depth == 5 || arrived){
        arrived = true;
        return;
    }

    visited[v] = true;
    for(int i: A[v]){
        if(visited[i] == false){
            DFS(i, depth +1);
        }
    }
    visited[v] = false;
}