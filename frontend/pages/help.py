import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QGridLayout

from frontend.generic import Font, TextLabel, HyperlinkTextLabel, Icons, ScrollBar, ScrollArea, ScrollAreaContent
from frontend.layouts import RowLayout

class HelpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("helpPage")

        self.layout = QGridLayout(self)
        self.layout.setObjectName("helpPageLayout")
        self.layout.setContentsMargins(25, 25, 25, 25)
        self.layout.setSpacing(0)

        self.scrollBar = ScrollBar(self, "helpPage")
        self.scrollArea = ScrollArea(self, "helpPage", self.scrollBar)
        self.scrollAreaContent = ScrollAreaContent(self.scrollArea, "helpPage")
        self.scrollArea.setWidget(self.scrollAreaContent)
        self.scrollAreaContentLayout = QVBoxLayout(self.scrollAreaContent)
        self.scrollAreaContentLayout.setObjectName("helpPageScrollAreaContentLayout")
        self.scrollAreaContentLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaContentLayout.setSpacing(15)

        # TODO maybe split into different subsections with headings
        s = "&nbsp;" # html space
        d = ("<p style=line-height:140%>"
             "如果你使用了自定义图标包，请前往“设置”页面，浏览并选择你的《黎明杀机》图标文件夹路径（使用原版图标留空即可）。<br>"
             "在“偏好配置”页面中，你可以为血网中的附加品、道具、祭品和技能设置优先级。"
             "每套偏好设置都可以保存为独立配置方案，方便按需切换。"
             "程序内置了两套预设方案：节俭流（以尽可能节省血点的方式升级血网）与 "
             "Otz 推荐强度表（基于 Otzdarva 的强度评级并略作微调）。"
             "两套预设均提供“优先技能”与“忽略技能”两种版本。你可以以内置预设为基础修改，也可以从零新建自己的方案。<br>"
             "每个解锁项都可以配置“层级（Tier）”和“子层级（Subtier）”：<br>"
             f"{s*8}- 层级（或子层级）越高，程序越优先购买该物品<br>"
             f"{s*8}- 层级（或子层级）越低，程序越倾向避开该物品<br>"
             f"{s*8}- 对于持有中立态度（既不刻意追求也不排斥）的物品，无需配置（默认层级和子层级均为 0）<br>"
             f"{s*16}- 未在配置中出现的物品默认视为中立（层级 0，子层级 0）<br>"
             f"{s*8}- 层级和子层级的有效范围为 -999 到 999<br>"
             f"{s*8}- 层级为 (A + B) 的单个物品，其优先级等价于 1 个层级为 A 与 1 个层级为 B 的物品之和<br>"
             f"{s*16}- 例如：1 个层级 2 的物品等价于 2 个层级 1 的物品<br>"
             f"{s*16}- 你可以借此精细调整对不同物品的偏好权重<br>"
             f"{s*8}- 负数层级同理，用于指定你排斥或尽量避免购买的物品的权重<br>"
             f"{s*8}- 子层级用于区分同一层级内的先后顺序，例如：层级 3 子层级 3 的优先级高于层级 3 子层级 2<br>"
             "不同配置方案可保存不同的偏好列表，随时一键切换；你也可以将方案导入或导出为 .emp 文件与他人分享。<br><br>"
             "在“运行”页面中，只需选择偏好配置方案、要升级的角色、选择模式、运行速度以及可选上限，即可开始运行！<br>"
             "运行前请务必关闭任何游戏滤镜、画质补丁或色盲模式，并确保游戏画面在主显示器上完全可见且无遮挡，否则程序可能无法准确识别血网节点。</p>")
        self.instructionsLabel = TextLabel(self, "helpPageInstructionsLabel", "使用说明（Blood Emporium 汉化版）", Font(12))
        self.instructionsDescription = TextLabel(self, "helpPageInstructionsDescription", d, Font(10))
        self.instructionsDescription.setWordWrap(True)

        self.contactLabel = TextLabel(self, "helpPageContactLabel", "原作者与社区链接", Font(12))

        self.contactDiscordRow = QWidget(self)
        self.contactDiscordRow.setObjectName("helpPageContactDiscordRow")
        self.contactDiscordRowLayout = RowLayout(self.contactDiscordRow, "helpPageContactDiscordRowLayout")

        self.contactDiscordIcon = QLabel(self.contactDiscordRow)
        self.contactDiscordIcon.setObjectName("helpPageContactDiscordIcon")
        self.contactDiscordIcon.setFixedSize(QSize(20, 20))
        self.contactDiscordIcon.setPixmap(QPixmap(os.getcwd() + "/" + Icons.discord))
        self.contactDiscordIcon.setScaledContents(True)
        self.contactDiscordLabel = HyperlinkTextLabel(self.contactDiscordRow, "helpPageContactDiscordLabel",
                                                      "官方 Discord 社区", "https://discord.gg/J4KCqJJuaM", Font(10))

        self.contactTwitterRow = QWidget(self)
        self.contactTwitterRow.setObjectName("helpPageContactTwitterRow")
        self.contactTwitterRowLayout = RowLayout(self.contactTwitterRow, "helpPageContactTwitterRowLayout")

        self.contactTwitterIcon = QLabel(self.contactTwitterRow)
        self.contactTwitterIcon.setObjectName("helpPageContactTwitterIcon")
        self.contactTwitterIcon.setFixedSize(QSize(20, 20))
        self.contactTwitterIcon.setPixmap(QPixmap(os.getcwd() + "/" + Icons.twitter))
        self.contactTwitterIcon.setScaledContents(True)
        self.contactTwitterLabel = HyperlinkTextLabel(self.contactTwitterRow, "helpPageContactTwitterLabel", "作者 Twitter / X",
                                                      "https://twitter.com/initiationmusic", Font(10))

        self.contactDiscordRowLayout.addWidget(self.contactDiscordIcon)
        self.contactDiscordRowLayout.addWidget(self.contactDiscordLabel)
        self.contactDiscordRowLayout.addStretch(1)

        self.contactTwitterRowLayout.addWidget(self.contactTwitterIcon)
        self.contactTwitterRowLayout.addWidget(self.contactTwitterLabel)
        self.contactTwitterRowLayout.addStretch(1)

        self.scrollAreaContentLayout.addWidget(self.instructionsLabel)
        self.scrollAreaContentLayout.addWidget(self.instructionsDescription)
        self.scrollAreaContentLayout.addWidget(self.contactLabel)
        self.scrollAreaContentLayout.addWidget(self.contactDiscordRow)
        self.scrollAreaContentLayout.addWidget(self.contactTwitterRow)
        self.scrollAreaContentLayout.addStretch(1)

        self.layout.addWidget(self.scrollArea)
        self.layout.setRowStretch(0, 1)
        self.layout.setColumnStretch(0, 1)