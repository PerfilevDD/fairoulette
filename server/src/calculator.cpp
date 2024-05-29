#include <pybind11/pybind11.h>

double calculate(double x, double y){
    return x+y;
}

PYBIND11_MODULE(calculator, m){
    m.def("calculate", &calculate, "ss");
}