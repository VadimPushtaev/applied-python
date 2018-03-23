Даны логи запросов сервера обслуживающего несколько доменных имен.<br />
Кроме запросов в логе могут встречаться строки не являющиеся записями об обращении к серверу.<br />
если строка является логом запроса к серверу, то она имеет слелующую структуру:<br />
[request_date] "request_type request protocol" response_code response_time<br />

request_date - дата выполнения запроса<br />
request_type - тип запроса (GET, POST, PUT ...)<br />
request - <схема>:[//[<логин>:<пароль>@]<хост>[:<порт>]][/]<URL‐путь>[?<параметры>][#<якорь>] https://ru.wikipedia.org/wiki/URL<br />
protocol - протокол и версия протокола, по которому осуществлялся запрос HTTP/HTTPS/FTP ...<br />
response_code - статус код, которым ответил сервер на запрос<br />
response_time - время выполнения запроса сервером<br />

пример логов:
  
[21/Mar/2018 21:32:09] "GET https://sys.mail.ru/static/css/reset.css HTTPS/1.1" 200 1090<br />
[21/Mar/2018 21:32:09] "GET https://corp.mail.ru/static/css/login.css HTTPS/1.1" 200 638<br />
help<br />
[21/Mar/2018 21:32:09] "GET https://sys.mail.ru/static/js/auth_error_message.js HTTPS/1.1" 200 1081<br />
[21/Mar/2018 21:53:10] "GET https://mail.ru/fitness/pay_list HTTP/1.1" 301 0<br />
ERROR [django.request:135] Internal Server Error: /fitness/pay_list/<br />
Traceback (most recent call last):<br />
  File "/root/lib/python2.7/site-packages/django/core/handlers/base.py", line 185, in _get_response<br />
    response = wrapped_callback(request, *callback_args, **callback_kwargs)<br />
  File "/root/fitness_pay/views.py", line 80, in show_pays<br />
    raise Exception<br />
Exception<br />
[21/Mar/2018 21:53:10] "GET https://corp.mail.ru/fitness/pay_list/ HTTP/1.1" 500 120426<br />
[21/Mar/2018 21:32:11] "GET https://mail.ru/static/js/jquery-go-top/go-top.png HTTP/1.1" 200 1845<br />

цель задачи:<br />
Написать функцию, возвращающую списк из количества использования топ 5 урлов, которые запрашивают у сервера<br />
функция должна принимать дополнительные параметры:<br />
ignore_files (bool) - игнорирует фаилы<br />
ignore_urls (list)- игнорирует урлы из переданного списка<br />
start_at (datetime) - начать парсить логи начиная с указанной даты<br />
stop_at (datetime) - закончить парсить логи на указанной дате<br />
request_type (string) - тип запроса, которые надо парсить ( остальные игнорируются)<br />
ignore_www (bool) - игнорировать www перед доменом<br />
slow_queries (bool) - если True возвращает количество милисекунд (целую часть), потраченное на топ 5 самых медленных запросов к серверу<br />

