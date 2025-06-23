from flask import Blueprint, request, jsonify
from server.models.appearance import Appearance
from server.models import db

appearance_bp = Blueprint("appearances", __name__)

@appearance_bp.route("/appearances", methods=["GET"])

def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([{
        "id": appearance.id,
        "rating": appearance.rating,
        "guest_id": appearance.guest_id,
        "episode_id": appearance.episode_id
    } for appearance in appearances])
