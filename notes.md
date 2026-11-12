# 我的 Python 学习日志（第一周）

## 日期：2026-10-26（第一天：环境与基础）
- **今天学了**：安装 Python/pip、终端基本操作、运行 python3 脚本。
- **常用命令**：
  - `pwd` / `ls` / `cd` / `mkdir` / `rm`
  - `nano 文件名`（编辑，Ctrl+O 保存，Ctrl+X 退出）
  - `cat 文件名`（查看内容）
  - `python3 文件名.py`（运行脚本）
  - `python3`（进入交互模式，`exit()` 退出）
  - `Ctrl+C` 终止程序，`Tab` 自动补全，上下键翻历史命令。
- **写出的文件**：`hello.py`, `about_me.py`
- **遇到的报错**：`SyntaxError: '(' was never closed`
- **怎么解决的**：补上右括号。

---

## 日期：2026-10-27（第二天：控制流）
- **今天学了**：变量、`input`输入、`float`转换、`if/else`条件判断、`f-string`格式化输出（特别是用 `:.2f` 保留两位小数）、`\n` 换行；`while` 循环、`for` 循环、`range()` 函数、`break` 语句。
- **写出的文件**：`calculator.py`, `day2_2challenge.py`（温度转换、圆面积、超市结账）, `day2_3loop.py`（输入0退出、打印1-10、判断成绩及格/挂科）。
- **遇到的报错/踩坑**：
  1. 在终端输入 `10 2` 报 `command not found`。-> 明白了运行脚本时，要在程序提示后输入，而不是在 bash 终端直接敲。
  2. 华氏度输出无限长的小数。-> 用 `:.2f` 格式化。
  3. `NameError: name 'total' is not defined`。-> 发现 else 分支里错拼成了 `tatol=t`，改成 `total` 修复。
  4. `while` 循环里 `input()` 拿到的是字符串，输入 0 无法退出。-> 用 `int(input())` 转换成整数。

---

## 日期：2026-10-28（第三天：函数）
- **今天学了**：如何用 `def` 定义函数、传入参数、使用 `return` 返回结果。
- **写出的文件**：`day3_1fanction.py`（包含 greet 打招呼、超市算价、Collatz 序列）。
- **遇到的报错/踩坑**：
  1. 写 Collatz 序列时，函数里用了全局变量 `i`，如果输入 1，程序直接崩溃。-> 函数内部尽量不要依赖全局变量，把循环写在主程序或函数内部。
  2. 函数里 `return` 后面的代码不会执行，不能把 `return` 当 `print` 用。

---

## 日期：2026-10-29（第四天：列表）
- **今天学了**：列表的创建、索引、`append()` 追加、`len()` 获取长度、`sort()` 排序；用 `for` 循环遍历列表；手写逻辑寻找列表最大值。
- **写出的文件**：`day4_list.py`（找最大值）, `day4_2lsit.py`（生成10个随机数并排序）。
- **遇到的报错/思考**：
  1. 找最大值时，一开始用了 `append(0)` 占位再覆盖，后来发现直接 `s.append(int(number))` 更简洁。
  2. 知道了 `max_s` 初始值如果设为 0，遇到全是负数的列表就会出错，应该设为 `max_s = s[0]`。
  3. 用 `import random` 和 `random.randint(1, 100)` 生成随机数。

---

## 日期：2026-10-30（第五天：字典与字符串）
- **今天学了**：
  1. **字典**：创建、键值对、`[]` 和 `get()` 的区别、`items()` 遍历、动态添加修改。
  2. **字符串**：`split()` 按空格切分列表，`join()` 把列表重新拼成字符串。
- **写出的文件**：`day5_dict.py`（通讯录查询与添加）, `day5_2dict.py`（游戏物品清单统计 + split/join 文本处理）。
- **遇到的报错/思考**：
  1. 用了 `__name__` 当作变量名，知道了这是 Python 的魔法变量，不能乱用。
  2. 理解了 `phone_book.get('名字', '查无此人')` 和 `phone_book['名字']` 的区别（后者会报错崩溃）。
  3. 遍历字典 `for k, v in spam.items():` 时，`v` 已经是值了，不需要再写 `spam[k]`。

