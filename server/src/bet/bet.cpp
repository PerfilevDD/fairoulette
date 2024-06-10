#include "bet/bet.hpp"

Bet::Bet(int pid): pid(pid) {}

void Bet::add_black_bet(int worth) {
    this->outside_bets.black += worth;
}

void Bet::add_red_bet(int worth) {
    this->outside_bets.red += worth;
}

void Bet::add_even_bet(int worth) {
    this->outside_bets.even += worth;
}

void Bet::add_odd_bet(int worth) {
    this->outside_bets.odd += worth;
}

void Bet::add_number_bet(int number, int worth) {
    if (!(number >= 0 && number <= 36)){
        // TODO: Throw error for not in bounds
    }
    number_bets[number] += worth;
}

void Bet::add_col_bet(int col, int worth) {
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

void Bet::add_dozen_bet(int dozen, int worth) {
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
