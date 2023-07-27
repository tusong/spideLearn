#!/bin/sh
if [ $# -eq 0 ]
then exit 1
fi

#仓库绝对路径
DIR="/data/svndata/svn/$1"

#创建备份仓库
if [ -d $DIR ]
  then
        echo "开始"
  else
        echo "$DIR 仓库不存在"
        exit 1
fi

#添加钩子
if [ -d "$DIR/hooks" ]
  then
        echo -e "#!/bin/sh\nexit 0" > "$DIR/hooks/pre-revprop-change"
        chmod 775 "$DIR/hooks/pre-revprop-change"
        echo "添加钩子成功"
  else
        echo "$DIR 仓库不存在"
        exit 1
fi

echo "开始初始化"
svnsync init https://svn.tydic.com/svnhftmp/$1 file://$DIR --username 'adminchaojiguanliyuan' --password 'Tydk123@'

if [ $? -eq 0 ]
    then
        echo "初始化成功"
    else 
        echo "初始化失败"
        exit 1
fi

echo "开始同步"
svnsync synchronize --non-interactive https://svn.tydic.com/svnhftmp/$1 --username 'adminchaojiguanliyuan' --password 'Tydk123@'

if [ $? -eq 0 ]
    then
        echo "同步成功"
    else 
        echo "同步失败"
        exit 1
fi

echo "操作成功"
exit 0

