DiffbotAPI
===========

Diffbot API client script draft written in Python.


Howto
===========

Run following commands to clone DiffbotAPI locally, create a virtualenv and
run script then:
```sh
git clone https://github.com/webknjaz/diffbot-api.git
cd diffbot-api
virtualenv -p python2.7 env
source env/bin/activate
./diffbot_draft.py
./diffbot_draft.py "https://github.com/webknjaz/diffbot-api/"
```


Comments
===========

If no args are passed it runs only 3 test queries, otherwise script runs 3
hardcoded queries and `article` method for each argument passed.

If you import it in your project you may use it as follows:

```python
from diffbot_draft import Diffbot

API = Diffbot(token='yourtokenhere')

API.api_call(method='frontpage',
             url='http://president.gov.ua/')
```
