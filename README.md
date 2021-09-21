<!-- markdownlint-disable MD033 MD041-->
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/kanomahoro/images@main/logo.png" width="200" height="200"/>
</p>

<div align="center">

# SimpleMusic
<!-- markdownlint-disable-next-line MD036 -->
_✨ 基于NoneBot2的最简点歌插件，支持网易云、QQ音乐 ✨_

</div>

## 简介

本插件基于[NoneBot2](https://github.com/nonebot/nonebot2)与[go-cqhttp](https://github.com/Mrs4s/go-cqhttp),可以实现最简的Q群点歌功能，支持网易云、QQ音乐

## 即刻开始

### 安装NoneBot2
完整文档可以在 [这里](https://v2.nonebot.dev/) 查看。

懒得看文档？下面是快速安装指南：

1. (可选)使用你喜欢的 Python 环境管理工具创建新的虚拟环境。
2. 使用 `pip` (或其他) 安装 NoneBot 脚手架。

   ```bash
   pip install nb-cli
   ```

3. 使用脚手架创建项目

   ```bash
   nb create
   ```
4. 请在创建项目时选用cqhttp适配器，并且按照文档完成最小实例的创建
   
### 配置文件示例
1. .env
   ```yml
   ENVIRONMENT=prod
   ```
2. .env.prod
   ```yml
   HOST=127.0.0.1
   PORT=8080
   SECRET=
   ACCESS_TOKEN=
   SUPERUSERS=[超级用户账户(你的QQ号,不是机器人的账户)]
   COMMAND_START=["","/"]
   NICKNAME=["","/"]
   COMMAND_SEP=["."]
   ```
3. 请务必安装以上示例配置你的Bot；go-cqhttp请自行参照官方文档配置

### 安装SimpleMusic
   1. pip安装
   ```bash
   pip install nonebot-plugin-simplemusic
   ```
   请在你的bot.py文件中加入以下内容
   ```python
   nonebot.load_plugin("nonebot_plugin_simplemusic")#添加此行
   nonebot.load_from_toml("pyproject.toml")#位于本行前
   ```
   2. 使用nb-cli安装(推荐)
  
   在你的Bot目录下执行：
   ```bash
   nb plugin install nonebot_plugin_simplemusic
   ```

### 指令说明
以下所有指令只在群聊中生效，使用时不需要@机器人，直接发送指令
**所有指令如下：**
1. **点歌 歌曲名**
   在QQ音乐中搜索指定歌曲，如果没有找到则不会有任何响应
2. **点歌 歌曲名 歌手名**
   在QQ音乐中搜索指定歌曲，并试图匹配指定歌手，如果没有找到则不会有任何响应
3. **网易点歌 歌曲名**
   在网易云音乐中搜索指定歌曲，如果没有找到则不会有任何响应
4. **网易点歌 歌曲名 歌手名**
   在网易云音乐中搜索指定歌曲，并试图匹配指定歌手，如果没有找到则不会有任何响应

### 遇到问题？
你可以直接提交issue，或者发送邮件到：kano@hanayori.top

### 效果展示

![效果1](https://cdn.jsdelivr.net/gh/kanomahoro/images@main/xiaoguo3.jpg)

![效果2](https://cdn.jsdelivr.net/gh/kanomahoro/images@main/xiaoguo4.jpg)
