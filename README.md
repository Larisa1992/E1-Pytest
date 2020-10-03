# E1-Pytest
Testing by Pytest


Клонировать проект командой git clone https://github.com/Larisa1992/E1-Pytest.git
Создать окружение python -m venv env
Активировать окружение env\Scripts\activate.bat
Установить пакеты pip install -r requirements.txt

Запустить тесты командой 
pytest -s -v  test_pytest.py

Отчет о покрытии приложения тестами можно вывести с помощью команды
pytest --cov=. test_pytest.py
