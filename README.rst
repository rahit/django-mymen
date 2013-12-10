=====
MyMen
=====

A simple django module for register, login and auth related activities
which nicely suited with default Auth module.


Quick start
-----------

1. Add "mymen" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'mymen',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^user/', include('mymen.urls')),

3. Run `python manage.py migrate` to create the mymen models.

4. Visit http://127.0.0.1:8000/user/ to see the magic.
