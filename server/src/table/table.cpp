#include "table/table.hpp"

#include "algorithm"
#include "randomizer.hpp"

namespace Fairoulette {

Table::Table(int table_id): table_id(table_id) {}

int Table::calculate_result() { // Hier wird berechnet, ob der Nutzer gewonnen hat, oder nicht 
    Fairoulette::Randomizer rand;
    int result = rand.get_random_number();
    for (Bet& bet : bets) {
        int user_bet_result = bet.calculate_result(result);
    }
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
}  // namespace Fairoulette