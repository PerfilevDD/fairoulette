#include "bet/bet.hpp"

bool _is_even(int number) {
    return number % 2 == 0;
}

namespace Fairoulette {
    
    Bet::Bet(int user_id, int bet_id) : user_id(user_id), bet_id(bet_id) {}

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
        int balance = 0;

        // Add earning from number bet
        balance += number_bets[number] * 36;

        // End the calculation if the number is 0
        if (number == 0)
            return balance;

        // Add Odd/Even
        if (_is_even(number)){
            balance += outside_bets.even * 2;
        } else {
            balance += outside_bets.odd * 2;
        }

        // Add Red/Black
        if (
            (number <= 9 && !_is_even(number)) ||
            (number > 9 && number <= 18 && _is_even(number)) ||
            (number > 18 && number <= 36 && !_is_even(number))
        ) {
            balance += outside_bets.red * 2;
        } else {
            balance += outside_bets.black * 2;
        }

        // Add First, Second, Third Dozen
        if (number <= 12) {
            balance += outside_bets.dozen1 * 3;
        } else if (number <= 24) {
            balance += outside_bets.dozen2 * 3;
        } else if (number <= 36) {
            balance += outside_bets.dozen3 * 3;
        }

        // Add Columns
        if (number % 3 == 1){
            balance += outside_bets.col1 * 3;
        } else if ( number % 3 == 2) {
            balance += outside_bets.col2 * 3;
        } else if (number % 3 == 0) {
            balance += outside_bets.col3 * 3;
        }

        return balance;
    }
}  // namespace Fairoulette