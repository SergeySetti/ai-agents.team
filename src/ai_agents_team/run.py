from waitress import serve
from ai_agents_team.app import create_app

app = create_app()

def run():
    serve(app, host="0.0.0.0", port=8080)

def dev_run():
    app.run(port=5000, debug=True)
