from blogsite import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False) # debug=True is only for development

