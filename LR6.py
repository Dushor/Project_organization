from typing import Optional, Tuple
from typing import NamedTuple
from typing import TypedDict
from dataclasses import dataclass


def get_price(price: Optional[Tuple[float, float]] = None) -> Tuple[float, float]:
    return price


class prices(NamedTuple):
    one: float
    fifteen: float


def get_price() -> prices:
    return prices(15000, 75000)


prices = get_price()
print(f"Цена 1 контракта: {prices.one}")
print(f"Цена 5 контрактов: {prices.fifteen}")


class prices(TypedDict):
    fifteen: float
    one: float


c: prices = {"one": 15000, "fifteen": 75000}
print(c["one"])
print(c["fifteen"])


@dataclass
class prices:
    fifteen: float
    one: float


def get_price() -> prices:
    return prices(15000, 75000)


print(get_price().one)
print(get_price().fifteen)
