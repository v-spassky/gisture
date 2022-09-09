import os
import glob
from uuid import uuid4
from zipfile import ZipFile
from flask import (
    Flask,
    request,
    send_from_directory,
    send_file,
)
import fiona
import matplotlib.pyplot as plt

"""
This module initializes Flask application and declares endpoints.
"""

app = Flask(__name__)


@app.route('/')
def home():
    """
    Renders home page.
    """

    return send_from_directory(
        'static',
        'index.html',
        mimetype='text/html',
    )


@app.route('/favicon.ico')
def favicon():
    """
    Serves the favicon.ico file.
    """

    return send_from_directory(
        'static',
        'favicon.ico',
        mimetype='image/x-icon',
    )


@app.errorhandler(404)
def page_not_found(e):
    """
    Renders custom 'Not found' if any route
    throws response with the 404 status code.
    """

    return send_from_directory(
        'static',
        '404.html',
        mimetype='text/html',
    ), 404


@app.route('/process_archive', methods=['POST'])
def process_archive():
    """
    Handles shapefile processing. Expects .zip archive for input.
    Returns a .png represnetation of a given shapefile.
    """

    # TODO:
    # - clean up seved files;
    # - request has no file in it;
    # - archive doesn`t contain smth necessary;
    # - zip bomb diffusion;
    # - do some research on how to process it in memory;
    # - plt.close()???;

    upload_id = str(uuid4())

    archive = request.files['file']
    archive_name = f'temp/{upload_id}.zip'
    unpacking_folder_name = f'temp/{upload_id}'
    archive.save(archive_name)

    with ZipFile(archive_name, 'r') as zip_archive:
        os.mkdir(unpacking_folder_name)
        zip_archive.extractall(unpacking_folder_name)

    shapefiles = glob.glob(f'{unpacking_folder_name}/*.shp')
    shapefile_name = shapefiles[0]

    with fiona.open(shapefile_name) as shapefile:
        for item in shapefile:
            plt.plot(*zip(*item['geometry']['coordinates']))

    picture_path = f'temp/{upload_id}.png'

    plt.savefig(picture_path)

    return upload_id


@app.route('/download_output/<id>')
def download_output(id):
    """
    Serves the generated in '/process_archive' picture.
    """

    return send_from_directory(
        'temp',
        f'{id}.png',
        mimetype='image/png',
        as_attachment=True,
    )
