#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:10:41 2019

@author: deeparora
"""


from flask import Flask, jsonify
from Chatbot import Chatbot


app = Flask(__name__)


@app.route("/chat/<string:input>",methods=['GET'])
def respondMe(input):
    chatbot  = Chatbot.getInstance()
    reply = chatbot.reply(input)
    return jsonify({'reply': reply})
    


if __name__ == "__main__":
    app.run(debug=True)
    
    
    
