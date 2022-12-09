#include <string>
#include <iostream>
#include <vector>

#include "movedef.h"

using namespace std;

char tttresult(string tttboard)
{
    // bad shape
    if(tttboard.size() != 9)
        return 'e';
    
    // count plays
    char count_x = 0;
    char count_o = 0;
    char count_p = 0;
    for(char i = 0; i < 9; ++i)
    {
        char p = tttboard[i];
        if(p == 'x')
            ++count_x;
        if(p == 'o')
            ++count_o;
        if(p == '#')
            ++count_p;
    }

    // bad chars
    if(count_x + count_o + count_p != 9)
        return 'e';

    // unbalanced numbers
    if(count_x - count_o > 1 || count_x - count_o < 0)
    {
        //cout << "unbalanced numbers\n";
        return 'i';
    }

    char wc[8] = {0}; // 3 columns, 3 rows, and 2 diagonal win conditions
    for(char i = 0; i < 9; ++i)
    {
        char score = 0;
        if(tttboard[i] == 'x')
            score = 1;
        if(tttboard[i] == 'o')
            score = -1;

        // column
        wc[i%3] += score;

        // row
        wc[3+i/3] += score;

        // both diagonals
        if(i == 4)
        {
            wc[6] += score;
            wc[7] += score;
        }
        else
        {
            // red diagonal
            if(i % 4 == 0)
                wc[6] += score;

            // black diagonal
            if(i % 4 == 2)
                wc[7] += score;
        }
    }

    // parse win conditions array
    char num_x_win = 0;
    char num_o_win = 0;
    for(char i = 0; i < 8; ++i)
    {
        if(wc[i] == 3)
            ++num_x_win;
        if(wc[i] == -3)
            ++num_o_win;
    }

    // too many winners
    if(num_x_win * num_o_win != 0)
    {
        //cout << "too many winners\n";
        return 'i';
    }

    // x wins
    if(num_x_win > 0)
        return 'x';

    // o wins
    if(num_o_win > 0)
        return 'o';

    // all spaces are filled
    if(count_p == 0)
        return 't';

    // all else game continues
    return 'c';
}

char tttresult(vector<Move> board)
{
    string tttboard = "#########";
    for(char i = 0; i < board.size(); ++i)
        tttboard[3*board[i].r + board[i].c] = board[i].player;
    return tttresult(tttboard);
}

vector<string> get_a_board(vector<string> boards, char idx)
{
    vector<string> new_boards;

    if(idx == 8)
    {
        boards[0][idx] = 'x';
        boards[1][idx] = 'o';
        boards[2][idx] = '#';

        new_boards.push_back(boards[0]);
        new_boards.push_back(boards[1]);
        new_boards.push_back(boards[2]);
    }
    else
    {
        int b3 = (int) (boards.size() / 3);

        // fill first third with x
        vector<string> board0;
        for(int i = 0; i < b3; ++i)
        {
            boards[i][idx] = 'x';
            board0.push_back(boards[i]);
        }

        // fill second third with o
        vector<string> board1;
        for(int i = 0; i < b3; ++i)
        {
            boards[b3+i][idx] = 'o';
            board1.push_back(boards[b3+i]);
        }

        // fill last third with #
        vector<string> board2;
        for(int i = 0; i < b3; ++i)
        {
            boards[2*b3+i][idx] = '#';
            board2.push_back(boards[2*b3+i]);
        }

        // recursion
        board0 = get_a_board(board0, idx+1);
        board1 = get_a_board(board1, idx+1);
        board2 = get_a_board(board2, idx+1);

        // combine results
        for(int i = 0; i < b3; ++i)
            new_boards.push_back(board0[i]);
        for(int i = 0; i < b3; ++i)
            new_boards.push_back(board1[i]);
        for(int i = 0; i < b3; ++i)
            new_boards.push_back(board2[i]);
    }

    return new_boards;
}

vector<string> get_all_boards()
{
    int num_boards = 3*3*3*3*3*3*3*3*3;
    vector<string> boards;
    for(int i = 0; i < num_boards; ++i)
        boards.push_back("#########");
    
    boards = get_a_board(boards, 0);

    // for(int i = 0; i < num_boards; ++i)
    //     cout << boards[i] << "\n";

    return boards;
}

int main()
{
    cout << tttresult("xox#x#xox") << '\n';
    cout << tttresult("xoxoxoxox") << '\n';
    cout << tttresult("###xxxoo#") << '\n';
    cout << tttresult("xxxoooHI!") << '\n';

    vector<Move> moves;
    bool error;
    char result;
    Move m; // make a move 
    m.r = 0; // fill the data
    m.c = 1;
    m.player = 'x';
    moves.push_back(m); // put the move on the vector representing the board.
    cout << tttresult(moves) << '\n';  // returns 'c'

    get_all_boards();

    return 0;
}