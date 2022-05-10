#include<bits/stdc++.h>>

using namespace std;

queue<int>q;
int n;

int main() {
	cin >> n;
  for (int i=0; i<n; i++){
    string input;
    cin >> input;
      if(input == "push"){
          int data;
          cin >> data;
          q.push(data);
    } else if (input == "pop"){
      if (q.size() == 0) {
        cout << -1 << '\n';
      } else {
        cout << q.front() << '\n';
        q.pop();
      }
    } else if (input == "size"){
        cout << q.size() << '\n';
    } else if (input == "empty"){
        if (q.size() == 0){
          cout << 1 << '\n';
        } else {
          cout << 0 << '\n';
        }
    } else if (input == "front"){
        if (q.size() == 0){
          cout << -1 << '\n';
        } else {
          cout << q.front() << '\n';
        }
    } else if (input == "back"){
        if (q.size() == 0){
          cout << -1 << '\n';
        } else {
          cout << q.back() << '\n';
        }
    }
  }
	return 0;
}