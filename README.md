## AVB_Legal_test

### Для запуска тестов
1. Склонировать проект 'git clone https://github.com/krivoiplintus/AVB_Legal_test.git'
2. Запустить тесты 'pytest api_test_reg.py', 'pytest api_test.py'
3. Сгенерировать отчет 'allure generate allure-files -o allure-report'
4. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- requests
- allure
- json

### Струткура:
- ./test - тесты
- ./pages - описание API
- ./configyration - провайдер настроек
  - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
  - test_data.json - тестовые данные

### Cсылк:
Сайт проекта: https://verdictor.ru/
Swagger проекта: https://verdictor.ru/api/swagger/
