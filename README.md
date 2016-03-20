An utility library to work with Mixpanel API and python 3

# Installation
```
pip install mixpanel3
```
# Example

```
mixpanel = Mixpanel(api_key=API_KEY, api_secret=API_SECRET)

date_format = "%Y-%m-%d"
date_now = datetime.datetime.utcnow()
date_last_week = date_now - datetime.timedelta(days=7)

query_params = {
    'event': EVENT_EXAMPLE,
    'from_date': str(date_now.strftime(date_format)),
    'to_date': str(date_now.strftime(date_format)),
    'format': 'json',
    'on': 'properties["' + PROPERTIES_FIELD_EXAMPLE + '"]',
}

response = mixpanel.get_request(methods='segmentation/numeric', params=query_params)
```

#REQUIRE LIBRARY

[Python Request](https://github.com/kennethreitz/requests)
