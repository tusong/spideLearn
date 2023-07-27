#!/bin/sh
if [ $# -eq 0 ]
then exit 1
fi

DIR="/data/svndata/svn/$1"

#创建备份仓库
if [ -d $DIR ]
  then
        echo "$DIR 已存在"
  else
        svnadmin create $DIR
fi

#添加钩子
if [ -d "$DIR/hooks" ]
  then
        echo -e "#!/bin/sh\nexit 0" > "$DIR/hooks/pre-revprop-change"
        echo -e "#!/bin/sh\nexit 0" > "$DIR/hooks/start-commit"
        chmod 775 "$DIR/hooks/pre-revprop-change" "$DIR/hooks/start-commit"
  else
        echo "仓库创建失败"
        exit 1
fi

echo "操作成功"
exit 0

