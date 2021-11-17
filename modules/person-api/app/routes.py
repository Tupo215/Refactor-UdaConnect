def register_routes(api, app, root="api"):
    from app.person import register_routes as attach_person

    # Add routes
    attach_person(api, app)
