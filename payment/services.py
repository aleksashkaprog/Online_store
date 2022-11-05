import random


def get_exc_to_pay() -> str:
    """Функция возвращает случайную ошибку при неудачной оплате"""
    exceptions = (
        'Вашу карту зажевал банкомат',
        'Недостаточно средств',
        'Неверный CVC',
        'Это была необдуманная покупка, подумайте еще раз нужно ли оно вам',
        'Код ошибки 007, обратитесь в службу поддержки вашего банка',
    )

    return random.choices(exceptions)


def check_cart_number(card_number: int) -> bool:
    """Функция проверяет возможность оплаты с карты"""
    if len(str(card_number)) != 8 or not isinstance(card_number, int) or card_number % 2 \
            or str(card_number)[-1] == '0':
        return False

    return True
