from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS
import json
from UserControl import login, register, find, editInfo, changePassword, editUserInfo
from PaperControl import purchase, download
from ResourceControl import comment, findComment
from ScholarControl import editScholarInfo, authenticate, manageResource, addScholar, findScholarByKwd, findScholar, getAuthentication, verification
from SearchControl import searchPaper, getPaperByID
from CollectionControl import subscribe, manageCollection, collectPaper, getPaperList, getSubscribeList
import pymongo
import time
import sys

myclient = pymongo.MongoClient('mongodb://106.14.150.33:27017')
mydb = myclient["test"]
logcol = mydb['requestLog']


app = Flask(__name__)
CORS(app, supports_credentials=True)

PORT = 5015


def write_log(data, ans, fun_name):
    log = {
        'address': fun_name,
        'time': time.time(),
        'data': data,
        'ans': ans
    }
    logcol.insert_one(log)


def error(e):
    dic = {
        "code": 0,
        "msg": e,
        "data": {
        }
    }
    return dic


@app.route("/")
def show_web():
    return render_template('main.html')


@app.route("/api/user/login", methods=['POST'])
def user_login():
    data = json.loads(request.data)
    try:
        code = 100
        userID = login(username=data['username'], password=data['password'])
        if not userID or userID == 0:
            code = 101
        if userID == -100:
            code = 102
        elif userID == -200:
            code = 103
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "userID": userID,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/user/register", methods=['POST'])
def user_register():
    data = json.loads(request.data)
    try:
        code = 100
        userID = register(username=data['username'], password=data['password'], email=data['email'])
        if userID == 0:
            code = 104
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "userID": userID,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/user/find", methods=['POST'])
def user_find():
    data = json.loads(request.data)
    try:
        code = 100
        user = find(userID=data['userID'])
        if user is None:
            code = 105
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "user": user,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/user/edit_info", methods=['POST'])
def user_edit_info():
    data = json.loads(request.data)
    try:
        code = 100
        flag = editInfo(userID=data['userID'], introduction=data['introduction'], organization=data['organization'])
        if not flag:
            code = 106
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/user/change_pwd", methods=['POST'])
def user_change_pwd():
    data = json.loads(request.data)
    try:
        code = 100
        flag = changePassword(userID=data['userID'], oldPassword=data['oldPassword'], newPassword=data['newPassword'])
        if not flag:
            code = 107
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/user/edit", methods=['POST'])
def user_edit():
    data = json.loads(request.data)
    try:
        code = 100
        info = {}
        for key in data['info'].keys():
            if data['info'][key]:
                info[key] = data['info'][key]
        flag = editUserInfo(userID=data['scholarID'], data=info)
        if not flag:
            code = 401
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    return json.dumps(ans)


@app.route("/api/paper/purchase", methods=['POST'])
def paper_purchase():
    data = json.loads(request.data)
    try:
        code = 100
        flag = purchase(userID=data['userID'], paperID=data['paperID'])
        if not flag:
            code = 201
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/paper/downloads", methods=['POST'])
def paper_downloads():
    data = json.loads(request.data)
    try:
        code = 100
        url = download(userID=data['userID'], paperID=data['paperID'])
        if not url:
            code = 202
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "url": url,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/resource/comment", methods=['POST'])
def resource_comment():
    data = json.loads(request.data)
    try:
        code = 100
        flag = comment(userID=data['userID'], resourceID=data['resourceID'], content=data['content'])
        if not flag:
            code = 301
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/resource/get_comment", methods=['POST'])
def resource_get_comment():
    data = json.loads(request.data)
    try:
        code = 100
        result = findComment(resourceID=data['resourceID'])
        if result is None:
            code = 302
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "result": result,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/scholar/edit", methods=['POST'])
def scholar_edit():
    data = json.loads(request.data)
    try:
        code = 100
        info = {}
        for key in data['info'].keys():
            info[key] = data['info'][key]
        flag = editScholarInfo(scholarID=data['scholarID'], data=info)
        if not flag:
            code = 401
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    return json.dumps(ans)


@app.route("/api/scholar/auth", methods=['POST'])
def scholar_auth():
    data = json.loads(request.data)
    try:
        code = 100
        flag = authenticate(userID=data['userID'], scholarID=data['scholarID'], email=data['email'])
        if not flag:
            code = 402
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/scholar/getAuth", methods=['POST'])
def scholar_getAuth():
    try:
        code = 100
        authenticationList = getAuthentication()
        if authenticationList is None:
            code =402
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "authenticationList": authenticationList,
            }
        }
    except Exception as e:
        ans = error(e)

    return json.dumps(ans)


