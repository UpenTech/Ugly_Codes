from unittest import result


def sum_square(n: int ) -> float:
    """Returns sum of natural series till n

    return type: float
    """
    return  ( n * (n+1) ) ** 2 / 4


def square_series_sum(n: int ) -> float:
    """Returns sum of squares of natural series till n

    return type: float
    """
    return  ( n * (n+1) * (2*n + 1) ) / 6


user_input = int(input("Series till: "))
result = sum_square(user_input) - square_series_sum(user_input)

print(f"Res: {int(result)}")