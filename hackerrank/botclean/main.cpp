#include<iostream>
#include<vector>
#include<stdlib.h>
#include<time.h>

using namespace std;

void next_move(int posr, int posc, vector <string> board) {
    //add logic here
    struct thing{
        int d;
        int x;
        int y;
    } closest;
    vector <string> moves;
    moves.push_back("LEFT");
    moves.push_back("RIGHT");
    moves.push_back("UP");
    moves.push_back("DOWN");
    moves.push_back("CLEAN");
    closest.d = 999;
    closest.x = 0;
    closest.y = 0;
    string out = "";
    int dist = 999;
    for(int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++){
            switch (board[i][j]) {
            case 'd':
                dist = abs(posr - i) + abs(posc - j);
                if (dist < closest.d) {
                    closest.y = i;
                    closest.x = j;
                    closest.d = dist;
/*
                    cout << "closest" << endl;
                    cout << i << endl;
                    cout << j << endl;
*/
                }
            default:
                break;
            }
        }
    }
/*
    cout << "col " << posc << endl;
    cout << "row " << posr << endl;
    cout << "c.x " << closest.x << endl;
    cout << "c.y " << closest.y << endl;
    cout << "col - x " << (posc - closest.x) << endl;
    cout << "row - y " << (posr - closest.y) << endl;
*/
    if (closest.d == 999){
        int test = (abs(rand() + time(NULL)) % 4);
        switch (test) {
            case 0:
                if (posc == 0) {out = "RIGHT";}
                else {out = "LEFT";}
                break;
            case 1:
                if (posc == 4) {out = "LEFT";}
                else {out = "RIGHT";}
                break;
            case 2:
                if (posr == 0) {out = "DOWN";}
                else {out = "UP";}
                break;
            case 3:
                if (posr == 4) {out = "UP";}
                else {out = "DOWN";}
                break;
        }
    }
    else if ((posc - closest.x) > 0){
        out = moves[0];
    }
    else if ((posc - closest.x) < 0){
        out = moves[1];
    }
    else if ((posr - closest.y) > 0){
        out = moves[2];
    }
    else if ((posr - closest.y) < 0){
        out = moves[3];
    }
    else if (((posc - closest.x) == 0)&&((posr - closest.y) == 0)){
        out = moves[4];
    }

    cout << out << endl;
}

int main(void) {
    int pos[2];
    vector <string> board;
    cin>>pos[0]>>pos[1];
    for(int i=0;i<5;i++) {
        string s;cin >> s;
        board.push_back(s);
    }
    next_move(pos[0], pos[1], board);
    return 0;
}
