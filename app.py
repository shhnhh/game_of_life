from game_of_life import GameOfLife
from config import MyConfig
from forms import MyForm
from flask import *

app = Flask(__name__)
app.config.from_object(MyConfig)

@app.route('/')
def index():
    return render_template('index.html', form=MyForm())

@app.route('/live', methods=['get', 'post'])
def live():
    if request.method == 'POST':
        size = int(request.form.get('size', 25))
        GameOfLife(size, size)
    life = GameOfLife()
    life.counter += 1
    return render_template('live.html', life=life)

@app.route('/reload_world', methods=['post'])
def reload_world():
    life = GameOfLife()
    life.form_new_generation()
    life.counter += 1
    return json.dumps({'world': life.world, 
                       'old_world': life.old_world,
                       'counter': life.counter})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)