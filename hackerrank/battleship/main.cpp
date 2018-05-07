#include <iostream>
#include <vector>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <algorithm>

using namespace std;

int main(void) {
    int N;
    vector < vector <char> > board;
    srand(time(NULL));

    int missile[2] = {0,0};

    cin >> N;
    for(int i = 0; i < N; i++) {
        vector <char> temp;
        for(int j = 0; j < N; j++){
            char s; cin >> s;
            temp.push_back(s);
        }
        board.push_back(temp);
    }

    // I had grand plans in mind, but not needed
    vector < pair <int, int> > row_hits;

    // find hit on the board
    // My original thought here was to process the group, but you can really only work one at a time per iteration
    for(size_t n = 0; n < board.size(); n++){
        int i = 0;
        // build an array of row hits
        do {
            i = find((board[n].begin() + i), board[n].end(), 'h') - board[n].begin();
            // find hits on the board
            if(i < board[n].size()){
                //cout << "\nFound hit at row " << n << " column " << i << "\n";
                pair <int, int> coord(n, i);
                row_hits.push_back(coord);
            }
            i++;
        } while (i < board[n].size());
    }
    bool guess = true;
    if ( !row_hits.empty() ){
        int i = 0;
        while ((i < row_hits.size()) && guess){
        // Look UP
        if ((row_hits[i].first != 0) && (board[(row_hits[i].first - 1)][row_hits[i].second]) == '-'){
            //cout << "\nMatch UP!\n";
            missile[0] = row_hits[i].first - 1;
            missile[1] = row_hits[i].second;
            guess = false;
        } // Else, look DOWN
        else if ((row_hits[i].first < (N - 1)) && ((board[(row_hits[i].first + 1)][row_hits[i].second]) == '-')){
            //cout << "\nMatch DOWN!\n";
            missile[0] = row_hits[i].first + 1;
            missile[1] = row_hits[i].second;
            guess = false;
        } // Else, look RIGHT
        else if ((row_hits[i].second < (N - 1)) && ((board[row_hits[i].first][(row_hits[i].second + 1)]) == '-')){
            //cout << "\nMatch RIGHT!\n";
            //cout << "\nboard: " << board[row_hits[0].first][(row_hits[0].second + 1)] << endl;
            missile[1] = row_hits[i].second + 1;
            missile[0] = row_hits[i].first;
            guess = false;
        } // Else, look LEFT
        else if ((row_hits[i].second != 0) && (board[row_hits[i].first][(row_hits[i].second - 1)]) == '-'){
            //cout << "\nMatch LEFT!\n";
            //cout << "\nboard: " << board[row_hits[0].first][(row_hits[0].second - 1)] << endl;
            missile[1] = row_hits[i].second - 1;
            missile[0] = row_hits[i].first;
            guess = false;
        } // Else, we guess
        else {
            guess = true;
        }
        i++;
    }
    }
    // should have been in a function, screw it, it's a short program
    if((row_hits.empty()) || (guess) ){
        do {
            //cout << "\n" << board[missile[0]][missile[1]] << "\n";
            missile[0] = (rand() % N);
            missile[1] = (rand() % N);
        } while (board[missile[0]][missile[1]] != '-');
    }
    //cout << "\n\nWe're bombing coordinates: " << missile[0] << " " << missile[1] << endl;
    cout << missile[0] << " " << missile[1] << endl;
    return 0;
}
