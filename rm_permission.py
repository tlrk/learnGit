#!/usr/bin/env python
#coding:utf-8
#author:huyinbo

import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import sys

def formatXml(root):
    ET._namespace_map['http://schemas.android.com/apk/res/android']='android'
    rough_string=ET.tostring(root,'utf-8')
    reparsed=minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=' ',encoding='utf-8')

def remove_permission(src, dst):
    tree = ET.ElementTree()
    tree.parse(src)
    root = tree.getroot()
    permissions = root.findall('uses-permission')
    for node in permissions:
        nodeStr = ET.tostring(node)
        #print nodeStr
        if (shouldDelete(nodeStr, permissionToDelete)):
            root.remove(node)
    content = formatXml(root)
    saveXml(content, dst)

def shouldDelete(nodeStr, array):
    for item in array:
        if (nodeStr.find(item) != -1):
            #print nodeStr
            return True
    return False

def saveXml(content,xmlpath):
    f=open(xmlpath,"w")
    content2=""
    for i in content.split("\n"):
        if i.strip() != '':
            content2+=i
            content2+="\n"
    f.write(content2)
    f.close()

permissionToDelete = ['UNINSTALL_SHORTCUT', 'READ_EXTERNAL_STORAGE', 'RECEIVE_SMS', 
                        'SEND_SMS', 'CHANGE_CONFIGURATION', 'CALL_PHONE', 'READ_SMS', 
                        'RECORD_AUDIO', 'DISABLE_KEYGUARD','READ_SETTINGS']

argv = sys.argv
if (len(argv) == 3):
    src = argv[1]
    dst = argv[2]
    remove_permission(src, dst)
else:
    print 'argument list does not match'


