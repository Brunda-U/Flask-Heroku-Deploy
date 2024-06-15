from website import create_app
# website becomes python package when you put init.py file in it.
app = create_app()

if __name__ == '__main__':
	app.run(debug = True)