@app.route("/api/scholar/verification", methods=['POST'])
def scholar_verification():
    data = json.loads(request.data)
    try:
        code = 100
        flag = verification(id = data['id'])
        if not flag:
            code =402
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/scholar/manage", methods=['POST'])
def scholar_manage():
    data = json.loads(request.data)
    try:
        code = 100
        flag = manageResource(resourceID=data['resourceID'], cmd=data['cmd'], newPrice=data['newPrice'])
        if not flag:
            code = 403
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)
    write_log(data, ans, sys._getframe().f_code.co_name)
    return json.dumps(ans)


@app.route("/api/scholar/add", methods=['POST'])
def scholar_add():
    data = json.loads(request.data)
    try:
        code = 100
        scholarID = addScholar(name=data['name'])
        if not scholarID:
            code = 404
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "scholarID": scholarID,
            }
        }
    except Exception as e:
        ans = error(e)
    write_log(data, ans, sys._getframe().f_code.co_name)
    return json.dumps(ans)


@app.route("/api/scholar/find_by_id", methods=['POST'])
def scholar_find_by_id():
    data = json.loads(request.data)
    try:
        code = 100
        scholarInfo = findScholar(scholarID=data['scholarID'])
        if scholarInfo is None:
            code = 405
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "scholarInfo": scholarInfo,
            }
        }
    except Exception as e:
        ans = error(e)
    write_log(data, ans, sys._getframe().f_code.co_name)
    return json.dumps(ans)


@app.route("/api/scholar/find_by_kwd", methods=['POST'])
def scholar_find_by_kwd():
    data = json.loads(request.data)
    try:
        code = 100
        scholarInfo = findScholarByKwd(kwd=data['keyword'])
        if scholarInfo is None:
            code = 406
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "scholarInfo": scholarInfo,
            }
        }
    except Exception as e:
        ans = error(e)
    write_log(data, ans, sys._getframe().f_code.co_name)
    return json.dumps(ans)


@app.route("/api/search/paper", methods=['POST'])
def search_paper():
    data = json.loads(request.data)
    try:
        code = 100
        result = searchPaper(data['keyword'])
        if result is None:
            code = 501
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "result": result
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/search/paper_id", methods=['POST'])
def search_paper_id():
    data = json.loads(request.data)
    try:
        code = 100
        result = getPaperByID(data['id'])
        if result is None:
            code = 501
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "result": result
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/collection/subscribe", methods=['POST'])
def collection_subscribe():
    data = json.loads(request.data)
    try:
        code = 100
        flag = subscribe(userID=data['userID'], scholarID=data['scholarID'], cmd=data['cmd'])
        if not flag:
            code = 601
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/collection/paper", methods=['POST'])
def collection_paper():
    data = json.loads(request.data)
    try:
        code = 100
        flag = collectPaper(userID=data['userID'], paperListID=data['paperListID'], cmd=data['cmd'], paperID=data['paperID'])
        if not flag:
            code = 602
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/collection/manage", methods=['POST'])
def collection_manage():
    data = json.loads(request.data)
    try:
        code = 100
        flag = manageCollection(userID=data['userID'], paperListID=data['paperListID'], cmd=data['cmd'], name=data['name'])
        if not flag:
            code = 603
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "flag": flag,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/collection/get_paper_list", methods=['POST'])
def collection_get_paper_list():
    data = json.loads(request.data)
    try:
        code = 100
        paperList = getPaperList(userID=data['userID'], paperListID=data['paperListID'])
        if paperList is None:
            code = 604
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "paperList": paperList,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)


@app.route("/api/collection/get_subscribe_list", methods=['POST'])
def collection_get_subscribe_list():
    data = json.loads(request.data)
    try:
        code = 100
        subscribeList = getSubscribeList(userID=data['userID'])
        if subscribeList is None:
            code = 605
        ans = {
            "code": code,
            "msg": "OK",
            "data": {
                "subscribeList": subscribeList,
            }
        }
    except Exception as e:
        ans = error(e)

    write_log(data, ans, sys._getframe().f_code.co_name)

    return json.dumps(ans)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
