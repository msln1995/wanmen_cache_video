import wanmen.token
import wanmen.http
import wanmen.file
import wanmen.db
import json
import sys

if len(sys.argv) < 2:
    print("参数错误");
    exit();

coursesId = str(sys.argv[1])
wanmen.file.createDir("tmp")
wanmenDb = wanmen.db.WanmenDb();

# 是否新的
taskType = input("是否是新的任务y/n(默认n):")
if taskType.lower() == 'y':
    wanmenDb.truncate()

f = open('./Authorization.ini', 'r')
Authorization = f.read()
token = wanmen.token.getXToken()
# 获取课程目录
url = "https://api.wanmen.org/4.0/content/courses/" + coursesId + "/catalogue"
info = wanmen.http.getMethod(url, Authorization , token['x_time'], token['xtoken'])

def runData(item):
    # 阶段
    wanmen.file.createDir(item["name"])
    runLectures(item["lectures"], item)

def runLectures (list, item=None):
    for item2 in list:
        # 章节
        if (item == None):
            rootPath = item2["prefix"] + '.' + item2["name"]
            print(item2["prefix"] + '.' + item2["name"])
        else:
            rootPath = item["prefix"] + '.' + item["name"] + "\\" + item2["prefix"] + '.' + item2["name"]
            print(item["prefix"] + '.' + item["name"])

        wanmen.file.createDir(rootPath)
        for item3 in item2["children"]:
            if item3['actions']['watch'] != True and item3['actions']['download'] != True:
                print("没有课程的权限");
                exit()
            # print(item3["name"] + "   "  + item3["_id"]) #课程
            if item3["_id"] == None or item3["_id"] == "":
                break
            print(item3['name'])
            if wanmenDb.hasFlag(item3['name']):
                print("已缓存过，跳过")
                continue
            pcHigh = wanmen.http.getVidenInfo(item3["_id"], Authorization, token)
            wanmen.file.truncateDir();
            wanmen.file.createDir("tmp")
            wanmen.http.download(pcHigh['pcHigh'],"./Download/tmp",Authorization, token['x_time'], token['xtoken'])
            pathAddr = wanmen.file.currDirPath(rootPath)
            wanmen.file.combine("./Download/tmp",pathAddr,item3["prefix"] + item3["name"]);
            wanmen.file.truncateDir();
            wanmenDb.insert(item3['name'], 1)
        print("\r\n");

res = info.content;
课程列表 = json.loads(res)
if len(课程列表["phases"]) > 0:
    for item in 课程列表["phases"]:
        runData(item)
elif len(课程列表["lectures"]) > 0:
    runLectures(课程列表["lectures"])
