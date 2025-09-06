from waitress import serve

from ai_agents_team.app import create_app

def run():
    app = create_app()
    serve(app, host="127.0.0.1", port=8080)

def dev_run():
    app = create_app()
    app.run(port=5000, debug=True)