#pragma once

#include "array"

namespace Fairoulette {
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
    Bet(int pid);
    int calculate_result(int number);
    void add_number_bet(int number, float worth);
    void add_red_bet(float worth);
    void add_black_bet(float worth);
    void add_even_bet(float worth);
    void add_odd_bet(float worth);
    void add_col_bet(int col, float worth);
    void add_dozen_bet(int dozen, float worth);

    std::array<int, 37> get_number_bets() {
        return number_bets;
    }

    int get_pid() {
        return pid;
    }

   private:
    std::array<int, 37> number_bets = {};
    struct OutsideBets outside_bets = {};
    int pid;
};
}  // namespace Fairoulette