#  Copyright (c) Minecraft internal standard copyright. 2021-2023. All rights reserved.
# -*- coding: utf-8 -*-
"""
    中文(中国大陆简体):大家好，这是一个可以查询当前风靡全球的游戏服务器的状态的程序，它可以让您只需要输入域名或IP地址和端口号即可快速查询。

    中文(繁體):大家好，這是一個可以査詢當前風靡全球的遊戲服務器的狀態的程式，它可以讓您只需要輸入功能變數名稱或IP地址和埠號即可快速查詢。

    中文(粤语):大家好，呢个系一个可以查询当前风靡全球嘅游戏服务器嘅状态嘅程式，可以畀你只需要输入域名或者IP地阯同埠号即可赶查询

    English(US):Hello everyone, this is a program that can check the status of the game servers that are currently
    popular all over the world, and it allows you to quickly query by simply entering the domain name or IP address and
    port number.

    使用方法:
        1).启动程序。
        2).输入IP/域名:端口号(例:abc.com:25565 123.456.78.9:25565)。
        3).数秒后，将会提示结果于下方结果框。

    使用方法：
        1).啟動程式。
        2).輸入IP/功能變數名稱：埠號（例：abc.com:25565 123.456.78.9:25565)。
        3).數秒後，將會提示結果於下方結果框。

    使用方法：
        1).启动程式。
        2).输入IP/域名：埠号（例：abc.com:25565 123.456.78.9:25565)。
        3).数秒之后，将会显示结果于下方结果框。

    Usage:
        1) Start the program.
        2) Enter IP/Domain Name: Port Number (e.g. abc. com: 25565 123.456.78.9:25565).
        3) After a few seconds, the result will be displayed in the result box below.

    感谢您对我们Minecraft-Create工作室的支持！
    感謝您對我們Minecraft-Create工作室的支持！
    感謝您對我們Minecraft-Create工作室的支持
    Thank you for your support of our Minecraft Create studio!

    由于时间原因，我们对以下程序将不再提供多语言注释，仅提供中国大陆 （简体）语言。
    由於時間原因，我們對以下程式將不再提供多語言注釋，僅提供中國大陸（簡體）語言。
    由于时间原因嘅，我哋对以下程式将唔再讲吓嘢喇！多语言注解，仅中国大陆（简体）语言讲吓嘢喇！
    Due to time constraints, we will no longer provide multilingual annotations for the following programs,
    but only provide Chinese Mainland (simplified) languages.
"""
from mcstatus import JavaServer  # 导入mcstatus模块(感谢pymine的技术支持)，用于检测服务器状态
from PyQt5 import QtCore, QtWidgets  # 导入PyQt5模块，用于创建GUI界面
import socket  # 导入socket模块，用于引用socket.gaierror错误捕捉
import sys  # 导入sys模块，用于QT5模块的启动


