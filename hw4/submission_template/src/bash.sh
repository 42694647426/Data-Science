grep -P '^\d+,\d{2}/\d{2}/2020'
grep -E '^([^,]*,){1}[^,]*2020'
bokeh serve --address 0.0.0.0 --port 8080 --enable-xsrf-cookies --auth-module=auth.py app.py