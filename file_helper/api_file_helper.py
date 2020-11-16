# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

import flask
from flask import request, jsonify
import file_helper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Anna's Ptojects</h1>
<p>A prototype API for file management </p>'''


@app.errorhandler(404)  # In HTML responses code 404 means “Not Found”
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/helpers', methods=['GET'])  # /api/v1/helpers?id=1
def api_filter():
    query_parameters = request.args  # grabs all the query parameters provided in the URL
    id = query_parameters.get('id')

    # `SELECT <columns> FROM <table> WHERE <column=match> AND <column=match>;
    query = "SELECT * FROM books WHERE"
    to_filter = []
    print_value = "Nothing happened"

    if id:
        id = int(id)
        query += ' id=? AND'
        to_filter.append(id)
        if id == 1:  # 1-> create file
            file_name = 'file1'
            file_helper.create_file(file_name)
            template_name = 'template'
            file_helper.copy_info(file_name, template_name)
            print_value = "You choose action 1 -> copy from template to a new file named: file1."
        elif id == 2:
            file_name = 'file1'
            template_name = 'template2'
            file_helper.add_info(file_name, template_name)
            print_value = "<p>You choose action 2 -> copy from template2 to the already existed file1.</p>"
        elif id == 3:
            file_name = 'file1'
            file_helper.delete_file(file_name)
            print_value = "<p>You choose action 3 -> delete file1.</p>"
    if not id:
        return page_not_found(404)

    return print_value

app.run()
