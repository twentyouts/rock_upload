from views import upload, hello, make_upload

def setup_routes(app):
    app.router.add_get('/upload', upload)
    app.router.add_get('/', hello)
    app.router.add_post('/upload',make_upload)