class Ui_MainWindow(object):
    def __init__(self) -> None:
        """
        初始化定义
        :param:None
        :return:None
        """
        self.statusbar = None  # 全局化定义
        self.menubar = None
        self.textEdit = None
        self.close = None
        self.check = None
        self.eg_ip = None
        self.eg_yuming = None
        self.tip_IP = None
        self.ip_input = None
        self.centralwidget = None
        return

    @staticmethod
    def get_data(host="mc-create.cn", port="25565") -> tuple | str:  # 获取数据信息
        """
        获取Minecraft服务器信息
        :param host:服务器IP或域名
        :param port:服务器端口号
        :return:数据信息或Error
        """
        if int(port) < 0 or int(port) > 65535:  # 如果端口号错误，则返回Error并终止static函数
            return "Error"
        try:  # 尝试连接，如果离线会报Getaddr info错误，即socket.gaierror
            server = JavaServer.lookup(host + ":" + port)  # 进行连接
            status = server.status()  # 获取状态信息
        except socket.gaierror:  # 如果报错，即离线
            return "Error"  # 返回错误并终止static函数
        motd: str = status.motd.raw["text"]  # 获取服务器MOTD信息
        max_player: int = status.players.max  # 获取最高玩家数
        online_player: int = status.players.online  # 获取在线玩家数
        if online_player != 0:  # 如果有在线玩家
            tmp_list = status.players.sample  # 获取玩家列表
            online_player_list = []  # 生成空列表，用于存储
            for tmp in tmp_list:  # 循环遍历
                tmp_str = "玩家名:" + tmp.name + "  UUID:" + tmp.uuid  # 生成单个玩家信息
                online_player_list.append(tmp_str)  # 添加信息
        else:  # 否则
            online_player_list = None  # 设为无玩家在线
        game_version = status.version.name  # 获取游戏服务器版本号
        is_online = True  # 之前获取状态成功才会进入这里↑，所以设置为True
        port = int(port)  # 将端口号Int化
        datas: tuple[str, int, int, list | None, str, str, bool, int] = (  # 遵循PEP8建议，添加类型提示
            motd, max_player, online_player, online_player_list, game_version, host, is_online, port)
        return datas

    def setupUi(self, Object_MainWindow) -> None:  # PyQt5初始化UI界面
        """
        初始化UI
        :param Object_MainWindow:主窗体
        :return: None
        """
        Object_MainWindow.setObjectName("Object_MainWindow")  # 以下均为生成控件，具体信息不再详细描述，请查阅QT官方文档
        Object_MainWindow.resize(800, 600)
        Object_MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        Object_MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(Object_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(380, 80, 113, 20))
        self.ip_input.setObjectName("ip_input")
        self.tip_IP = QtWidgets.QLabel(self.centralwidget)
        self.tip_IP.setGeometry(QtCore.QRect(220, 80, 151, 21))
        self.tip_IP.setObjectName("tip_IP")
        self.eg_yuming = QtWidgets.QLabel(self.centralwidget)
        self.eg_yuming.setGeometry(QtCore.QRect(300, 122, 151, 21))
        self.eg_yuming.setObjectName("eg_yuming")
        self.eg_ip = QtWidgets.QLabel(self.centralwidget)
        self.eg_ip.setGeometry(QtCore.QRect(300, 150, 151, 21))
        self.eg_ip.setObjectName("eg_ip")
        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(520, 80, 75, 23))
        self.check.setObjectName("check")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(520, 150, 75, 23))
        self.close.setObjectName("close")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 240, 701, 321))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        Object_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Object_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Object_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Object_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Object_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Object_MainWindow)
        self.close.clicked.connect(Object_MainWindow.close)  # type: ignore
        # noinspection PyUnresolvedReferences
        self.check.clicked.connect(self.check_ip)
        QtCore.QMetaObject.connectSlotsByName(Object_MainWindow)
        return

    def check_ip(self) -> None:  # 按键调用主函数
        """
        按键按下时调用函数
        :return: UI:显示信息 | None
        """
        ip: str = self.ip_input.text()  # 获取IP或域名
        split: list[str] = ip.split(":")  # 分割域名及端口号
        if len(split) != 2:  # 如果不是两个，即IP和端口号
            self.textEdit.setText("错误:IP或域名格式不正确!")  # 提示格式错误
        else:  # 否则
            datas = self.get_data(host=split[0], port=str(split[1]))  # 获取信息
            msg_1: str = """状态:在线 
IP/域名:%s
端口号:%s
服务器motd:%s
最大玩家数:%s
在线玩家数:%s
玩家列表:%s
游戏版本:%s
"""  # 定义模板（在线）
            msg_2: str = """状态:离线
IP/域名:%s
端口号:%s
"""  # 定义模板（离线）
            if datas == "Error":  # 如果离线
                self.textEdit.setText(msg_2 % (self.ip_input.text().split(":")[0], self.ip_input.text().split(":")[1]))  # 用2号模板，插入IP/域名和端口号
            else:  # 否则
                player_list = datas[3]  # 获取玩家列表
                self.textEdit.setText(  # 使用1号模板，插入各种状态信息
                    msg_1 % (datas[5], datas[-1], datas[0], datas[1], datas[2], player_list, datas[4]))
        return

    def retranslateUi(self, Object_MainWindow) -> None:
        """
        :param Object_MainWindow: 主窗体
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate  # PyQt5模块设置文字，不再叙述
        Object_MainWindow.setWindowTitle("Minecraft Server Status")  # 设置标题
        self.tip_IP.setText(_translate("Object_MainWindow", "IP/域名(IP/域名:端口号)："))
        self.eg_yuming.setText(_translate("Object_MainWindow", "示例:mc-create.cn:25565"))
        self.eg_ip.setText(_translate("Object_MainWindow", "示例:123.456.78.9:25565"))
        self.check.setText(_translate("Object_MainWindow", "检测"))
        self.close.setText(_translate("Object_MainWindow", "关闭"))
        return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    MainWindow = QtWidgets.QMainWindow()  # 实例化QtWidgets中的QMainWindow
    ui = Ui_MainWindow()  # 实例化UI
    ui.setupUi(MainWindow)  # 初始化UI
    MainWindow.show()  # 展示UI
    sys.exit(app.exec_())  # 安全退出程序
