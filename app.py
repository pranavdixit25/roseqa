from flask import Flask, request, render_template_string

app = Flask(__name__)

attempt = 0

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Q&A</title>
</head>
<body style="font-family:Arial; text-align:center; margin-top:80px;">

<h2>Enter password</h2>

<form method="post">
    <input type="text" name="password" required>
    <br><br>
    <button type="submit">Submit</button>
</form>

{% if error %}
    <p style="color:red;">Wrong password ❌</p>
{% endif %}

{% if hint %}
    <p style="color:gray;">Hint: "aap dudu ki kya ho?"</p>
{% endif %}

{% if success %}
    <h3>Access granted ✅</h3>
    <p>Next question coming soon…</p>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
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

    return render_template_string(
        HTML,
        error=error,
        hint=hint,
        success=success
    )

if __name__ == "__main__":
    app.run()
