#include <iostream>
#include <vector>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <algorithm>

using namespace std;

void init(const int N){
    vector < vector <char> > temp_board;
    char s = '-';
    for(int i = 0; i < N; i++){
        vector <char> temp;
        for(int j = 0; j < N; j++){
            temp.push_back(s);
        }
        temp_board.push_back(temp);
    }

    // true vertical, false horizontal
    bool vertical = (rand() % 2);
    int row, col;
    // start with carrier, size 5
    const int num_boats = 7;
    int boats[num_boats] = {5,4,3,2,2,1,1};
    // pair of x/y, bool vert or horiz
    struct boat
    {
        pair <int, int> start_pos;
        int boat_size;
        bool vert;
    };

    boat boat_pos[num_boats];

    for (int i = 0; i < num_boats; i++){
        bool okay = true;
        // We'll keep guessing while there isn't another boat in the way
        //cout << "Boat: " << boats[i] << endl;
        while(okay){
            // randomly guess on a position
            if(vertical){
                col = (rand() % N);
                row = (rand() % (N - boats[i]));
                //cout << "Vertical col: " << col << " row: " << row << endl;
            } else {
                col = (rand() % (N - boats[i]));
                row = (rand() % N);
                //cout << "Horizontal col: " << col << " row: " << row << endl;
            }
            // go through and update the temp_board with our boats
            for(int j = 0; j < boats[i]; j++){
                if(vertical){
                    if (temp_board[(row + j)][col] != '-'){
                        okay = false;
                        continue;
                    }
                    //cout << "Vertical: Row: " << row << " Col: " << col << " TB[row + j][col]: " << temp_board[row + j][col] << endl;
                    temp_board[(row + j)][col] = 'b';
                } else if (!vertical) {
                    if (temp_board[row][(col + j)] != '-'){
                        okay = false;
                        continue;
                    }
                    //cout << "Horizontal: Row: " << row << " Col: " << col << " TB[row][col + j]: " << temp_board[row][col + j] << endl;
                    temp_board[row][(col + j)] = 'b';
                } // end if !vertical
            } // end for j
            // since for loop successful, okay to false
            okay = false;
        } // end while

        boat_pos[i].start_pos = make_pair(col, row);
        boat_pos[i].vert = vertical;
        boat_pos[i].boat_size = boats[i];

        vertical = (rand() % 2);
    } // end for i

    // print out ship positions in game format
    for (int i = num_boats - 1; i >= 0; i--){
        //cout << boat_pos[i].boat_size << " ";
        if(boat_pos[i].boat_size == 1) {
            cout << boat_pos[i].start_pos.first << " " << boat_pos[i].start_pos.second << endl;
        } else if (boat_pos[i].vert){
            cout << boat_pos[i].start_pos.first << " " << boat_pos[i].start_pos.second << ":"
                    << boat_pos[i].start_pos.first << " " << (boat_pos[i].start_pos.second + boat_pos[i].boat_size) << endl;
        } else {
            cout << boat_pos[i].start_pos.first << " " << boat_pos[i].start_pos.second << ":"
                    << (boat_pos[i].start_pos.first + boat_pos[i].boat_size)<< " " << boat_pos[i].start_pos.second << endl;
        }
    }

    // print the board with boats
    /*
    for (int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            cout << temp_board[i][j];
        }
        cout << endl;
    } */
    return;
}

int main(void) {
    string input;
    int N = 10;
    vector < vector <char> > board;
    srand(time(NULL));

    int missile[2] = {0,0};

    cin >> input;
    if(input == "INIT"){
        init(N);
        return(0);
    }
    // closes at end of main()
    else {

    N = atoi(input.c_str());

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

    // find hit on the
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
}