---

## 日期：2026-10-31（第六天：正则表达式基础）
- **今天学了**：`import re`、`re.compile()` 编译模式、`search()` 查找第一个、`group()` 和 `groups()` 提取内容、括号 `()` 分组、`\d` `\w` `\s` 基本规则。
- **写出的文件**：`day6_1regex.py`（电话号码匹配与分组）。
- **遇到的报错/思考**：
  1. `AttributeError: 'NoneType' object has no attribute 'group'`。-> 正则没匹配上返回了 None。仔细检查发现正则里多了一个空格，或者把 `\d` 写成了字母 `d`。
  2. `ValueError: too many values to unpack`。-> 正则里有几个括号，`groups()` 就返回几个元素，左边就要用几个变量去接。

---

## 日期：2026-11-02（第七天：正则表达式实战）
- **今天学了**：
  1. `findall()` 找所有；`re.VERBOSE` 多行注释正则。
  2. 发现神奇规律：`findall()` 遇到有括号的正则返回元组列表；没括号返回字符串列表。
  3. 用正则写了“强口令检测”和“邮箱+电话提取”。
- **写出的文件**：`day6_2regex.py`（邮箱提取与电话提取）, `day7_projects.py`（强口令检测）。
- **遇到的报错/踩坑**：
  1. **电话号码提取被截断**（比如 `138-1234-5678` 只提取到了 `138-1234`）。-> 明白了正则的“回溯”机制，把 `\d{3}` 改成了 `\d{3,4}` 解决。
  2. 用 `"-".join(...)` 强行拼接电话时，容易出现多余符号或 `None` 导致报错。-> 学会了直接用 `phone_tuple[0].replace(' ', '-')` 保留原格式并清洗。
  3. 强口令检测中，理解了用多个独立的 `search()` 来判断字符串是否包含大写、小写和数字。

---

## 日期：2026-11-03（第八天：读写文件）
- **今天学了**：
  1. `os.path` 模块：路径拼接、获取当前目录、查看文件是否存在、创建多级文件夹。
  2. 文件读写：`open()` 函数、`'r'`（读）、`'w'`（覆盖写）、`'a'`（追加写）三种模式。
  3. 读文件的区别：`read()` 读全部，`readlines()` 读成列表。
  4. `with open(...) as f:` 上下文管理器，自动关闭文件。
  5. `shelve` 模块：像字典一样把复杂的变量存进硬盘（存档功能）。
- **写出的文件**：`day8_1text.py`（文件路径与读写测试）, `day8_3_shelve.py`（shelve 存档测试）, `day8_4_diary.py`（命令行日记本项目）。
- **遇到的报错与思考**：
  1. `AttributeError: 'TextIOWrapper' object has no attribute 'open'`。-> 混淆了文件对象和 open 函数。重新打开文件直接用 `open('文件名', 'r')`。
  2. `io.UnsupportedOperation: not readable`。-> 用 `'w'` 模式打开的文件只能写不能读，读完必须重新用 `'r'` 模式打开。
  3. 日记本项目的边缘情况：如果文件不存在直接读取会报 `FileNotFoundError`，学会了用 `os.path.exists` 先判断。

---

## 📌 明日计划（第九天）
- 学习第 9 章（组织文件）。
- 重点掌握 `shutil` 模块（`copy`、`move`、`rmtree` 等）进行文件的复制、移动和重命名。
- 学习 `os.walk()` 遍历目录树，批量处理文件夹。

## 日期：2026-11-04（第九天：组织文件与网络初探）
- **今天学了**：
  1. `shutil` 模块：`copy()` 复制文件、`move()` 移动/重命名文件。
  2. `os` 模块进阶：`os.path.exists()` 检查路径是否存在、`os.remove()` 删除文件。
  3. `os.walk()` 遍历目录树：可以无限往下钻，找到所有子文件夹里的文件（返回 root, dirs, files）。
  4. `zipfile` 模块：`zipfile.ZipFile('xxx.zip', 'w')` 创建压缩包，并用 `write()` 把文件打包进去。
  5. `requests` 模块初探：`requests.get()` 发送网络请求，获取网页或 API 数据。
