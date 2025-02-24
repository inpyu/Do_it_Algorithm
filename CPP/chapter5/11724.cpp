#include <iostream>
#include <vector>

using namespace std;

static vector<vector<int>> A;
static vector<bool> visited;
void DFS(int v);

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int node, edge;
    cin >> node >> edge;

    A.resize(node+1);
    visited = vector<bool>(node+1, false);

    for(int i=0; i < edge ; i++){
        int n,m;
        cin >> n >> m ;
        A[n].push_back(m);
        A[m].push_back(n);
    }

    int count = 0;

    for(int i =1;i<node+1; i++){
        if(!visited[i]){
            count ++;
            DFS(i);
        }
    }

    cout << count << "\n";
}

void DFS(int v){
    if(visited[v]){
        return;
    }

    visited[v] = true;
    for(int i: A[v]){
        if(visited[i] == false){
            DFS(i);
        }
    }
}