# Demo static
* load static
```html
{% load static %}
<img src="{% static "example.png" %}">
```

* access static file
```html
<h2>Static HTML</h2>
<!-- You can access it by http://127.0.0.1:8000/static/static.html -->
```

* settings
```python
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