- **写出的文件**：`day9_1_files.py`（批量备份脚本）, `day9_2_walk.py`（目录树打印）, `day9_3_zip.py`（打包备份）。
- **遇到的报错/思考**：
  1. 发现 `shutil.copy(文件, '目标文件夹')` 可以直接保留原文件名复制，非常方便。
  2. 用 `os.listdir()` 会把文件夹也列出来，需要加 `os.path.isdir()` 过滤，但 `os.walk()` 会自动把文件夹和文件分开，更省事。
  3. 打包压缩包时，`zipf.write(路径, arcname=文件名)` 可以避免解压后嵌套太深的文件夹。
- **明天计划**：
  1. 继续第 11 章，学习 `requests` 发送和接收数据。
  2. 学习第 14 章，用 `json` 模块解析网络返回的数据（大模型 API 的核心基础）。

## 日期：2026-11-05（第十一天：网络抓取，环境配置与 Excel 初探）
- **今天学了**：
  1. 成功编写了支持自动翻页的完整爬虫，并将 100 句名言保存到文件。
  2. 掌握了如何处理 pip 安装第三方库时的系统级依赖冲突（安装了 libxml2-dev 和 libxslt1-dev），成功安装了 openpyxl、PyPDF2、python-docx。
- **写出的文件**：`day10_4_quotes.py`（完整翻页爬虫）, `quotes.txt`。
- **遇到的报错/踩坑**：
  1. pip 安装 python-docx 时遇到 `ResolutionImpossible`，原因是 Python 3.14 版本太新，lxml 没有预编译包。通过 `sudo apt install libxml2-dev libxslt1-dev python3-dev` 安装系统底层依赖解决。
- **明天计划**：
  1. 彻底拿下第 12 章 Excel 数据的读取、遍历、修改与写入。
  2. 拿下第 13 章 PDF 和 Word 的文本提取，为以后做 AI 文档问答（RAG）打基础。

  ## 日期：2026-11-06（第十二天：Excel、PDF、Word 数据处理）
- **今天学了**：
  1. 使用 `openpyxl` 读取、批量写入和遍历 Excel 表格；做数据统计并生成汇总表。
  2. 使用 `PyPDF2` 读取 PDF 文件，遍历所有页面并使用 `extract_text()` 提取文本。
  3. 使用 `python-docx` 读取 Word 文档，遍历 `paragraphs` 提取文本。
  4. 数据清洗实战：通过正则表达式 `re.sub(r'\s+', ' ', text)` 将乱糟糟的 PDF 排版字符串清洗成干净的连续文本，去除多余的换行和空格，为后续喂给 AI 做准备。
- **写出的文件**：`day12_1_excel.py`, `day12_2_read_excel.py`, `day12_3_summary.py`, `day12_1_pdf.py`, `day12_2_pdf_to_txt.py`, `day12_3_word.py`, `day12_4_clean_text.py`。
- **遇到的报错/踩坑**：
  1. 新版 PyPDF2 必须用 `PdfReader`。
  2. 正则里的 `\s` 会把换行符也吃掉，导致文本变成一行。学会了根据需求调整清洗策略，比如按行读取后再清洗拼接。

  ## 日期：2026-11-07（第十三天：JSON 与 CSV 数据格式实战）
- **今天学了**：
  1. **JSON 数据格式**：理解了 JSON 本质上是跨语言传输的字符串。
     - `json.loads()`：将 JSON 字符串转为 Python 字典。
     - `json.dumps()`：将 Python 字典转为 JSON 字符串。
     - `json.dump()` 和 `json.load()`：直接用于读写本地的 `.json` 文件。
     - 掌握了处理嵌套 API 数据时的“剥洋葱”技巧（多层字典和列表的层层取值）。
  2. **CSV 数据格式**：极简版的 Excel，纯文本数据。
     - 写入：`csv.writer()` 配合 `writerows()`，**必须加 `newline=''`** 防止出现双倍行距。
     - 读取：`csv.reader()` 逐行遍历，用 `reader.line_num` 获取当前行号。
     - 进阶：了解了 `csv.DictReader` 能直接按字典格式读取数据。

