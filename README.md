# discord-forwarding-bot

Бот для сканирования чатов каналов. В дальнейшем можно пересылать сообщение в другие места.

### Пояснение к настройке конфига:<br>
`"chats_ids": ["836078633776709663"]` - id чата в канале. Брать из https://discord.com/channels/{id канала}/{id чата} <br>
`"token": "ABOBA"` - Токен авторизации аккаунта. Брать из headers при запросах к Дискорду в поле Authorization <br>
`"lap_time_sleep": 10` - Время задержки между циклами 1 прохода по массиву id чатов в секундах  <br>
`"step_time_sleep": 1`  # время задержки между запросами к разным чатам в секундах <br>
<br>

По всем вопросам в лс в контакты из профиля гитхаба
