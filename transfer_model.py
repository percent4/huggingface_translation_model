# -*- coding: utf-8 -*-
# @Time : 2021/2/8 11:41
# @Author : Jclian91
# @File : transfer_model.py
# @Place : Yangpu, Shanghai
from flask import Flask
from flask import request, jsonify

from single_sentence_transfer import paragraph_transfer


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route("/transfer", methods=['GET',  'POST'])
def get_news():
    doc = [_+"。" for _ in request.get_json()["text"].split("。") if _]
    new_doc = paragraph_transfer(doc)
    return_result = {"doc": doc, "transfer doc": new_doc}
    return jsonify(return_result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)