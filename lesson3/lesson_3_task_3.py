from address import Address
from mailing import Mailing

letter = Mailing(
    Address("1117123", "Москва", "ул Коктебельская", "д. 43", "кв. 10",),
    Address("5117555", "Санкт Петербург", "ул Дрезденская", "д. 28", "кв. 38",),
    "$25.78",
    "1234567890",)

print(f"Письмо с трек номером {letter.track} отправлено по почте с адреса: {letter.from_address} Куда: {letter.to_address}. Стоимость отправления: {letter.cost}")
