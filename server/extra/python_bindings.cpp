#include <pybind11/pybind11.h>
#include <randomizer.hpp>

using namespace Fairoulette;

PYBIND11_MODULE(fairoulette, m) {
    m.doc() = "kk";
    pybind11::class_<Randomizer>(m, "Randomizer")
        .def(pybind11::init<>())
        .def("get_random_number", &Randomizer::get_random_number);
}
