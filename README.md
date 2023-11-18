## Библиотека Pydantic v1

### Подготовка файлов к работе
Для подготовки файлов к работе необходимо создать виртуальное окружение и установить зависимости:
```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

### Вложенная схема валидации данных

Для проверки вложенной схемы валидации данных необходимо запустить файл `nested_model.py`:
```bash
python nested_model.py
```
После запуска файла будет создан файл `nested_model.json`, содержащий валидированную модель из файла `nested_model.py`.
Также в консоль будет выведено описание модели, считанной из файла `nested_model_sample.json`:
Затем в консоль будет выведено сообщение об ошибке валидации:
```bash
2 validation errors for Member
person -> age
  ensure this value is greater than 18 (type=value_error.number.not_gt; limit_value=18)
joined
  field required (type=value_error.missing)
```

### Вложенная схема валидации переменных окружения

Для проверки вложенной схемы валидации данных необходимо запустить файл `model_from_env.py`:
```bash
python model_from_env.py
```
По умолчанию настройки окружения берутся из файла `.env.sample`, который содержит корректные данные.
Для получения ошибок валидации можно удалить одну из указанных в файле `.env.sample` переменных, или изменить ее значение:
```bash
SECRET_KEY=testing123
PROJECT__TITLE=Pydantic_nested_model
PROJECT__TAGS=test pydantic nested model
# заменить на
SECRET_KEY=testing123
PROJECT__TITLE=Pydantic_nested_model
PROJECT__TAGS=test pydantic nested 2
```
