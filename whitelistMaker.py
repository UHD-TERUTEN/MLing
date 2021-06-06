import json
import sqlite3
import contextlib

def internal(node, footprint, cursor):
  (parent, children), *rest = node.items()
  iterate(parent, children, footprint, cursor)
  return

def iterate(parent, children, footprint, cursor):
  for key, value in children.items():
    if type(value) == dict: # is internal node
      internal(value, footprint + [( parent, key )], cursor)
    elif value == 'YES':
      keys = ()
      values = ()
      for item in footprint + [( parent, key )]:
        keys += (item[0],)
        values += (item[1],)
      if len(keys) == 1:
        cursor.execute(f"INSERT OR IGNORE INTO whitelist('{keys[0]}') VALUES('{values[0]}')")
      else:
        cursor.execute(f"INSERT OR IGNORE INTO whitelist{str(keys)} VALUES{str(values)}")
  return

with contextlib.closing(sqlite3.connect('whitelist.sqlite')) as conn:
  with conn as cursor:
    with open('result.json', 'r', encoding='UTF8') as json_file:
      internal(json.load(json_file), [], cursor)
