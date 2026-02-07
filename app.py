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
    <button style="font-size:18px;padding:10px 20px;">Next →</button>
</form>
{% endif %}

</body>
</html>
"""

# ---------------- COLOR PAGE ----------------
COLOR_HTML = """
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
<p style="color:red;">😌 Dhyaan se dekho</p>
{% endif %}

{% if success %}
<h3 style="color:green;">Correct ❤️</h3>
<form action="/flower">
    <button style="font-size:18px;padding:10px 20px;">Next →</button>
</form>
{% endif %}

</body>
</html>
"""

# ---------------- FLOWER IMAGE QUESTION ----------------
FLOWER_HTML = """
<!DOCTYPE html>
<html>
<body style="font-family:Arial;text-align:center;margin-top:40px;">

<h2>Ye kaunsa flower hai? 🌸</h2>

<img src="https://upload.wikimedia.org/wikipedia/commons/b/bf/Rose_red_blossom.jpg"
     width="250" style="border-radius:10px;"><br><br>

<form method="post">
    <input type="text" name="answer" placeholder="Answer here" required>
    <br><br>
    <button type="submit">Submit</button>
</form>

{% if error %}
<p style="color:red;">❌ Galat jawab, phir se try karo</p>
{% endif %}

{% if success %}
<h3 style="color:green;">🌹 Correct! Ye Rose hai</h3>
<form action="/final">
    <button style="font-size:18px;padding:10px 20px;">Next →</button>
</form>
{% endif %}

</body>
</html>
"""

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def password():
    global attempt
    error = False
    hint = False
    success = False

    if request.method == "POST":
        pwd = request.form.get("password")

        if pwd.lower() == "bubu":
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
        choice = request.form.get("color")
        if choice == "red":
            success = True
        else:
            error = True

    return render_template_string(COLOR_HTML, error=error, success=success)


@app.route("/flower", methods=["GET", "POST"])
def flower():
    error = False
    success = False

    if request.method == "POST":
        ans = request.form.get("answer")
        if ans.lower() == "rose":
            success = True
        else:
            error = True

    return render_template_string(FLOWER_HTML, error=error, success=success)


@app.route("/final")
def final():
    return """
    <h2 style="text-align:center;margin-top:80px;">
        🌹 Final surprise coming next…
    </h2>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

