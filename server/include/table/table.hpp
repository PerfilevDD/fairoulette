#pragma once

#include "bet/bet.hpp"
#include "ctime"
#include "list"
#include "vector"

namespace Fairoulette {
class Table {
   public:
    Table();

    void add_participant(int pid);
    void add_or_update_bet_for_participant(int pid, Bet bet);
    int calculate_result();

   private:
    std::time_t next_round = 0;
    std::list<int> participants;
    std::list<Bet> bets;
};
}  // namespace Fairoulette