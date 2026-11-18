[![Blood Emporium](assets/images/splash.png)](https://github.com/IIInitiationnn/BloodEmporium/releases/latest)

[![Upstream](https://img.shields.io/badge/上游原版-IIInitiationnn%2FBloodEmporium-purple)](https://github.com/IIInitiationnn/BloodEmporium)
[![Base Version](https://img.shields.io/badge/基于版本-v1.2.22-blue)](https://github.com/IIInitiationnn/BloodEmporium/releases/tag/v1.2.22)
[![Discord](https://img.shields.io/discord/1016471051187802333?logo=discord&label=discord)](https://discord.gg/J4KCqJJuaM)

> **简体中文汉化分支**：本项目为 [IIInitiationnn/BloodEmporium](https://github.com/IIInitiationnn/BloodEmporium)（`v1.2.22`）的简体中文汉化版本，用于《黎明杀机》（Dead by Daylight）自动点血网辅助。  
> 原作版权及代码归原作者 **IIInitiationnn** 所有；本分支仅包含界面及游戏内词条汉化、UTF-8 编码兼容适配与启动自动更新禁用（防止覆盖为英文上游版本）。

---

## 汉化说明

- **数据库与词条中文化**（`assets/data.db`）：
  - 完成全部 **1,478** 项解锁物（技能、道具、附加品、祭品、神秘礼盒）与 **44** 名杀手称号/姓名汉化，参考《黎明杀机》简体中文翻译标准；
  - 数据库保留 `name_en` / `alias_en` 字段，**支持在「偏好配置」页同时使用中文或英文名称搜索**，鼠标悬停物品图标时会提示英文原名。
- **内置预设汉化**（`assets/presets/`）：
  - `[内置] 节俭流（忽略技能）.emp`
  - `[内置] 节俭流（优先技能）.emp`
  - `[内置] Otz推荐强度表（忽略技能）.emp`
  - `[内置] Otz推荐强度表（优先技能）.emp`
- **客户端界面与兼容修复**：
  - 完整汉化主界面、运行页、偏好配置页、设置页、帮助页及弹窗提示，字体调整为 `Microsoft YaHei UI`；
  - 统一 `config.json`、`runtime.json`、`.emp` 方案与 `.csv` 购买统计导出为 UTF-8 编码；
  - 下拉框内部保留原始英文 ID（如角色、`press`/`hold`、`left`/`right`），与原有配置文件兼容；
  - 默认禁用启动时的上游自动更新检查，以免覆盖本汉化版。

---

<details>
<summary>原版英文说明与功能介绍（点击展开 / 翻译对照）</summary>

## 开发者说明（上游）
图标识别资源更新至《黎明杀机》**Patch 10.1.0**（第 41 章：Chorus of Sin）。  
如对上游原项目有建议或需提交基础功能缺陷，可前往原作者的 [Discord](https://discord.gg/J4KCqJJuaM) 或 [上游 Issues](https://github.com/IIInitiationnn/BloodEmporium/issues)。

## 项目简介
自动根据用户设置的偏好权重在《黎明杀机》血网中选择最优购买路线的桌面工具。
- 基于权重与路径代价算法计算“收益最大、讨厌项最少”的购买顺序；
- 通过游戏图标与屏幕识别定位血网节点；
- 全程在游戏对局外运作，不读写游戏内存、不注入游戏进程。

## 安装与使用（汉化版）
1. **成品用户**：前往本仓库 **Releases** 页面下载中文免安装压缩包，解压后直接双击运行 `Blood Emporium.exe`。
2. **源码运行（Python 3.8）**：安装 `requirements.txt` 中的依赖后执行 `python main.py`。
3. 如使用自定义图标包，请在「设置」页指定游戏图标目录（原版图标保持留空即可）。
4. 运行前务必关闭显卡滤镜、Reshade、游戏内色盲模式等会改变画面颜色的设置，并保证游戏窗口位于主显示器且无遮挡。

## 核心特性
- 自定义各类附加品、道具、祭品、技能的层级（Tier）与子层级（Subtier），范围 `-999` ~ `999`；
- 两种选择模式：**单点模式** 与 **多点路径模式**；
- 两种运行速度：**慢速（精准）** 与 **快速**；
- 支持设置自动购买中心按钮阈值、转生次数上限、血点消耗上限；
- 默认热键 `Ctrl + Alt + 9` 快速启动/停止（可在设置页自定义）。

## 常见问题
- **杀毒软件/Windows Defender 误报**：PyInstaller 打包的 Python 程序常出现误报，属常见现象，添加信任/排除即可。上游已说明相关讨论：
  - https://github.com/pyinstaller/pyinstaller/issues/6754
  - https://www.reddit.com/r/learnpython/comments/ng3hmp/pyinstaller_create_onefile_exe_windows/
  - https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg

## 致谢
- 原项目作者：[IIInitiationnn](https://github.com/IIInitiationnn/BloodEmporium)
- 图标素材来源：[The Noun Project](https://thenounproject.com/)
- GUI 样式灵感：[Wanderson](https://www.youtube.com/WandersonIsMe)
- 上游社区贡献者：digitalyeti、dazvise (Discord)

</details>