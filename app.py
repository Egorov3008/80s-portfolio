from flask import Flask, render_template
from config import Config
import os

def create_app():
    """Создаёт и конфигурирует Flask приложение"""
    # Укажем правильную папку templates и static
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Загрузка конфигурации
    app.config.from_object(Config)
    
    # Регистрация шаблонов
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/projects')
    def projects():
        return render_template('projects.html')
    
    @app.route('/contacts')
    def contacts():
        return render_template('contacts.html')
    
    # Обработка ошибок
    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(e):
        return render_template('500.html'), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=5000)
