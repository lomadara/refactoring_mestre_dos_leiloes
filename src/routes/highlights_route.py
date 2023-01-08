from flask import render_template
from instance import server

app = server.app

@app.route('/destaques', methods=['GET'])
def highlights():
    return render_template('highlights.html')