# Как запустить на MacOS:
1) Вначале нужно установить на mac python и git, это удобно сделать через специальный пакетный менеджер (homebrew)
https://brew.sh/
На главной странице есть команда, которую нужно вписать в терминал, чтобы поставить brew

2) После того, как brew установлен можно ставить python и git. Там же в терминале написать
```
brew install python
brew install git
```

3) Перезапустить терминал. Убедиться, что все установилось, выполнив
```
python3 --version
pip3 --version
git --version
```

4) Склонировать репозиторий моего проекта в любую папку. Вначале перейти туда и выполнить
```
git clone git@github.com:marknik139/subscription_checker.git
```

5) Создать переменное окружение в папке, которую склонировал из гита, активировать его и установить пакеты
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

6) Сделать файл с секретными переменными в той же папке, назвать файл .env и поменять содержимое на свое
```
TOKEN=7192301234:AAGmQnLQpfD3-bB29zjy6gknFVFuWnvyEH0
CHANNEL_USERNAME=@goodsrest
LINK=https://path1/path2
```

7) Запустить скрипт бота
```
python3 main.py 
```
