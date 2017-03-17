# bultin library
from uuid import uuid4

from sanic import Sanic
from sanic.response import html, redirect, text, json
from jinja2 import Environment, PackageLoader

import qr_control as qr


DATABASE = []


env = Environment(
    loader=PackageLoader("app", "templates"),
)


app = Sanic(__name__)
app.static("/static", "./static")


@app.route("/")
async def root(request):
    return redirect(app.url_for('signup'))


@app.route("/signup")
async def signup(request, methods=['GET']):
    token = str(uuid4().hex)
    host = request.headers.get("Host")
    DATABASE.append(token)
    qr.image(
        f"{host}/signin?token={token}", f"./static/codes/{token}.svg"
    )
    template = env.get_template("signup.html")
    html_content = template.render(path=f"/static/codes/{token}.svg")
    return html(html_content)


@app.route("/signin")
async def signin(request, methods=['GET']):
    token = request.args['token'][0]
    if token not in DATABASE:
        return text(":<")
    return text(":>")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )
