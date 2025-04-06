# 🎧 Music Link Converter Bot

Telegram-бот, который принимает ссылку на трек с одного стриминга и возвращает ссылки на другие платформы. Поддерживает:

- Spotify
- Apple Music
- YouTube
- Deezer
- Яндекс.Музыку

## 🚀 Как работает

1. Кидаешь боту ссылку на трек с любого стриминга.
2. Бот через Odesli API находит ссылки на доступные стриминги.
3. Возвращает тебе удобный список ссылок.

Пример:

Ты: https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
Бот:
	•	Apple Music: https://music.apple.com/…
	•	YouTube: https://youtube.com/…
	•	Deezer: https://deezer.com/…
	•	…

---

## ⚙️ Установка

```bash
git clone https://github.com/shdwofm/music-bot.git
cd music-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt