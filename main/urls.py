'''
    Регистрирует все чертежи и делает для них путь (that's how urls.py works)
'''
from .settings import project
import tour, user, home
'Конец импортов'
tour.tour.add_url_rule(rule = "/tour/", view_func = tour.render_tour_page)
user.user_app.add_url_rule(rule = "/user/", view_func = user.show_user_app)
home.home.add_url_rule(rule = "/", view_func = home.render_home_page)
'Конец указаний пути'
project.register_blueprint(blueprint = user.user_app)
project.register_blueprint(blueprint = tour.tour)
project.register_blueprint(blueprint = home.home)
'Конец файла и регистрации чертежей'