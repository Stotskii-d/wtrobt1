from aiogram.types import ReplyKeyboardRemove
from wtrmarkbot.keyboards.reply.watermark import watermark_position, colors, fonts
from wtrmarkbot.keyboards.inline.menu import main_menu
from consts import MAX_FONT_SIZE

STARTING_MESSAGE = f"Привет! Добро пожаловать в @wtrmarkbot!" \
                   f"\n\n" \
                   f"Данный бот поможет без проблем наложить текст-вотермарку на картинку.\n" \
                   f"Также, тут есть следующие возможности:\n" \
                   f"📌 Возможность выбора шрифтов\n" \
                   f"📌 Возможность выбора цвета текста, его размера и прозрачности\n" \
                   f"📌 Возможность выбора позиции, где нужно разместить текст\n" \
                   f"📌 Для работы просто установи настройки и отправь картинку!.\n" \
                   f"\n\n" \
                   f"Сделал @kiriharu with <3. [Репозиторий бота](https://github.com/kiriharu/wtrmarkbot)."

routes_messages = {
    "starting": dict(
        text="💫 Можешь скидывать картинку.",
        reply_markup=ReplyKeyboardRemove(),
    ),
    "position": dict(
        text="↕️ Выберите позицию вотермарки: ",
        reply_markup=watermark_position()
    ),
    "color": dict(
        text="🏁 Выберите цвет текста",
        reply_markup=colors()
    ),
    "opacity": dict(
        text="➿ Установите прозрачность цифрой от 1 до 255 (255 непрозрачный, 1 - полностью прозрачный)",
        reply_markup=ReplyKeyboardRemove()
    ),
    "font": dict(
        text="✍️ Выберите шрифт",
        reply_markup=fonts()
    ),
    "fontsize": dict(
        text=f"✍️ Выберите размер шрифта (до {MAX_FONT_SIZE})",
        reply_markup=ReplyKeyboardRemove()
    ),
    "text": dict(
        text=f"💬 Напишите текст вотермарки",
        reply_markup=ReplyKeyboardRemove()
    ),
    "sendpic": dict(
        text="💫 Вот твоё фото с вотермаркой. Вроде неплохо, теперь никто не сворует твой контент. Хочешь ещё?",
        reply_markup=main_menu()
    )
}