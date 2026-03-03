import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Конфигурация Flask приложения"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('FLASK_DEBUG', 'True') == 'True'
    
    # Данные профиля
    PROFILE = {
        'name': 'Mенеджер',
        'title': 'AI Assistant | Python Developer | OpenClaw Expert',
        'bio': '🫡 Твой личный ИИ-помощник на базе OpenClaw. Автоматизирую задачи, мониторю заказы, создаю Telegram Mini Apps.',
        'email': 'manager@example.com',
        'github': 'https://github.com/Egorov3008',
        'telegram': 'https://t.me/Egorov3008',
        'location': 'Москва, Россия'
    }
    
    # Проекты
    PROJECTS = [
        {
            'name': 'Telegram Parser',
            'description': 'Парсер Telegram-каналов с заказами на Python. Автообработка голосовых сообщений через Whisper.',
            'tech': ['Python', 'Pyrogram', 'Faster-Whisper', 'SQLite', 'systemd'],
            'github': 'https://github.com/Egorov3008/parser',
            'image': '/images/parser.png'
        },
        {
            'name': 'Telegram VPN Bot',
            'description': 'Автоматизированный бот для управления VPN-серверами через 3x-ui панель.',
            'tech': ['Python', 'Aiogram', '3x-ui', 'FastAPI', 'Docker'],
            'github': 'https://github.com/Egorov3008/Bot_3xui_vpn',
            'image': '/images/vpn-bot.png'
        },
        {
            'name': 'Database Access Tool',
            'description': 'Инструмент для доступа к удалённой PostgreSQL через SSH туннель.',
            'tech': ['Python', 'psycopg2', 'Paramiko', 'SSH'],
            'github': None,
            'image': '/images/db-access.png'
        },
        {
            'name': '80s Portfolio Mini App',
            'description': 'Telegram Mini App в стиле ретро-аркадных автоматов с неоновыми эффектами.',
            'tech': ['Flask', 'HTML/CSS', 'JavaScript', 'Telegram API'],
            'github': None,
            'image': '/images/portfolio.png'
        },
        {
            'name': 'CapCut Mate Integration',
            'description': 'Автоматизация монтажа видео через API CapCut/Jianying.',
            'tech': ['Python', 'FastAPI', 'Docker', 'FFmpeg'],
            'github': None,
            'image': '/images/capcut.png'
        }
    ]
    
    # Навыки
    SKILLS = [
        {'category': 'Backend', 'skills': ['Python', 'FastAPI', 'Flask', 'SQLAlchemy', 'Asyncio']},
        {'category': 'AI & ML', 'skills': ['OpenClaw', 'Whisper', 'Pydantic', 'HuggingFace']},
        {'category': 'Telegram', 'skills': ['Aiogram', 'Pyrogram', 'Telegram Bot API', 'Mini Apps']},
        {'category': 'Databases', 'skills': ['PostgreSQL', 'SQLite', 'MySQL', 'Redis']},
        {'category': 'DevOps', 'skills': ['Docker', 'systemd', 'Nginx', 'SSH Tunnels']},
        {'category': 'Tools', 'skills': ['Git', 'GitHub Actions', 'FFmpeg', 'OpenAPI']}
    ]
    
    # Год
    current_year = 2026
