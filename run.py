from app import create_app

# Cria e executa a aplicação Flask
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)