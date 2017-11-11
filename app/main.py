import bottle
import os
import random
<<<<<<< HEAD
import snake
=======
import movesnake
>>>>>>> 58a1a6cdeff865ccdd49762e989c8e5c2a319d48

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data
    
    return {
        'color': '#7F3FBF',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Jarmin'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    # directions = ['up', 'down', 'left', 'right']

    return {
        'move': movesnake.moveSnake(),
        'taunt': 'dont snake with me'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
