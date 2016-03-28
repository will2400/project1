#!/usr/bin/env python2.7

"""
Columbia W4111 Intro to databases
Example webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser


A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""

import os
import time
import datetime
from flask import session
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
global name
name = ''
global s_item

global s_price

DATABASEURI = "postgresql://xw2400:BLTJHA@w4111db.eastus.cloudapp.azure.com/xw2400"


#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)


#
# START SQLITE SETUP CODE
#
# after these statements run, you should see a file test.db in your webserver/ directory
# this is a sqlite database that you can query like psql typing in the shell command line:
# 
#     sqlite3 test.db
#
# The following sqlite3 commands may be useful:
# 
#     .tables               -- will list the tables in the database
#     .schema <tablename>   -- print CREATE TABLE statement for table
# 
# The setup code should be deleted once you switch to using the Part 2 postgresql database
#
engine.execute("""DROP TABLE IF EXISTS test;""")
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")
#
# END SQLITE SETUP CODE
#



@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

@app.route('/')
def index():
  context =dict (data = name)
  return render_template("index.html", **context)

@app.route('/shoes1')
def shoes1():
  global s_item
  global s_price
  temp = []
  s_item = 1
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '1' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]

  context = dict(data = details)
  return render_template("shoes1.html", **context)

@app.route('/shoes2')
def shoes2():
  global s_item
  global s_price
  temp = []
  s_item = 2
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '2' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes2.html", **context)

@app.route('/shoes3')
def shoes3():
  global s_item
  global s_price
  temp = []
  s_item = 3
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '3' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes3.html", **context)

@app.route('/shoes4')
def shoes4():
  global s_item
  global s_price
  temp = []
  s_item = 4
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '4' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes4.html", **context)

@app.route('/shoes5')
def shoes5():
  global s_item
  global s_price
  temp = []
  s_item = 5
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '5' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes5.html", **context)

@app.route('/shoes6')
def shoes6():
  global s_item
  global s_price
  temp = []
  s_item = 6
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '6' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes6.html", **context)

@app.route('/shoes7')
def shoes7():
  global s_item
  global s_price
  temp = []
  s_item = 7
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '7' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes7.html", **context)

@app.route('/shoes8')
def shoes8():
  global s_item
  global s_price
  temp = []
  s_item = 8
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '8' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes8.html", **context)

@app.route('/shoes9')
def shoes9():
  global s_item
  global s_price
  temp = []
  s_item = 9
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '9' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes9.html", **context)

@app.route('/shoes10')
def shoes10():
  global s_item
  global s_price
  temp = []
  s_item = 10
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = 10 and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes10.html", **context)

@app.route('/shoes11')
def shoes11():
  global s_item
  global s_price
  temp = []
  s_item = 11
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '11' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes11.html", **context)

@app.route('/shoes12')
def shoes12():
  global s_item
  global s_price
  temp = []
  s_item = 12
  cursor = g.conn.execute("SELECT s.color, s.size, s.price, l.sale_price, l.starting_date, l.ending_date, b.brand_name, b.rating, t.type_name FROM shoes s, brands b, made_from m, types_belong_to t, sales_addto l where s.item_id = '12' and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id and s.item_id = l.item_id")
  details = []
  for result in cursor:
    temp.append(result['price'])
    details.append('User: ')
    try:
      details.append(name)
    except:
      pass
    details.append('Color: ')
    details.append(result['color'])
    details.append('Size: ')
    details.append(result['size'])
    details.append('Regular Price: ')
    details.append(result['price'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('Brand: ')
    details.append(result['brand_name'])
    details.append('Rating: ')
    details.append(result['rating'])
    details.append('Type: ')
    details.append(result['type_name'])
  cursor.close()
  s_price = temp[0]
  context = dict(data = details)
  return render_template("shoes1.html2", **context)

@app.route('/addtocart')
def addtocart():
  try:
    sql = 'INSERT INTO cart values (%s,%s,%s)'
    args = (name, s_item, s_price)
    g.conn.execute(sql, args)
    context = dict(data1 = 'Successfully add to cart')
  except:
    context = dict(data1 = 'No user information detected, please log in first!')
  return render_template("shoes1.html", **context)

@app.route('/cart')
def cart():
  try:
    sql = 'SELECT c.user_id, c.item_id, s.color, s.size, s.price, b.brand_name, b.rating, t.type_name FROM cart c, shoes s, brands b, made_from m, types_belong_to t where c.user_id = %s and c.item_id = s.item_id and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id' 
    args = (name)
    cursor = g.conn.execute(sql, args)
    details = []
    for result in cursor:
      details.append('User: ')
      details.append(result['user_id'])
      details.append('Item id: ')
      details.append(result['item_id'])
      details.append('Color: ')
      details.append(result['color'])
      details.append('Size: ')
      details.append(result['size'])
      details.append('Regular Price: ')
      details.append(result['price'])
      details.append('Brand: ')
      details.append(result['brand_name'])
      details.append('Rating: ')
      details.append(result['rating'])
      details.append('Type: ')
      details.append(result['type_name'])
    cursor.close()
    context = dict(data = details)
  except:
    context = dict(data1 = 'No user information detected, please log in first!')
  return render_template("cart.html", **context)
 
@app.route('/emptycart')
def emptycart():
  sql4 = 'delete from cart where user_id = %s'
  arg4 = (name)
  g.conn.execute(sql4, arg4)

@app.route('/sale')
def sale():
  cursor = g.conn.execute("SELECT item_id, sale_price, starting_date, ending_date FROM sales_addto")
  details = []
  for result in cursor:
    details.append('Item: ')
    details.append(result['item_id'])
    details.append('Sale Price: ')
    details.append(result['sale_price'])
    details.append('Sale Starting at: ')
    details.append(result['starting_date'])
    details.append('Sale Ending at: ')
    details.append(result['ending_date'])
    details.append('************************************************')
  cursor.close()
  context = dict(data = details)
  return render_template("sale.html", **context)

@app.route('/order')
def order():
  try:
    sql = 'SELECT p.user_id, p.order_id, d.item_id, d.qty, p.date, p.total_cost, o.delivery_date, o.shipping_status, o.address from pay p, orders o, details d where p.user_id = %s and p.order_id = o.order_id and o.order_id = d.order_id'
    args = name
    cursor = g.conn.execute(sql, args)
    details = []
    for result in cursor:
      details.append('User: ')
      details.append(result['user_id'])
      details.append('Order Number: ')
      details.append(result['order_id'])
      details.append('Contain item: ')
      details.append(result['item_id'])
      details.append('Quantity: ')
      details.append(result['qty'])
      details.append('Order Date: ')
      details.append(result['date'])
      details.append('Total Price: ')
      details.append(result['total_cost'])
      details.append('Delivery Date: ')
      details.append(result['delivery_date'])
      details.append('Shipping  Status: ')
      details.append(result['shipping_status'])
      details.append('Address: ')
      details.append(result['address'])
    cursor.close()
    context = dict(data = details)
  except:
    context = dict(data1 = 'No user information detected, please log in first!')
  return render_template("order.html", **context)

@app.route('/addtowishlist')
def addtowishlist():
  try:
    sql = 'INSERT INTO wishlists values (%s,%s)'
    args = (name, s_item)
    g.conn.execute(sql, args)
    context = dict(data1 = 'Successfully add to wishlist')
  except:
    context = dict(data1 = 'No user information detected, please log in first!')
  return render_template("shoes1.html", **context)

@app.route('/wishlist')
def wishlist():
  try:
    sql = 'SELECT w.user_id, w.item_id, s.color, s.size, s.price, b.brand_name, b.rating, t.type_name FROM wishlists w, shoes s, brands b, made_from m, types_belong_to t where w.user_id = %s and w.item_id = s.item_id and b.bid = m.bid and s.item_id = m.item_id and s.item_id = t.item_id' 
    args = (name)
    cursor = g.conn.execute(sql, args)
    details = []
    for result in cursor:
      details.append('User: ')
      details.append(result['user_id'])
      details.append('Item id: ')
      details.append(result['item_id'])
      details.append('Color: ')
      details.append(result['color'])
      details.append('Size: ')
      details.append(result['size'])
      details.append('Regular Price: ')
      details.append(result['price'])
      details.append('Brand: ')
      details.append(result['brand_name'])
      details.append('Rating: ')
      details.append(result['rating'])
      details.append('Type: ')
      details.append(result['type_name'])
    cursor.close()
    context = dict(data = details)
  except:
    context = dict(data1 = 'No user information detected, please log in first!')
  return render_template("wishlist.html", **context)


@app.route('/another')
def another():
  return render_template("anotherfile.html")

@app.route('/wrong')
def wrong():
  return render_template("wrong.html")

@app.route('/checkout')
def checkout():
  total=[]
  totals = []
  total_price = 0
  sql = 'SELECT price from cart where user_id = %s'
  args = (name)
  cursor = g.conn.execute(sql, args)
  for result in cursor:
    total.append(result['price'])
  cursor.close()
  for i in range(0, len(total)):
    total_price = total_price + total[i]
  totals.append('Total Price is :') 
  totals.append(total_price)
  context=dict(data = totals)
  return render_template("confirm.html", **context)

@app.route('/confirm', methods=['POST'])
def confirm():
  try:
    itemid=[]
    quantity=[]
    lastorder=[]
    total=[]
    totals = []
    total_price = 0
    sql = 'SELECT price from cart where user_id = %s'
    args = (name)
    cursor = g.conn.execute(sql, args)
    for result in cursor:
      total.append(result['price'])
    cursor.close()
    for i in range(0, len(total)):
      total_price = total_price + total[i]

    cursor1 = g.conn.execute("SELECT order_id from orders order by order_id desc limit 1")
    for result in cursor1:
      lastorder.append(result['order_id'])
    cursor1.close()
    neworder = lastorder[0] + 1
    deliverydate = datetime.datetime.now()
    print deliverydate
    shippingstatus = 'ready for ship'
    address = request.form['address']
    print address
    sql = 'INSERT INTO orders values (%s,%s,%s,%s)'
    args = (neworder, deliverydate, shippingstatus, address)
    g.conn.execute(sql, args)
    sql1 = 'INSERT INTO pay values (%s,%s,%s,%s)'
    args1 = (name, neworder, deliverydate, total_price)
    g.conn.execute(sql1, args1)


    itemiddd = []
    quann = []
    sql3 = 'SELECT item_id, count(*) from cart where user_id = %s group by item_id'
    args3 = (name)
    cursor2 = g.conn.execute(sql3, args3)
    for result in cursor2:
      itemiddd.append(result['item_id'])
      quann.append(result['count'])
    cursor2.close

    for i in range(0, len(itemiddd)):
      print itemiddd[i],quann[i]
      sql2 = 'INSERT INTO details values (%s,%s,%s)'
      args2 = (neworder, itemiddd[i], quann[i])
      g.conn.execute(sql2, args2)

    #clean the cart
    sql4 = 'delete from cart where user_id = %s'
    arg4 = (name)
    g.conn.execute(sql4, arg4)

    context=dict(data1="Order Placed")
    return render_template("confirm.html", **context)
  except:
    pass

@app.route('/signup')
def signup():
  return render_template("adduser.html")

# Example of adding new data to the database
@app.route('/adduser', methods=['POST'])
def adduser():
  try:
    user = request.form['user']
    password = request.form['password']
    email = request.form['email']
    first = request.form['first']
    last = request.form['last']
    age = request.form['age']
    g.conn.execute("INSERT INTO customers values ('%s','%s','%s','%s','%s','%s')" %(user,password,email,first,last,age))
    context = dict(data = 'Successfully sign up, please log in')
    return render_template("index.html", **context)
  except:
    context = dict(data = 'Please recheck the sign up requirements')
    return render_template("adduser.html", **context)

@app.route('/login', methods=['POST'])
def login():
  global name
  cursor = g.conn.execute("SELECT user_id FROM customers")
  ids = []
  for result in cursor:
    ids.append(result['user_id'])  # can also be accessed using result[0]
  cursor.close()

  cursor = g.conn.execute("SELECT password FROM customers")
  psw = []
  for result in cursor:
    psw.append(result['password'])  # can also be accessed using result[0]
  cursor.close()
  
  name = request.form['u_id']
  passW= request.form['passw']
  print passW


  for i in ids:
    if name in i :
      for j in psw:
        if passW in j:
          context = dict (data = name)
          return render_template("index.html", **context)
  context = dict(data = 'Wrong username or password')
  return render_template("index.html", **context)



if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