- **写出的文件**：`day13_1_json.py`（JSON转换与文件读写）, `day13_2_json.py`（嵌套数据提取）, `day13_3_csv.py`（CSV读写）。

- **遇到的报错与思考**：
  1. `FileNotFoundError`：手抖把 `test.json` 写成了 `test.josn`，导致读文件找不到。明白了拼写检查（Typo）是编程中极其重要的一环。
  2. 提取复杂嵌套数据时，拆分成多个变量（如 `data_dict`, `history_dict`）比写成一长串，可读性更高，工程思维开始成型。
  3. 深刻记住了 CSV 的坑：写文件不加 `newline=''`，结果直接多出空行。

- **🎯 里程碑达成**：
  《Automate the Boring Stuff》中最核心的 Python 基础语法、网络请求、文件读写、Excel/PDF处理、正则清洗、JSON/CSV 提取**已全部通关**！

- **明日计划**：
  1. 注册国内大模型（如 DeepSeek、智谱清言等）开发者账号。
  2. 获取 `API Key`。
  3. 正式进入 AI 开发阶段，用 `requests` 给大模型发送第一个 POST 请求！

  ## 日期：2026-11-08（第十三天：时间模块与自动发邮件）
- **今天学了**：
  1. **第15章（时间）**：`time.time()` 记录时间戳、`datetime` 格式化时间、`time.sleep()` 模拟延迟。
  2. **第16章（发邮件）**：使用 `smtplib` 和 `email` 模块，配置 QQ 邮箱 SMTP，成功实现了跨域（QQ发到Outlook）的自动发邮件通知。
- **写出的文件**：`day14_1_time.py`, `day14_2_email.py`。
- **遇到的报错与思考**：
  1. WSL 纯命令行环境无法调用图形界面计算器（`gnome-calculator`）和浏览器，理解了代码运行环境的限制。
  2. `NameError: name 'server' is not defined`：发邮件时由于前面连接失败，导致 `finally` 里的 `server.quit()` 找不到变量。学会了异常处理的连带效应。
  3. `'ascii' codec can't encode characters...`：发邮件时错把占位符“这里填授权码”当成了真实密码传进去，导致编码报错。明白了敏感信息必须用真实的纯英文字符串。

  ## 日期：2026-11-09（第十四天：大模型 API 与多轮对话）
- **今天学了**：
  1. **调用 DeepSeek API**：理解了 API 调用的本质是发送 POST 请求（URL、Headers 授权、Payload 请求体）。
  2. **剥洋葱提取数据**：掌握了标准公式 `result["choices"][0]["message"]["content"]`。明白了 `choices` 为什么是个列表（因为 API 设计上支持返回多个回答）。
  3. **多轮对话记忆**：利用 `while True` 循环和 `messages.append()`，手搓了一个带记忆的多轮对话 AI 助手。
- **写出的文件**：`day15_1_ai_api.py`, `day15_2_review.py`, `day15_3_review.py`。
- **遇到的报错与思考（血泪教训）**：
  1. **【严重安全警告】**：截图时不小心泄露了真实的 DeepSeek API Key。深刻认识到了 API Key 等于钱，以后绝对不在任何地方明文展示，已去后台作废并重新生成。
  2. `role` 逻辑混淆：一开始把用户提问也写成了 `"role": "system"`，后来修正为 `"role": "user"`。明白了 system 是上帝视角设定，user 才是用户提问。
  3. `Invalid n value`：尝试让 AI 一次生成 2 个回答（`"n": 2`），被 DeepSeek 官方拦截。学会了通过阅读报错信息来理解 API 限制。

- **明日计划**：
  1. 拿下第一阶段最后的拼图：Git 和 GitHub（把代码推送到云端）。
  2. 学习 FastAPI，把今天写的 AI 对话代码包装成一个可以供浏览器访问的接口。
  3. 第一阶段（Month 1）正式毕业！

  ## 日期：2026-11-11（第十五天：Git 与 FastAPI 大通关，第一阶段毕业！）

