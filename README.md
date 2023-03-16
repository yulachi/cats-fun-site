<div align="center">

# Cats Fun Site

<br>[![code-quality](https://github.com/yulachi/cats-fun-site/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/yulachi/cats-fun-site/actions/workflows/code-quality-main.yaml)
[![tests](https://github.com/yulachi/cats-fun-site/actions/workflows/test.yml/badge.svg)](https://github.com/yulachi/cats-fun-site/actions/workflows/test.yml)<br>

</div>

# Запуск сервера с сайтом

```console
# активация venv с django
poetry shell

# только при первом запуске
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate

# запуск сервера
python manage.py runserver
```

## Установка зависимостей

```console
# менеджер зависимостей poetry (также необходим python 3.10)
pip install poetry

# установка зависимостей (кроме development dependencies)
poetry install --without dev
```

### Установка python 3.10 (опционально)

```console
./scripts/ubuntu_build_python.sh
export PATH=/opt/python/3.10.0/bin/:$PATH
```
