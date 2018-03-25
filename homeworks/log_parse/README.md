# Парсер логов
Даны логи запросов сервера обслуживающего несколько доменных имен.  
Кроме запросов в логе могут встречаться строки не являющиеся записями об обращении к серверу.
Если строка является логом запроса к серверу, то она имеет следующую структуру:

```
[request_date] "request_type request protocol" response_code response_time  
```

- **request_date** - дата выполнения запроса    
- **request_type** - тип запроса (GET, POST, PUT ...)    
- **request** - <схема>:[//[<логин>:<пароль>@]<хост>[:<порт>]][/]<URL‐путь>[?<параметры>][#<якорь>] https://ru.wikipedia.org/wiki/URL    
- **protocol** - протокол и версия протокола, по которому осуществлялся запрос HTTP/HTTPS/FTP ...    
- **response_code** - статус код, которым ответил сервер на запрос    
- **response_time** - время выполнения запроса сервером    

#### Пример логов
```
[21/Mar/2018 21:32:09] "GET https://sys.mail.ru/static/css/reset.css HTTPS/1.1" 200 1090    
[21/Mar/2018 21:32:09] "GET https://corp.mail.ru/static/css/login.css HTTPS/1.1" 200 638    
help    
[21/Mar/2018 21:32:09] "GET https://sys.mail.ru/static/js/auth_error_message.js HTTPS/1.1" 200 1081    
[21/Mar/2018 21:53:10] "GET https://mail.ru/fitness/pay_list HTTP/1.1" 301 0    
ERROR [django.request:135] Internal Server Error: /fitness/pay_list/    
Traceback (most recent call last):    
  File "/root/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response    
    response = wrapped_callback(request, *callback_args, **callback_kwargs)    
  File "/root/fitness_pay/views.py", line 80, in show_pays    
    raise Exception    
Exception    
[21/Mar/2018 21:53:10] "GET https://corp.mail.ru/fitness/pay_list/ HTTP/1.1" 500 120426    
[21/Mar/2018 21:32:11] "GET https://mail.ru/static/js/jquery-go-top/go-top.png HTTP/1.1" 200 1845    
```
## Цель задачи  
Написать функцию, возвращающую список из количества использования топ 5 урлов, которые запрашивались у сервера.

### Функция должна принимать дополнительные параметры:
- **ignore_files (bool)** - игнорирует файлы (игнорируется весь лог, если в логе запрашивается фаил)
- **ignore_urls (list)** - игнорирует урлы из переданного списка    
- **start_at (datetime)** - начать парсить логи начиная с указанной даты    
- **stop_at (datetime)** - закончить парсить логи на указанной дате    
- **equest_type (string)** - тип запроса, которые надо парсить ( остальные игнорируются)    
- **ignore_www (bool)** - игнорировать www перед доменом (лог учитывается, но отбрасывается www из url лога)
- **slow_queries (bool)** - если True возвращает среднее значение в количестве миллисекунд (целую часть), потраченное на топ 5 самых медленных запросов к серверу (суммарное время ответов деленное на количество запросов)    
