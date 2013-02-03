#!/usr/bin/python
# -*- coding:utf-8 -*-

import re
from sys import argv
import sys
import os
import codecs

if len(argv) < 3:
    print "Usage: \n" + argv[0] + " [file] [dir name]"
    exit(1)

print "\033[0;32;1mhandling: " + argv[1] + '\033[0m'
try:
    fileInput = codecs.open(argv[1], 'r', encoding='utf-16-le')
except:
    exit(1)


file_name = os.path.splitext(os.path.basename(argv[1]))[0]
new_file = file_name + ".utf8"

fileOut = codecs.open(new_file, 'w', encoding='utf-8')

# 统计字串行数
count=0

# 第一行字串的定义
style=''

new_file_content = ''

var_name='lpsz_' + argv[2] + '_' +  file_name + '_utf8'

fileOut.write(u'\ufeff')
fileOut.write(u'/*--------------------------------------------------------------\n')
fileOut.write(u'//\t文件名： ' + new_file + '\n')
fileOut.write(u'//\t最后修改时间：\n')
fileOut.write(u'//\n')
fileOut.write(u'//\t此文件属自动生成，请勿手工修改\n')
fileOut.write(u'//-------------------------------------------------------------*/\n\n')

#fileOut.writelines('static LPCSTR ' + var_name + '[] =\n{\n')
new_file_content += 'static LPCSTR ' + var_name + '[] =\n{\n'

# 当前处理的那行字符串
val=''
# 是否多行字串
next_line=False
for line in fileInput.readlines():

	if re.search(r"/*---", line) :
		continue
	if re.match(r"^//", line) :
		continue
	if not next_line and re.match(r"^\s*$", line):
		continue

	line = line.strip()
	parts = re.split(r',', line)
	if not parts and not next_line:
		continue

	# 字串包含有','
	p_len = len(parts)
	if p_len > 2:
		for i in range(2, p_len):
			parts[1] += ','
			parts[1] += parts[i]

	if count == 0:
		style = parts[0]

	if next_line :
		tmp = line
	else :
		tmp = parts[1].strip()

	has_quota = False
	
	# 正则表达式的
	if len(tmp) > 0:
		tmp = re.sub(r'(?<!\\)\\(?!(r|n|t|\\|a|b|f|v|0|\d))', r'\\\\', tmp)
	# 去掉首个"
	if len(tmp) > 0 and tmp[0] == r'"' :
		tmp = tmp[1:]
	# 最后一个
	# 要多处理字符串只有""的情况
	if (len(tmp) > 1 and tmp[-1] == r'"') or (len(tmp) == 1 and tmp[0] == r'"') :
		has_quota = True
		tmp = tmp[:-1]

	# 防止只有引号的情况
	if len(tmp) > len(r'""') :
		tmp = tmp.replace(r'""', r'\"')

	if not has_quota:
		next_line = True
		tmp += r'\n'
		val += tmp
		continue
	else :
		# 追加到上一行
		if next_line :
			val += tmp
		else :
			val = tmp
		next_line = False
		count+=1

	#fileOut.writelines('\t' + r'"' +  val + '\",\n')
	new_file_content += '\t' + r'"' +  val + '\",\n'
	val = ''
# end of for

# 防止漏掉一行
if len(val) > 0:
	if val[-1] != r'"':
		val += r'"'
#	fileOut.writelines(val + '\n')
	new_file_content += val + '\n'

if new_file_content[-2] == r',':
	new_file_content = new_file_content[:-2]
	new_file_content += '\n'
#fileOut.writelines('};\n\n')
new_file_content += '};\n\n'

section_name = 'section_' + argv[2] + '_' + file_name + '_utf8'

# fileOut.writelines('ResourceStringSection ' + section_name + ' = {' +str( count) + ', ' + var_name + '};\n')
# fileOut.writelines('strings.insert(std::make_pair(' + style + ', ' + section_name + '));')
new_file_content += 'ResourceStringSection ' + section_name + ' = {' +str(count) + ', ' + var_name + '};\n'
new_file_content += 'strings.insert(std::make_pair(' + style + ', ' + section_name + '));'

if count > 0:
	fileOut.write(new_file_content)

fileInput.close()
fileOut.close()
