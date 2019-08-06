import os
import connexion

# Connexion setup
debugging = os.environ.get('debugging')
options = {"swagger_ui": debugging}
application = connexion.FlaskApp(
    __name__,
    specification_dir='swagger/',
    options=options
    )
application.add_api(
    'swagger.yaml',
    base_path='/api',
    arguments={'title': 'Sample API'}
    )

# Run
if __name__ == '__main__':
    application.run()