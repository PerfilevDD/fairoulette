from fairoulette import Randomizer, Bet, Table  # type: ignore

table = Table(1)
result_random = table.calculate_result()
bet = Bet(1, 1)
bet.add_red_bet(1)

print(bet.calculate_result(29))
