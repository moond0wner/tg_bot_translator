from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Начать перевод')]],
                           resize_keyboard=True,
                           input_field_placeholder='Нажмите кнопку...')


languages = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Русский', callback_data='ru')],
                                                  [InlineKeyboardButton(text='Английский', callback_data='en')],
                                                  [InlineKeyboardButton(text='Немецкий', callback_data='de')],
                                                  [InlineKeyboardButton(text='Французский', callback_data='fr')],
                                                  [InlineKeyboardButton(text='Испанский', callback_data='es')],
                                                  [InlineKeyboardButton(text='Китайский', callback_data='kt')]])
to_main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='На главную', callback_data='to_main')]])
