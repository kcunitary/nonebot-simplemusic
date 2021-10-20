# _*_ coding:utf-8 _*_
from setuptools import setup, find_packages

with open("README.md", "r",encoding='UTF-8') as fh:
    long_description = fh.read()

setup(name='nonebot_plugin_simplemusic',
      version='0.2',   
      description='最简点歌插件，支持网易云、QQ音乐',
      long_description=long_description,
      long_description_content_type="text/markdown",  
      author='鹿乃ちゃんの猫',  
      author_email='kano@hanayori.top',  
      url='https://github.com/kanomahoro/nonebot-simplemusic', 
      packages=find_packages(),  
      license="GPLv3",   
      classifiers=[
          "Programming Language :: Python :: 3", 
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent"],
      python_requires='>=3.8',
      install_requires=[
        "nb-cli>=0.5.0",
        "nonebot-adapter-cqhttp>=2.0.0a15"
    ]
      )