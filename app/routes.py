from flask import Blueprint, jsonify, request
from app.database import get_db
from app.auth import require_api_key

bp_routes = Blueprint('routes', __name__)

@bp_routes.route('/')
def home():
    return jsonify({
        'status': 'online',
        'message': 'Bienvenue sur l\'API REST Flask de MotaDev',
        'docs': '/api/v1/posts'
    })

@bp_routes.route('/api/v1/posts', methods=['GET'])
def list_posts():
    page     = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    offset   = (page - 1) * per_page

    db    = get_db()
    posts = db.execute(
        'SELECT * FROM posts ORDER BY created_at DESC LIMIT ? OFFSET ?',
        (per_page, offset)
    ).fetchall()
    
    total_row = db.execute('SELECT COUNT(*) FROM posts').fetchone()
    total = total_row[0] if total_row else 0

    return jsonify({
        'data': [dict(p) for p in posts],
        'meta': {'page': page, 'per_page': per_page, 'total': total},
    })

@bp_routes.route('/api/v1/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = get_db().execute(
        'SELECT * FROM posts WHERE id=?', (post_id,)
    ).fetchone()
    if not post:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(dict(post))

@bp_routes.route('/api/v1/posts', methods=['POST'])
@require_api_key
def create_post():
    data  = request.get_json(silent=True) or {}
    title = data.get('title', '').strip()
    body  = data.get('body', '').strip()

    if not title or not body:
        return jsonify({'error': 'title and body are required'}), 422

    db = get_db()
    cur = db.execute(
        'INSERT INTO posts (title, body) VALUES (?,?)', (title, body)
    )
    db.commit()
    return jsonify({'id': cur.lastrowid, 'title': title}), 201

@bp_routes.route('/api/v1/posts/<int:post_id>', methods=['DELETE'])
@require_api_key
def delete_post(post_id):
    db = get_db()
    db.execute('DELETE FROM posts WHERE id=?', (post_id,))
    db.commit()
    return '', 204

