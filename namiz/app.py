# namiz/app.py
from eve import Eve
from namiz.routes import register_routes
from namiz.utils.logger import get_logger
from flask import jsonify

def start_server():
    # Initialize logger
    logger = get_logger("app")
    logger.info("Starting the Eve API server...")
    
    # Initialize Eve app with settings
    app = Eve(settings='settings.py')
    
    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify("OK")

    # Register custom routes
    register_routes(app)
    
    logger.info("Eve API server is running.")
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    start_server()
