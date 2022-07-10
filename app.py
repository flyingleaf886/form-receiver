from flask import Flask, jsonify, render_template, request, json
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/users")
def users():
    users = [{'name': 'test1'}, {'name': 'test2'}]
    return jsonify(data=users)


@app.route("/users/<id>")
def user(id):
    return jsonify(data={'name': 'test1'})


@app.route("/get_json", methods=['POST'])
def get_json():
    data = request.json
    result = {"bind_code": "f1dd05f1332c4473aa727f900902bf2e"}

    response_text = f'json = {data}\n'
    try:
        with open('json.txt', 'wt') as json_file:
            json_file.write(str(data))
    except Exception as ex:
        response_text = response_text + str(ex) + '\n'
    except:
        response_text = response_text + 'excetion not catched\n'
    finally:
        response_text = response_text + 'after write operation\n'
        response_text = response_text + str(result)
    return json.dumps(response_text)


# HTTP 直通函数由于是基于 docker 镜像运行，所以必须监听地址为 0.0.0.0，并且端口为 9000
app.run(host = '0.0.0.0', port = 9000)


