import os, hashlib

cur_path = os.path.dirname('c:/temp/pic/new')
sample_tree = os.walk(cur_path)

allmd5s = dict()
n = 0
for dirname, subdir, files in sample_tree:
    allfiles = []
    for file in files:
        ext = file.split('.')[-1]
        if ext.lower() == 'jpg' or ext.lower() == 'png':
            allfiles.append(os.path.join(dirname, file))

    if len(allfiles) > 0:
        for img in allfiles:
            img_md5 = hashlib.md5(open(img, 'rb').read()).digest()
            if img_md5 in allmd5s:
                if n == 0:
                    print("找到以下重复文件")
                    n += 1
                print(os.path.abspath(img))
                print(allmd5s[img_md5] + '\n')
            else:
                allmd5s[img_md5] = os.path.abspath(img)
