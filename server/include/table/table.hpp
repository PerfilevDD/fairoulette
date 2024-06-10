#pragma once

#include "ctime"
#include "vector"

class Table {
public:
    void add_participant(int pid);
    void add_or_update_bet_for_participant(int pid);

private:
    std::time_t next_round = 0;
    std::vector<int> participants;

};