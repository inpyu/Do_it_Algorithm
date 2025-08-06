#include <iostream>
#include <queue>

using namespace std;

int n,m;
int grid[1002][1002];
int dist[1002][1002];
int visited[1002][1002];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

int main(void){

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;

    queue<pair<int,int>> q;

    int startX = -1, startY = -1;
    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            cin >> grid[i][j];
            if(grid[i][j]==2){
                startX = i;
                startY = j;
            }
        }
    }

    q.push({startX, startY});
    visited[startX][startY] = true;
    dist[startX][startY] = 0;

    while(!q.empty()){
        pair<int,int> current = q.front();
        int x = current.first;
        int y = current.second;
        q.pop();

        for(int dir = 0 ; dir < 4 ; dir++){
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if(nx >= 0 && ny >= 0 && nx < n && ny < m){
                if(!visited[nx][ny] && grid[nx][ny] == 1){
                    visited[nx][ny] = true;
                    dist[nx][ny] = dist[x][y] +1;
                    q.push({nx,ny});
                }
            }
        }

    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 0) {
                cout << 0 << " ";
            } else if (visited[i][j]) {
                cout << dist[i][j] << " ";
            } else {
                cout << -1 << " ";
            }
        }
    cout << '\n';
    }
    return 0;
}