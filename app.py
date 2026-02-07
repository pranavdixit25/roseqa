from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

attempt = 0

PASSWORD_HTML = '''
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
    <button style="font-size:18px;padding:10px 20px;">Next →</button>
</form>
{% endif %}

</body>
</html>
'''

COLOR_HTML = '''
<!DOCTYPE html>
<html>
<body style="font-family:Arial;text-align:center;margin-top:60px;">

<h2>Inme se <span style="color:red;">RED</span> block ko click karo</h2>

<form method="post">
    <button name="color" value="red" style="width:120px;height:120px;background:red;border:none;margin:10px;"></button>
    <button name="color" value="blue" style="width:120px;height:120px;background:blue;border:none;margin:10px;"></button>
    <button name="color" value="green" style="width:120px;height:120px;background:green;border:none;margin:10px;"></button>
    <button name="color" value="orange" style="width:120px;height:120px;background:orange;border:none;margin:10px;"></button>
</form>

{% if error %}
<p style="color:red;margin-top:20px;">😌 Nahi… dhyaan se dekho</p>
{% endif %}

{% if success %}
<h3 style="color:green;">Correct choice ❤️</h3>
<form action="/flower">
    <button style="font-size:18px;padding:10px 20px;">Next →</button>
</form>
{% endif %}

</body>
</html>
'''

FLOWER_HTML = '''
<!DOCTYPE html>
<html>
<body style="font-family:Arial;text-align:center;margin-top:80px;">

<h2>Which is the most common red flower?</h2>

<form method="post">
    <input type="text" name="flower" placeholder="Type your answer"
           style="font-size:16px;padding:8px;text-align:center;" required>
    <br><br>
    <button type="submit" style="font-size:16px;padding:8px 20px;">Submit</button>
</form>

{% if error %}
<p style="color:red;">❌ Wrong answer</p>
<p style="color:gray;">Hint: us flower ko hum everyday bolte hain 😏</p>
{% endif %}

{% if success %}
<h3 style="color:green;">CORRECT ANSWER!!!!!!! 🌹</h3>
<form action="/final">
    <button style="font-size:18px;padding:10px 20px;background:red;color:white;border:none;">
        Next →
    </button>
</form>
{% endif %}

</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def password():
    global attempt
    error = False
    hint = False
    success = False

    if request.method == "POST":
        pwd = request.form.get("password", "").lower()
        if pwd == "bubu":
            success = True
            attempt = 0
        else:
            error = True
            attempt += 1
            if attempt == 1:
                hint = True

    return render_template_string(PASSWORD_HTML, error=error, hint=hint, success=success)


@app.route("/colors", methods=["GET", "POST"])
def colors():
    error = False
    success = False

    if request.method == "POST":
        if request.form.get("color") == "red":
            success = True
        else:
            error = True

    return render_template_string(COLOR_HTML, error=error, success=success)


@app.route("/flower", methods=["GET", "POST"])
def flower():
    error = False
    success = False

    if request.method == "POST":
        if request.form.get("flower", "").lower().strip() == "rose":
            success = True
        else:
            error = True

    return render_template_string(FLOWER_HTML, error=error, success=success)


@app.route("/final")
def final():
    return '<h2 style="text-align:center;margin-top:80px;">🌹 Next surprise coming soon…</h2>'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

