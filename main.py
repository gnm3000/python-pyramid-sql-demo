from waitress import serve
from pyramid.config import Configurator

def main():
    with Configurator() as config:
        config.include('pyramid_mako')
        config.add_mako_renderer('.mako')
        config.add_route('hello', '/')
        config.add_route('customer_info', '/db/Chinook/Customer/{field}/{value}.html')
        config.add_route('generic_query', '/db/Chinook/{table}/{field}/{value}.html')
        config.scan('views')  # this will scan decorations for my views.py file
        app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = main()
    serve(app, host='0.0.0.0', port=6543)