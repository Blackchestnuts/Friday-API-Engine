# Friday-API-Engine
星期五接口测试引擎
🤖 Friday API Automation Engine
零代码 · 数据驱动 · 多系统隔离 · 全链路追踪

Python 3.8+PytestAllure ReportLicense: MIT

一款面向业务测试人员的轻量级接口自动化测试引擎。告别编写冗余脚本，只需维护一份 YAML 配置与一张中文 Excel 表格，即可实现多系统接口的自动化鉴权流转与精准断言。

✨ 为什么选择 Friday？
在接口自动化领域，很多框架要么太重（需要写大量代码），要么太死（与业务系统强耦合）。Friday 引擎采用了 “配置与逻辑绝对分离” 的架构设计：

🛡 多系统隔离舱：一套引擎，通过 YAML 无缝切换不同被测系统（如 OMS、ERP），互不干扰。
🔑 自动化鉴权流转：只需配置一次登录规则，引擎自动完成 Token 提取与全生命周期注入，无需硬编码。
📊 纯中文 Excel 驱动：内置中英文翻译层，业务人员无需懂 Python，照着模板填表即可生成测试用例。
🎯 轻量级 JSONPath 断言：在 Excel 中直接写 $.code == 1 即可完成深度业务字段校验。
🌌 Allure 全息战报：深度集成 Allure，自动生成包含请求/响应切片、日志追踪的深色主题报告。
📁 架构蓝图
Friday 的核心思想是：引擎（Engine）只负责执行逻辑，业务差异全部交给配置层消化。

Friday-API-Engine/├── config/│   ├── env_config.example.yaml    # 【多系统配置中心】定义域名、鉴权规则│   └── env_config.yaml            # 【本地真实配置】已被 .gitignore 保护，不入库├── core/│   ├── engine.py                  # 【核心引擎】读取表格 -> 翻译 -> 发起请求 -> 断言│   └── logger.py                  # 【日志控制台】统一输出格式并自动留存文件├── test_cases/│   └── test_engine_runner.py      # 【唯一入口】Pytest 的启动文件├── test_data/│   └── example_test_cases.xlsx    # 【弹药库】中文表头 Excel 模板└── .github/workflows/    └── allure-deploy.yml          # 【云端巡航】GitHub Actions 自动生成报告
🚀 快速开始
只需四步，让引擎跑起来。

1. 环境准备
确保拥有 Python 3.8+ 环境，一键安装依赖：

bash

git clone https://github.com/你的用户名/Friday-API-Engine.git
cd Friday-API-Engine
pip install -r requirements.txt
2. 配置目标系统
复制示例配置，并填入真实的业务信息：

bash

cp config/env_config.example.yaml config/env_config.yaml
编辑 env_config.yaml，核心配置如下：

yaml

systems:
  your_system_key:            # 自定义系统别名
    base_url: "http://api.yourdomain.com" 
    auth:
      login_url: "/api/login"
      payload:
        username: "your_account"
        password: "your_password"
      token_extract_path: "result.token"  # 告诉引擎去 JSON 的哪个位置拿 Token
3. 编写测试用例
在 test_data/ 目录下新建 Excel 文件（如 biz_cases.xlsx），第一行必须遵循以下中文表头规范：

所属系统
用例名称
请求方式
接口路径
URL参数
请求体
断言状态码
断言路径
预期结果
your_system_key	查询用户成功	GET	/api/user/info			200	$.success	true
your_system_key	创建订单	POST	/api/order/create		{"sku":"001"}	200	$.code	1

(提示：URL参数 和 请求体 如果有值，必须符合标准 JSON 格式字符串)

4. 执行与查看报告
bash

# 运行引擎并生成 Allure 原始数据
pytest test_cases/test_engine_runner.py -v --alluredir=allure-results

# 在本地启动全息战报网页
allure serve allure-results
🛠️ 进阶指南 (TODO)
Friday 正在快速进化中，以下特性已在蓝图中：

 动态参数关联：支持在 Excel 中使用 ${extract_var} 语法，实现接口上下游数据传递。
 多环境动态切换：通过命令行参数（如 --env=test）无缝切换测试/预发环境 URL。
 自定义函数扩展：支持在 Excel 中调用内置随机数生成器（如手机号、时间戳）。
🤝 参与贡献
如果你在使用中发现 Bug，或者有新的想法，欢迎提 Issue 或 Pull Request！

📄 开源协议
本项目基于 MIT 协议开源，请放心用于企业与个人学习。