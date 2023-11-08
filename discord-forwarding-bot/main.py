import yaml
import time
import requests
from collections import deque
import logging


with open("config.yaml", "r") as stream:
    config = yaml.safe_load(stream)
messages_history = {}  # хранение истории сообщений для сравнения с новыми
for chat_id in config["chats_ids"]:
    messages_history[chat_id] = deque()
headers = {
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9,ko;q=0.8",
    "authorization": config["token"],
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "ru",
    "x-discord-timezone": "Europe/Moscow"
}


def find_new_messages():
    for chat_id in config["chats_ids"]:
        url = f"https://discord.com/api/v9/channels/{chat_id}/messages?limit=10"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            logging.warning(f"Ошибка запроса к Discord, статус код: {response.status_code}")
            continue
        messages = response.json()
        if len(messages_history[chat_id]) == 0:  # если только запущен бот и нет данных
            messages_history[chat_id] = deque(messages)
        else:
            iters = -1  # подсчёт количества новых элементов
            for i, mes in enumerate(messages):
                if messages_history[chat_id][0]["id"] == mes["id"]:
                    iters = i
                    if messages_history[chat_id][0]["content"] != mes["content"]:
                        iters += 1
                    break
            if iters == -1:  # в случае выхода за пределы лимита
                iters = len(messages)
            for i in range(iters-1, -1, -1):
                messages_history[chat_id].pop()
                messages_history[chat_id].appendleft(messages[i])
                print("Новые данные:", messages[i])
        time.sleep(config["step_time_sleep"])


if __name__ == "__main__":
    while True:
        find_new_messages()
        time.sleep(config["lap_time_sleep"])
