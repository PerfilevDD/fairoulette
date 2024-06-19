#include "table/table.hpp"

#include "algorithm"
#include "randomizer.hpp"

namespace Fairoulette {

Table::Table(int table_id): table_id(table_id) {}

int Table::calculate_result() { // Hier wird berechnet, ob der Nutzer gewonnen hat, oder nicht 
    Fairoulette::Randomizer rand;
    int result = rand.get_random_number();
    return result;
}

void Table::add_or_update_bet_for_participant(int pid, Bet bet) {   // Die Wette wird aktualisiert "also hinzugefügt"
    for (auto it = bets.begin(); it != bets.end(); ++it) {
        if (it->get_user_id() == pid) {
            bets.erase(it);
            break;
        }
    }
    bets.push_back(bet);
}

void Table::add_participant(int pid) {      // Neuer Nutzer kommt am Tisch
    if (std::find(participants.begin(), participants.end(), pid) == participants.end())
        participants.push_back(pid);
}

    pybind11::list Table::get_and_clear_bets() {
        Bet new_bet = Bet(1, 1);
        new_bet.add_number_bet(1, 10);
        bets.push_back(new_bet);
        pybind11::list tmp_list = pybind11::cast(bets);
        bets.clear();
        return tmp_list;
    }
}