#!/bin/bash

cur_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

dirs=`ls $cur_dir | grep ^[0-9]*$`

for dir in $dirs; do
	working_dirs=`ls $cur_dir/$dir/strings/`

	for wd in $working_dirs; do
		if [ -d "$cur_dir/$dir/strings/$wd" ]; then
			$cur_dir/tools.sh $cur_dir/$dir/strings/$wd
		fi
	done
done
