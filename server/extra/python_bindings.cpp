#include <pybind11/pybind11.h>

#include <bet/bet.hpp>
#include <randomizer.hpp>
#include <table/table.hpp>

using namespace Fairoulette;

PYBIND11_MODULE(fairoulette, m) {
    m.doc() = "kk";
    pybind11::class_<Randomizer>(m, "Randomizer")
        .def(pybind11::init<>())
        .def("get_random_number", &Randomizer::get_random_number);

    pybind11::class_<Table>(m, "Table")
        .def(pybind11::init<>())
        .def("calculate_result", &Table::calculate_result)
        .def("add_participant", &Table::add_participant)
        .def("add_or_update_bet_for_participant", &Table::add_or_update_bet_for_participant);

    pybind11::class_<Bet>(m, "Bet")
        .def(pybind11::init<int>())
        .def("calculate_result", &Bet::calculate_result)
        .def("add_number_bet", &Bet::add_number_bet)
        .def("add_red_bet", &Bet::add_red_bet)
        .def("add_black_bet", &Bet::add_black_bet)
        .def("add_even_bet", &Bet::add_even_bet)
        .def("add_odd_bet", &Bet::add_odd_bet)
        .def("add_col_bet", &Bet::add_col_bet)
        .def("add_dozen_bet", &Bet::add_dozen_bet)
        .def("get_number_bets", &Bet::get_number_bets)
        .def("get_pid", &Bet::get_pid);
}
