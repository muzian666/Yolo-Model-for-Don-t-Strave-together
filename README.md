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
 - [ ] 1.在Windows10下，使用环境为Python3.10.0时，点击Creat ReatBox后工具直接闪退。
 - [x] 2.在Windows & Macos下，更改项目格式(例如：PasalVOC转为Yolo)，按下保存后，工具闪退。


### 已知问题的解决方法
1. (暂无解决方法，可能需要更换Python环境)
2. 解决方法：先选定Save File Dir（文件储存位置&文件打开位置），再转换格式


## 2.使用标记工具

   出现标记工具后，先选定读取文件夹与储存文件夹。可以尝试将格式从PasalVOC转为Yolo，并点击保存，如果程序未意外退出，即可进行标记工作。
   如果标记工具意外退出，参考上述已知存在问题，若有更多问题，欢迎留下评论。
   
   在图片出现后，点击Creat ReatBox（创建区块），对需要标记的对象选框，并对标签进行命名。
   
   点击保存。
   
## 3.标记工具命名规则文件
   链接地址：https://hksyu3-my.sharepoint.com/:x:/g/personal/199010_hksyu_edu_hk/EUxivwAmQ9tImAHFdUAHoKcBkOGMwzNblh-g61EqVktVmg?e=lFS2XL 中国大陆境内可直接访问（实时更新）
    
# 内容更新记录
  1.2021/12/08 更新了附带名称的图鉴目录
  2.更新了一个命名规则的文档

# Reference
  (没啥格式，就有啥标啥）
  1. 《饥荒联机版》图鉴：https://www.gamersky.com/handbook/201702/866370.shtml

# 未完待续
