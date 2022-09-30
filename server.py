from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)


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
    else:
        finalResult = stdout[:(len(stdout)-1)]


    return jsonify({"result": finalResult}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)