from flask import Blueprint, request, jsonify
from .models import Articles
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/articles', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    articles_list = []
    for article in all_articles:
        article_data = {
            'id': article.id,
            'title': article.title,
            'body': article.body,
            'date': article.date
        }
        articles_list.append(article_data)

    return jsonify(articles_list)

@views.route('/article/<int:id>/', methods=['GET'])
def article_details(id):
    article_detail = Articles.query.get(id)
    if article_detail:
        article_data = {
            'id': article_detail.id,
            'title': article_detail.title,
            'body': article_detail.body
        }
        return jsonify(article_data)
    
    else:
        return 'No article with that ID'
    
@views.route('/article', methods=['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']

    new_article = Articles(title, body)
    db.session.add(new_article)
    db.session.commit()

    article_data = {
        'id': new_article.id,
        'title': new_article.title,
        'body': new_article.body
    }
    return jsonify(article_data)

@views.route('/article/<int:id>/', methods=['PUT'])
def update_article(id):
    update_article = Articles.query.get(id)
    if update_article:
        update_article.title = request.json['title']
        update_article.body = request.json['body']
        db.session.commit()

        updated_article_data = {
            'id': update_article.id,
            'title': update_article.title,
            'body': update_article.body,
        }
        return jsonify(updated_article_data)

    else:
        return 'No article with that ID'
    
@views.route('/article/<int:id>/', methods=['DELETE'])
def delete_article(id):
    delete_article = Articles.query.get(id)
    if delete_article:
        db.session.delete(delete_article)
        db.session.commit()

        delete_article_data = {
            'id': delete_article.id,
            'title': delete_article.title,
            'body': delete_article.body
        }
        return jsonify(delete_article_data)
    
    else:
        return 'No article with that ID'