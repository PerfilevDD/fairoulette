#include "table/table.hpp"

#include "randomizer.hpp"
#include "algorithm"

void Table::calculate_result() {
    Fairoulette::Randomizer rand;
    int result = rand.get_random_number();
    for (Bet& bet: bets){
        int user_bet_result = bet.calculate_result(result);
    }
}

void Table::add_or_update_bet_for_participant(int pid, Bet bet) {
    for (auto it = bets.begin(); it != bets.end(); ++it) {
        if (it->get_pid() == pid)
            bets.erase(it);
    }
    bets.push_back(bet);
}

void Table::add_participant(int pid) {
    if (std::find(participants.begin(), participants.end(), pid) == participants.end())
        participants.push_back(pid);
}