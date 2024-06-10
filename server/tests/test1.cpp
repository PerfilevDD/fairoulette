#include <iostream>
#include <randomizer.hpp>
#include "bet/bet.hpp"

int main(){
    Fairoulette::Randomizer rand;
    int x = rand.get_random_number();

    printf("%d\n", x);

    Fairoulette::Bet bet(2);
    bet.add_black_bet(1);
    bet.add_number_bet(1, 1);

}