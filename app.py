import os
from flask import Flask, render_template, send_from_directory, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Ensure the folder exists

@app.route('/media/images')
def list_images():
    # Get all files in the uploads folder
    files = os.listdir(UPLOAD_FOLDER)
    # We pass the files to the HTML template
    return render_template('index_list.html', fruits=fruit_catalog)

# This route actually serves the image when you click the link
@app.route('/static/uploads/<filename>')
def serve_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/clear-catalog', methods=['POST', 'GET'])
def clear_catalog():
    global fruit_catalog
    fruit_catalog = [] # Reset the list to empty
    return jsonify({"status": "success", "message": "Catalog cleared"}), 200


fruit_catalog = []
# This is the "Doorway" where your script will knock
@app.route('/upload-fruit', methods=['POST'])
def upload_fruit():
    # 1. Check if an actual file was sent in the request
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    
    file = request.files['file']

    # 2. Extract text data sent from ParsingDescription
    # These keys must match the ones in your fruit_info dictionary
    fruit_name = request.form.get('name')
    fruit_weight = request.form.get('weight')
    fruit_desc = request.form.get('description')
    
    # 2. If the user didn't select a file
    if file.filename == '':
        return {"error": "No selected file"}, 400

    if file:
        # 3. Clean the filename for security
        filename = secure_filename(file.filename)
        # 4. Save the image into your static uploads folder
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        new_fruit = {
            "name": fruit_name,
            "weight": fruit_weight,
            "description": fruit_desc,
            "image_url": filename
        }
        fruit_catalog.append(new_fruit)

        return jsonify({
        "status": "success",
        "filename": filename,
        "message": f"Fruit {fruit_name} uploaded successfully!"
    }), 200

if __name__ == '__main__':
    # host='0.0.0.0' is required for Docker later
    app.run(host='0.0.0.0', port=5000, debug=True)