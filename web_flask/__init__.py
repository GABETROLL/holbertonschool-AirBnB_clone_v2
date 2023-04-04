#!/usr/bin/python3
"""
Website files using Pytohn and flask
"""
app = __import__("0-hello_route.py").app
app.run(host="0.0.0.0", port=5000)
