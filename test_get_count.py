#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
'''
print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))


first_state_id = list(storage.all(State).values())[0].id

print("First state: {}".format(storage.get(State, first_state_id)))

print(storage.get(State, first_state_id))
'''
req = {"name": "California is so cool"}
print(req)
for nem in ['id', 'created_at', 'updated_at']:
    req.pop(nem, None)
print(req)
obj = State(req)
print(obj.to_dict())
storage.new(obj)
storage.save()


