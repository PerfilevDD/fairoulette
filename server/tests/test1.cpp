#include <iostream>
#include <randomizer.hpp>

int main(){
    Fairoulette::Randomizer rand;
    int x = rand.get_random_number();

    printf("%d\n", x);
}