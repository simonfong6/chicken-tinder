#!/usr/bin/env python3
"""
Keeps track of number of clients and
"""
from collections import Counter


class RestaurantRoom:
    """
    Attributes:
        room: Room name.
        clients_count: Number of clients in room.
        hit_counter: Keeps track the number of accepts.
    """

    def __init__(self):
        self.clients_count = 0
        self.hit_counter = Counter()

    def reset(self):
        self.__init__()

    def set_clients_count(self, count):
        self.clients_count = count

    def increment_clients_count(self):
        self.clients_count += 1
    
    def add_hit(self, restaurant):
        self.hit_counter[restaurant] += 1

    def is_match(self, restaurant):
        return self.hit_counter[restaurant] == self.clients_count
