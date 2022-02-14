import streamlit as st
import pandas as pd
import numpy as np

# 模块零：标题与表头
st.write("""
# DNA数据存储编码系统原型
密码子（杭州）科技有限公司，最后更新: 2022 Feb 14
""")

def get_oringinal_binary_data(file):
    i = 0
    bit = file.read(1)
    data = []
    while bit:
        byte = ord(bit)
        data.append(format(int(str(byte),10), 'b').zfill(8))
        i += 1
        bit = file.read(1)
    file.close()
    data = "".join(data)
    return data

# 模块一：文件读取
st.title("File Uploader")
st.sidebar.write('文件读取')
file = st.sidebar.file_uploader('请选取要编码的文件：', key=None)
# @st.cache
if file is not None:
   st.write("选取的文件: ", file.name)
   data = get_oringinal_binary_data(file)
   st.write(data)