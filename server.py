from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
	return "본 API는 GET 형식 요청을 받지 않습니다."

@app.route('/', methods=['POST'])
def main():
    requestData = request.json

    f = open("request" + ".yak", 'w')
    f.write(requestData['code'])
    f.close()

    result = subprocess.Popen(['yaksok', "request" + ".yak"], stdout=subprocess.PIPE, text=True)
    stdout, stderr = result.communicate()
    if result.returncode != 0:
        finalResult = "오류가 발생하였습니다. 약속 코드에 문제가 있는지 확인해주세요."
        return jsonify({"result": finalResult}), 401
    else:
        finalResult = stdout[:(len(stdout)-1)]
        return jsonify({"result": finalResult}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)