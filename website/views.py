from flask import Blueprint, render_template, request, flash
import api


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            playername = request.form['playername']
            if not playername:
                raise AttributeError
                
            player = api.call_api(playername)
            return render_template("single_stats.html", stats=player.player_stats, name=player.player_name,
                                   stat_map=api.stat_name_map)
        except AttributeError:
            flash("Player name is invalid", "error")
    return render_template("index.html")


@views.route('/stats', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        try:
            playername = request.form['playername']
            if not playername:
                raise AttributeError
                
            player = api.call_api(playername)
            return render_template("single_stats.html", stats=player.player_stats, name=player.player_name,
                                   stat_map=api.stat_name_map)
        except AttributeError:
            flash("Player name is invalid", "error")
    return render_template("index.html")
    """
    if request.method == 'POST':
        playername = request.form['playername']
        playername2 = request.form['playername2']
        if (not playername) or (not playername2):
            flash("You didn't enter in two players.")
        else:
            print(playername, playername2)
    return render_template("compare.html")
    """
