# routes/__init__.py
from namiz.routes.upload import upload_bp

def register_routes(app):
    app.register_blueprint(upload_bp)
