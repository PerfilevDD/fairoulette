#include "bet/bet.hpp"

namespace Fairoulette {
    
Bet::Bet(int pid) : pid(pid) {}

void Bet::add_black_bet(float worth) {
    this->outside_bets.black += worth;
}

void Bet::add_red_bet(float worth) {
    this->outside_bets.red += worth;
}

void Bet::add_even_bet(float worth) {
    this->outside_bets.even += worth;
}

void Bet::add_odd_bet(float worth) {
    this->outside_bets.odd += worth;
}

void Bet::add_number_bet(int number, float worth) {
    if (!(number >= 0 && number <= 36)) {
        // TODO: Throw error for not in bounds
    }
    number_bets[number] += worth;
}

void Bet::add_col_bet(int col, float worth) {
    switch (col) {
        case 1:
            outside_bets.col1 += worth;
            break;
        case 2:
            outside_bets.col2 += worth;
            break;
        case 3:
            outside_bets.col3 += worth;
            break;
        default:
            // Todo: Throw error
            break;
    }
}

void Bet::add_dozen_bet(int dozen, float worth) {
    switch (dozen) {
        case 1:
            outside_bets.dozen1 += worth;
            break;
        case 2:
            outside_bets.dozen2 += worth;
            break;
        case 3:
            outside_bets.dozen3 += worth;
            break;
        default:
            // Todo: Throw error
            break;
    }
}

int Bet::calculate_result(int number) {
    return 0;
}
}  // namespace Fairoulette