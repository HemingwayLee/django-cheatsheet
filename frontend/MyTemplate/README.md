# Demo template in Django
* block content
```html
<html>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

* include 
```html
<html>
<body>
  {% include "included.html" %}
</body>
</html>
``` 

* context
```html
<h2>My name is {{name}}</h2>
```

* if else 
```html
{% if users %}
    <table border="1">
    {% for user in users %}
        <tr>
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td><a href="/context/{{ user.username }}">click me</a></td>
        </tr>
    {% endfor %}
    </table>
{% else %}
    <p>No data available.</p>
{% endif %}
```

* extends
```html
{% extends 'base.html' %}

{% block content %}
<h1>Hello Base</h1>
{% endblock %}
```

