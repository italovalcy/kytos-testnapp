Overview
========
Kytos Napp to test basic kytos


Requirements
============
 - nothing

Getting started
===============

- To install this Napp:

```
git clone https://github.com/italovalcy/kytos-testnapp/
cd kytos-testnapp
python3 setup.py develop
```

After installing the Napp, you should see it on Kytos Napps list:

```
kytos napps list
...
 [ie]  | italovalcy/testnapp:1.0       | Kytos Napp to test kytos
...
```

Now you have to reload Kytos (due to an bug https://github.com/kytos-ng/kytos/issues/469)

After that, you should be able to see the Napp running and its APIs:

```
curl http://127.0.0.1:8181/api/italovalcy/testnapp/v1/
{"result": "Napp is running!"}
```

You can also test the POST API endpoint:

```
curl -X POST -i http://127.0.0.1:8181/api/italovalcy/testnapp/v1/ -d '{"somedata": "xpto"}'
HTTP/1.1 201 Created
date: Fri, 27 Sep 2024 19:08:14 GMT
server: uvicorn
content-length: 22
content-type: application/json

"Operation successful"
```

You will also notice that the Napp listens to some Kytos Events, so you can check on the system logs for messages of the Napp:

```
grep "italovalcy/testnapp.*handle" /var/log/syslog
2024-09-27T19:05:04.646444+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.new content={'switch': Switch('00:00:00:00:00:00:00:01')}
2024-09-27T19:05:04.647265+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.new content={'switch': Switch('00:00:00:00:00:00:00:02')}
2024-09-27T19:05:04.647579+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.new content={'switch': Switch('00:00:00:00:00:00:00:03')}
2024-09-27T19:05:05.949287+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.reconnected content={'switch': Switch('00:00:00:00:00:00:00:01')}
2024-09-27T19:05:05.950908+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.reconnected content={'switch': Switch('00:00:00:00:00:00:00:03')}
2024-09-27T19:05:05.952330+00:00 b5a5796b6fe3 kytos.napps.italovalcy/testnapp:INFO main:46:  handle_new_switch event=kytos/core.switch.reconnected content={'switch': Switch('00:00:00:00:00:00:00:02')}
```
