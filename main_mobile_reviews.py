import bottle
import appcode

@bottle.route("/")
def any_name():
  return bottle.static_file("index.html", root="")

@bottle.route("/piechart")
def piechart():
    return appcode.piechart()

@bottle.route("/bubblechart")
def bubblechart():
    return appcode.bubblechart()

bottle.run(host="0.0.0.0", port=8080, debug=True)