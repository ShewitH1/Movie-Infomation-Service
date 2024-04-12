from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

from repositories import image_repo

load_dotenv()

app = Flask(__name__)

@app.get('/')
def index():
    all_image = image_repo.get_all_images_table()
    # print(all_image)
    return render_template('index.html', images=all_image)

@app.get('/images/<int:image_id>')
def get_image(image_id):
    image = image_repo.get_image_bys_id(image_id)
    return render_template('image.html', image=image)

@app.get('/images/new')
def new_image():
    return render_template('new_image.html')


@app.post('/images')
def create_image():
    caption = request.form.get('caption')
    image_link = request.form.get('image_link')
    author_user = request.form.get('author_user')
    if not caption or not image_link or not author_user:
        return 'Bad Request', 400
    image_id = image_repo.create_image(caption, image_link, author_user)
    return redirect(f'/images{image_id}') 