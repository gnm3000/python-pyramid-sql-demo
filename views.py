from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.orm import sessionmaker
from models import Customer
from sqlalchemy import text

from settings import engine


@view_config(route_name='hello')
def hello(request):
    return Response("hello")


@view_config(route_name='generic_query', renderer='templates/generic_query.mako')
def generic_query(request):
    table = request.matchdict.get('table')
    field = request.matchdict.get('field')
    value = request.matchdict.get('value')
    connection = engine.connect()
    sql_query = text("SELECT * FROM " + table + " WHERE " + field + " = '" + value + "'")
    result = connection.execute(sql_query)
    field_names = list(result.keys())
    data = result.fetchall()
    return {"data": data, "field_names": field_names, "table": table}


@view_config(route_name='customer_info', renderer='templates/customer_info.mako')
def customer_info(request):
    field = request.matchdict.get('field')
    value = request.matchdict.get('value')
    Session = sessionmaker(bind=engine)
    session = Session()
    customers = session.query(Customer).filter_by(**{field: value}).all()
    html = '<body><h1>Customer List</h1>'
    html += '<ul>'
    for customer in customers:
        html += f'<li>{customer.FirstName} {customer.LastName} - {customer.Country}</li>'
    html += '</ul></body>'
    return {'result': html}
