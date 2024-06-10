#pragma once

#include "array"

struct OutsideBets {
    int odd = 0;
    int even = 0;
    int red = 0;
    int black = 0;
    int high = 0;
    int low = 0;
    int col1 = 0;
    int col2 = 0;
    int col3 = 0;
    int dozen1 = 0;
    int dozen2 = 0;
    int dozen3 = 0;
};

class Bet {
public:
    Bet();
    int calculate_result(int number);
    void add_number_bet(int number, int worth);
    void add_red_bet(int worth);
    void add_black_bet(int worth);
    void add_even_bet(int worth);
    void add_odd_bet(int worth);
    void add_col_bet(int col, int worth);
    void add_dozen_bet(int dozen, int worth);

    std::array<int, 37> get_number_bets() {
        return number_bets;
    }

private:
    std::array<int, 37> number_bets = {};
    struct OutsideBets outside_bets = {};

};