import requests


res = requests.get("http://127.0.0.1:8000/hi/Maaz%20Ahmed")


def test_status_code():
    assert res.status_code == 200
    # assert res.text == "Hi Maaz Ahmed"
    # assert res.headers["Content-Type"] == "text/html; charset=utf-8"
    # assert res.headers["Content-Length"] == "18"
    # assert res.headers["Server"] == "WSGIServer/0.2 CPython/3.8.0"
    # assert res.headers["Date"] == "Mon, 29 Jun 2020 13:56:06 GMT"
    # assert res.headers["Connection"] == "close"
    # assert res.headers["X-Powered-By"] == "Django/3.0.4"
    # assert res.headers["Content-Language"] == "en"
    # assert res.headers["Vary"] == "Accept-Language, Cookie"
    # assert res.headers["X-Frame-Options"] == "DENY"
    # assert res.headers["X-Content-Type-Options"] == "nosniff"
    # assert res.headers["X-XSS-Protection"] == "1; mode=block"