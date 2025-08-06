#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    long long a, b;
    cin >> a >> b;

    const long long MAX = 10000000; // 소수 찾기 범위 (10^7)
    vector<bool> isPrime(MAX + 1, true);
    vector<long long> primes; // 소수 저장

    // 에라토스테네스의 체를 사용하여 소수 찾기
    isPrime[0] = isPrime[1] = false;
    for (long long i = 2; i <= MAX; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (long long j = i * i; j <= MAX; j += i) {
                isPrime[j] = false;
            }
        }
    }

    int count = 0;
    
    // 거의 소수 판별
    for (long long prime : primes) {
        long long temp = prime * prime; // 제곱수부터 시작

        while (temp <= b) {
            if (temp >= a) {
                count++;
            }
            if (temp > b / prime) break; // 오버플로우 방지
            temp *= prime;
        }
    }

    cout << count << "\n";
    return 0;
}
