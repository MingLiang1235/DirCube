#coding:utf-8

from distutils.core import setup

import py2exe
import sys


#includes = ["encodings", "encodings.*"]    
#要包含的其它库文件

options = {"py2exe":

    {"compressed": 1, #压缩
     "optimize": 2,
     "ascii": 0,
     "dll_excludes": [ "mswsock.dll", "powrprof.dll" ],  #解决用py2exe打包运行后老是出现如下错误提示：“ImportError: MemoryLoadLibrary failed loading win32api.pyd”
     "bundle_files": 3 #所有文件打包成一个exe文件 
    }
	}
setup(     
    options = options,      
    zipfile=None,   #不生成library.zip文件
    windows=[{"script": "Aggre_11_9.py"}]#源文件，程序图标
    )
