#pragma once

#include "bet/bet.hpp"
#include "ctime"
#include "list"
#include "vector"
#include <pybind11/stl.h>

namespace Fairoulette {
class Table {
   public:
    Table(int table_id);

    void add_participant(int pid);
    void add_or_update_bet_by_bet_id(int pid, Bet bet);
    int calculate_result();

    Bet get_bet_by_bet_id(int bet_id);

    pybind11::list get_and_clear_bets();

    int get_table_id(){
        return table_id;
    }

   private:
    std::time_t next_round = 0;
    std::list<int> participants;
    std::list<Bet> bets;
    int table_id;
};
}  // namespace Fairoulette