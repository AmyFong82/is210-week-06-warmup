#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Manipulating a tuple named Directions."""

import data

DIRECTIONS = data.DIRECTIONS
DIRECTIONS = DIRECTIONS[:-1] + ('West',)
