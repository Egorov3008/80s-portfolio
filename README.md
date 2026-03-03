# 🎮 80s Portfolio - Telegram Mini App

**Telegram Mini App** в стиле **ретро-аркадных автоматов 80-х** с неоновыми эффектами, CRT-анимациями и пиксель-артом!

---

## 🌟 **Особенности**

- ✨ **80s Retro Design** - Dendy/CRT aesthetic
- 🎨 **Neon Colors** - Pink, Blue, Yellow, Green
- 📺 **CRT Effects** - Scanlines, flickering, glow
- 🎭 **Glitch Animation** - Avatar effects
- 📱 **Responsive** - Mobile-friendly
- ⚡ **Fast Loading** - Optimized performance

---

## 🚀 **Быстрый старт**

### Установка

```bash
# Клонировать репозиторий
git clone https://github.com/Egorov3008/80s-portfolio.git
cd 80s-portfolio

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер
python app.py
```

### Запуск

```bash
# Local development
python app.py  # http://localhost:5000

# Production
python app.py --host 0.0.0.0 --port 5000
```

---

## 📁 **Структура проекта**

```
80s-portfolio/
├── app.py              # Flask application
├── config.py           # Configuration & profile data
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css   # 80s retro styles
└── templates/
    ├── base.html       # Base template
    ├── index.html      # Homepage
    ├── projects.html   # Projects page
    ├── contacts.html   # Contact page
    ├── 404.html        # Error page
    └── 500.html        # Error page
```

---

## 🎨 **Настройка**

Измените `config.py`:

```python
PROFILE = {
    'name': 'Ваше Имя',
    'title': 'Ваша Должность',
    'bio': 'Ваше описание',
    'email': 'your@email.com',
    'github': 'https://github.com/username',
    'telegram': 'https://t.me/username',
    'location': 'Город, Страна'
}

PROJECTS = [
    {
        'name': 'Название проекта',
        'description': 'Описание',
        'tech': ['Python', 'FastAPI'],
        'github': 'https://github.com/...'
    }
    # Добавьте свои проекты...
]

SKILLS = [
    {'category': 'Backend', 'skills': ['Python', 'FastAPI']},
    # Добавьте свои навыки...
]
```

---

## 📱 **Telegram Mini App**

Для интеграции с Telegram:

1. Создайте бота в [@BotFather](https://t.me/BotFather)
2. Выберите **Menu Button** → **Configure Menu Button**
3. Укажите URL: `https://github.com/Egorov3008/80s-portfolio`
4. Готово! Пользователи смогут открывать ваше портфолио прямо в Telegram!

---

## 🔧 **Технологии**

- **Backend**: Flask (Python 3.12)
- **Frontend**: HTML5, CSS3, JavaScript
- **Style**: 80s Retro, Neon, CRT
- **Font**: Press Start 2P (Google Fonts)

---

## 📄 **Лицензия**

MIT License - свободное использование с указанием авторства.

---

## 🤝 **Контакты**

- **GitHub**: [Egorov3008](https://github.com/Egorov3008)
- **Telegram**: [@Egorov3008](https://t.me/Egorov3008)
- **Email**: manager@example.com

---

## 🎯 **Планы развития**

- [ ] Добавить анимации на JS
- [ ] Интеграция с Telegram Web App API
- [ ] Темы (светлая/тёмная)
- [ ] Многоязычность
- [ ] Анимированные фоны
- [ ] Звуковые эффекты

---

**Made with 💜 in the 80s style** 🎮✨
