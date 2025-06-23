from flask import Blueprint, request, jsonify
from server.models.episode import Episode
from server.models import db

episode_bp = Blueprint('episodes',__name__)

@episode_bp.route('/episodes',methods =['GET'])
def get_episodes():
    
    episodes = Episode.query.all()

    return jsonify([{'id':episode.name, 'number':episode.number,'date':episode.date.isoformat()}for episode in episodes])