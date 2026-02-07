from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

attempt = 0

# ---------------- PASSWORD PAGE ----------------
PASSWORD_HTML = """
<!DOCTYPE html>
<html>
<body style="font-family:Arial;text-align:center;margin-top:80px;">

<h2>Enter password</h2>

{% if not success %}
<form method="post">
    <input type="text" name="password" required>
    <br><br>
    <button type="submit">Submit</button>
</form>
{% endif %}

{% if error %}
<p style="color:red;">Wrong password ❌</p>
{% endif %}

{% if hint %}
<p style="color:gray;">Hint: "aap dudu ki kya ho?" 😏</p>
{% endif %}

{% if success %}
<h3 style="color:green;">Access granted ✅</h3>
<br>
<form action="/colors">
    <button style="font-size:18px;padding:10px 20px;">Next →</
