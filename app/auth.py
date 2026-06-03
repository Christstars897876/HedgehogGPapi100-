import functools
from flask import request, jsonify
import os

VALID_KEYS = {'sk-test-abc123', 'sk-prod-xyz789', os.environ.get('MOTADEV_API_KEY', 'mtd_key1050789750IDEK')}

def require_api_key(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        key = request.headers.get('X-API-Key') or request.args.get('api_key')
        if key not in VALID_KEYS:
            return jsonify({'error': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    return wrapper

