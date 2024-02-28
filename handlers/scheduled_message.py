from aiogram import Router, types, F
from bot import bot, scheduler, reminders

scheduled_message_router = Router()


@scheduled_message_router.message(F.text.lower().startswith("напомни"))
async def send_later(message: types.Message):
    text = message.text[7:]
    interval = 10

    reminder_id = f"{message.message_id}_{message.from_user.id}"
    reminders[reminder_id] = {"text": text}
    scheduler.add_job(
        send_my_message,
        'interval',
        seconds=interval,
        kwargs={'chat_id': message.from_user.id, 'reminder_id': reminder_id},
        id=reminder_id
    )
    await message.answer("Будет сделано!")


async def send_my_message(reminder_id, chat_id: int):
    if reminder_id not in reminders:
        scheduler.remove_job(job_id=reminder_id)
        return

    reminder = reminders.pop(reminder_id)
    await bot.send_message(
        chat_id=chat_id,
        text=f"Напоминание {reminder['text']}"
    )
