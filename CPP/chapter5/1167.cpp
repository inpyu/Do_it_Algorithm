#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

typedef pair<int, int> edge;
static vector<vector <edge>> A;
static vector<bool> visited;
static vector<int> m_distance;
void BFS(int node);

int main(){

    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);

    int n;
    cin >> n;
    A.resize(n+1);

    for(int i = 0 ; i < n ; i++){
        int s;
        cin >> s;
        while(true){
            int e,v;
            cin >> e;
            if(e == -1){
                break;
            }
            cin >> v;
            A[s].push_back(edge(e,v));
        }
    }

    m_distance = vector<int>(n+1, 0);
    visited = vector<bool>(n+1, false);

    BFS(1);
    int max = 1;

    for( int i = 2; i<=n; i++){
        if(m_distance[max] < m_distance[i]){
            max = i;
        }
    }

    fill(m_distance.begin(), m_distance.end(), 0);
    fill(visited.begin(), visited.end(), false);
    BFS(max);
    sort(m_distance.begin(), m_distance.end());

    cout << m_distance[n] << "\n";

}

void BFS(int index){
    queue<int> myqueue;
    myqueue.push(index);
    visited[index] = true;

    while(!myqueue.empty()){
        int now = myqueue.front();
        myqueue.pop();
        for(edge i : A[now]){
            if(!visited[i.first]){
                visited[i.first] = true;
                myqueue.push(i.first);
                m_distance[i.first] = m_distance[now] + i.second;
            }
        }
    }
}