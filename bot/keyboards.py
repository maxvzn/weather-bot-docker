from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_request_location_keyboard() -> ReplyKeyboardMarkup:
    """
    Returns a keyboard with a button to request the user's location.
    """
    buttons = [
        [KeyboardButton(text="📍 Отправить местоположение", request_location=True)]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons, resize_keyboard=True, one_time_keyboard=True
    )
    return keyboard
