# Yolo-Model-for-Don-t-Strave-together
  中文名：训练一个《饥荒联机版》的Yolo模型

## 1.安装标记工具 (Windows 与 Mac 通用)
  打开 cmd(win) / 终端(mac)
  
  输入:
  ```
  pip3 install pyqt5 --user  #安装pyqt5基本环境
  
  pip3 install labelimg  #安装labelimg程序
  
  labelimg  #启动labelimg程序
  ```
  稍等片刻，即出现标记工具窗口。
  
### 目前已知存在问题
 - [ ] ❌ 1.在Windows10下，使用环境为Python3.10.0时，点击Creat ReatBox后工具直接闪退。
 - [x] ✅ 2.在Windows & Macos下，更改项目格式(例如：PasalVOC转为Yolo)，按下保存后，工具闪退。


#### 已知问题的解决方法
❌ 1. (暂无解决方法)
✅ 2. 解决方法：先选定Save File Dir，再转换格式
