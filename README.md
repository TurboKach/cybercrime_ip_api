# cybercrime_ip_api
1. `docker build --tag ubuntu:18.04`
2. `docker run --publish 8000:8080 --detach --name cc_ip_api ubuntu:18.04`
2. Запросы к API:

- `GET /api/ip` - получить список всех IP и подсетей, в заданном промежутке времени   
параметры:  
`time_from` - время от, `time_to` - время до, `list` - название списка, в который входит IP  

- `GET /api/list` - получить все списки, в которые входит заданный IP  
параметры:  
`ip` - IP адрес(обязательный), `time_to` - время, не позже которого IP был добавлен в список  

- `GET /api/management/update` - обновить списки IP-адресов (может потребоваться не менее 10 минут)
