swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "School API",
        "description": "API for managing school students",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http", "https"],
    "paths": {},
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flask-swagger-ui",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}