- **今天学了**：
  1. **Git & GitHub**：掌握了 `git init`, `git add`, `git commit`, `git push`。成功将本地代码推送到云端仓库，并学会了使用 `.gitignore` 过滤虚拟环境和敏感/二进制大文件（如压缩包）。
  2. **FastAPI 入门**：
     - 安装 `fastapi` 和 `uvicorn`，理解了 ASGI 服务器的启动方式（`uvicorn main:app --reload`）。
     - 掌握了 `@app.get()` 和 `@app.post()` 路由写法。
     - 体验了 FastAPI 自动生成的 Swagger UI 测试文档（`/docs` 路径），不用写前端就能测接口。
  3. **【高光时刻】**：将 DeepSeek API 调用代码，成功封装成了一个 POST 接口 `/chat`。通过浏览器发送参数，成功获取 AI 的 JSON 回复。
  4. **【概念顿悟】**：搞懂了网页端“多轮对话”的底层逻辑——服务器本身是失忆的，全靠前端把历史记录打包发过来（State 管理）。

- **写出的文件**：`main.py`（FastAPI 服务端）, `test_app.py`（极简接口测试）, 完善了 `.gitignore`。

- **遇到的报错与思考**：
  1. 直接用 `python main.py` 运行没反应，明白了必须用 `uvicorn` 启动 Web 服务器。
  2. 访问首页报 `404 Not Found`，因为代码里只定义了 `/chat` 路由，没有 `/` 路由。学会了通过 `/docs` 页面来测试。
  3. 觉得自己“啥也没学会”，产生了畏难情绪。导师复盘后明白：是因为直接复制了大段代码，缺少了从零推导的过程。后来通过自己手敲极简的 3 行 FastAPI 代码，找回了掌控感。

- **🏆 第一阶段（Month 1）里程碑总结**：
  原版路线图第一个月的 6 大核心目标（读写文件、终端、HTTP请求、Git、SQL基础、FastAPI）——**除 SQL 外，已全部达成！** 我不仅掌握了 Python 基础，还提前越级打通了全栈 AI 接口调用，正式具备了开发真实 AI 应用的基础能力！

- **明日计划**：
  1. 花半小时快速补齐 SQL 基础（只学查、增、改）。
  2. 正式进入第二阶段：Prompt Engineering（提示词工程）与结构化输出（JSON）。

  ## 日期：2026-11-12（第十六天：SQL入门与 AI 结构化数据流水线 ETL）

- **今天学了**：
  1. **SQLite 数据库基础**：掌握了用代码建表（`CREATE TABLE`）、增（`INSERT`）、删（`DELETE`）、查（`SELECT`）。
  2. **提示词工程（Prompt Engineering）**：学会了通过 system 设定人设，在 user 中强限制输出格式。
  3. **结构化输出（Structured Outputs）**：使用了 `response_format={"type": "json_object"}` 魔法参数，强制大模型不废话，只吐出极其纯净的 JSON 字典。
  4. **【终极实战】**：成功编写了一个完整的 ETL（提取、转换、加载）项目。用 `PyPDF2` 提取文献内容 -> 丢给 DeepSeek 强制输出标题和关键词 JSON -> 解析为字典 -> 存入 SQLite 数据库。

- **写出的文件**：`day16_1_sql.py`（数据库测试）, `day16_3_magic_project.py`（AI PDF 提取入库机）。

- **遇到的报错与思考**：
  1. `UnicodeEncodeError`：把中文占位符填进了 headers 导致请求头报错，深刻理解了 HTTP 协议只能传英文。
  2. 拼写错误（Typo）：`Auhorization`、`sysstem` 导致请求失败。明白了排查 Bug 第一要务是检查拼写。
  3. 深刻体会到了 `response_format` 的好处：对比实验中，如果不加该参数，AI 可能会改变键名（如变成中文键），导致代码 KeyError 崩溃；加了参数后，彻底避免了需要用正则去清理脏数据的痛苦。

- **🏆 重大突破**：
  今天完成了人生第一个工业级 ETL 流水线，这意味着我已经具备了开发企业级 AI 数据处理工具的基础能力。
  另外：**严重教训，代码截图/上传前，必须彻底清理 API Key！**

- **明日计划**：
  开启 RAG（检索增强生成）的探索，尝试让 AI 通过“语义搜索”来回答特定段落的问题。