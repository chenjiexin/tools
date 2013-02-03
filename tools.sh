#!/bin/bash

cur_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

dir=$1
if [ -z $dir ]; then
	dir=$cur_dir
	echo -e '\033[45;31;1mNo directory specified, try working in current directory\033[0m'
fi

cd $dir
# 取得真正目录名，而不是'.'之类
dir=`pwd`
dir_name=$(basename $dir)

echo '==============================================='
echo -e '================ \033[0;31;1mWORKING IN\033[0m ==================='
echo -e '\033[0;34;1m'$dir'\033[0m'
echo '==============================================='

files=`ls *.str`

for file in $files; do
	$cur_dir/tools.py $file $dir_name

done


echo '==============================================='
echo -e '================ \033[0;32;1mJOB DONE\033[0m ====================='
echo '==============================================='
echo ''
