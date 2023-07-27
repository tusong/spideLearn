#!/bin/sh
API_NAME=service-inf
JAR_NAME=$API_NAME\.jar
#PID  代表是PID文件
PID=$API_NAME\.pid

DIR="/home/admin/eams/apps/service-inf"
PNAME="service-inf"
DLOG="/home/admin/eams/apps/service-inf/logs/"

#使用说明，用来提示输入参数
usage() {
    echo "Usage: sh 执行脚本.sh [start|stop|restart|status]"
    exit 1
}

#检查程序是否在运行
is_exist(){
  pid=`ps -ef|grep $JAR_NAME|grep -v grep|awk '{print $2}' `
  #如果不存在返回1，存在返回0
  if [ -z "${pid}" ]; then
   return 1
  else
    return 0
  fi
}

#启动方法
start(){
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${JAR_NAME} is already running PID=${pid} <<<"
  else
    java -Xms4096m -Xmx4096m -Xmn1024m -XX:MaxMetaspaceSize=512m -XX:+AggressiveOpts -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:ParallelGCThreads=16  -XX:+UnlockCommercialFeatures -XX:+FlightRecorder  -Dserver.tomcat.max-connections=1000 -Dserver.tomcat.max-threads=80  -Dserver.tomcat.min-spare-threads=10  -Dserver.session.cookie.name=eams-admin  -jar  -Dspring.cloud.nacos.config.server-addr=192.168.181.12:8848,192.168.181.13:8848,192.168.181.15:8848 -Dcom.alibaba.nacos.client.naming.ctimeout=30000  -Dserver.session.timeout=86400 -Dserver.tomcat.acceptorThreadCount=8 -Dserver.connectionTimeout=3000 -DtaskRun=run -Dspring.application.name=service-inf -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005  $PNAME.jar >logs/run.log 2>&1 &
        echo $! > $PID
    echo ">>> start $JAR_NAME successed PID=$! <<<"
   fi
  }

#停止方法
stop(){
  #is_exist
  pidf=$(cat $PID)
  #echo "$pidf"
  echo ">>> api PID = $pidf begin kill $pidf <<<"
  kill $pidf
  rm -rf $PID
  rm -rf logs/run.log
  sleep 2
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> api 2 PID = $pid begin kill -9 $pid  <<<"
    kill -9  $pid
    sleep 2
    echo ">>> $JAR_NAME process stopped <<<"
  else
    echo ">>> ${JAR_NAME} is not running <<<"
  fi
}

#输出运行状态
status(){
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${JAR_NAME} is running PID is ${pid} <<<"
  else
    echo ">>> ${JAR_NAME} is not running <<<"
  fi
}

#重启
restart(){
  stop
  start
}

#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
  "start")
    start
    ;;
  "stop")
    stop
    ;;
  "status")
    status
    ;;
  "restart")
    restart
    ;;
  *)
    usage
    ;;
esac
exit 0
