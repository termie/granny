#!/bin/bash

#for email in `git log --format='%ae' | sort -u`
#do
	#for hash in `git log --author ${email} --format='%H'`
	#do
	#	echo ${hash} ${email}
	#done
#done

echo $GIT_DIR

$prev_score="0"
$score="0"
for hash in `git log --format='%H' | tac`
do
	git checkout ${hash} > /dev/null 2> /dev/null
	email=`git log --format='%ae' -n 1`
	score=`find ./ -name '*.py' | xargs python ../granny/score_file.py | tail -n 1`
	echo ${prev_score} ${score} ${email}
	prev_score=$score
done
