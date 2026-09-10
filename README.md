# 数学建模头脑风暴工具

一个强大的交互式工具，帮助数学建模爱好者和专业人士快速进行问题分析、模型选择、参数识别和解决方案验证。

## 🎯 核心功能

### 1. 问题分析框架
- **问题分解** - 将复杂问题拆解成可管理的子问题
- **背景信息提取** - 识别关键信息和约束条件
- **目标明确化** - 定义问题的具体目标

### 2. 模型推荐
- 根据问题特征自动推荐合适的数学模型
- 支持的模型类型：
  - 线性回归与多项式拟合
  - 微分方程模型
  - 优化模型（线性规划、非线性规划）
  - 概率统计模型
  - 时间序列模型
  - 网络图论模型

### 3. 参数识别
- 自动识别模型中的关键参数
- 参数约束条件设定
- 参数范围估计

### 4. 数据处理
- 数据预处理建议
- 缺失值处理策略
- 数据可视化

### 5. 解决方案验证
- 模型假设检验
- 结果合理性检查
- 灵敏度分析
- 误差估计

## 📁 项目结构

```
math-modeling-brainstorming/
├── README.md                      # 项目说明
├── docs/                          # 文档目录
│   ├── quick-start.md            # 快速开始指南
│   ├── model-guide.md            # 模型选择指南
│   └── examples.md               # 使用示例
├── src/                          # 源代码目录
│   ├── problem_analyzer.py       # 问题分析模块
│   ├── model_recommender.py      # 模型推荐模块
│   ├── parameter_identifier.py   # 参数识别模块
│   ├── data_processor.py         # 数据处理模块
│   ├── validator.py              # 验证模块
│   └── visualizer.py             # 可视化模块
├── examples/                     # 示例项目
│   ├── linear_regression.ipynb   # 线性回归示例
│   ├── ode_model.ipynb           # 微分方程示例
│   └── optimization.ipynb        # 优化问题示例
├── tests/                        # 测试文件
└── requirements.txt              # 依赖包列表
```

## 🚀 快速开始

### 安装

```bash
git clone https://github.com/Jasonnsy/math-modeling-brainstorming.git
cd math-modeling-brainstorming
pip install -r requirements.txt
```

### 基本使用

```python
from src.problem_analyzer import ProblemAnalyzer
from src.model_recommender import ModelRecommender

# 1. 分析问题
analyzer = ProblemAnalyzer()
problem = analyzer.analyze({
    "description": "根据历史销售数据预测下个月的销售量",
    "variables": ["时间", "销售量", "市场条件"],
    "constraints": ["数据周期为3年", "需要考虑季节性"]
})

# 2. 获取模型建议
recommender = ModelRecommender()
suggestions = recommender.recommend(problem)

# 3. 查看推荐结果
for model in suggestions:
    print(f"模型: {model.name}")
    print(f"适用性: {model.suitability}")
    print(f"描述: {model.description}")
```

## 📚 文档

- [快速开始指南](docs/quick-start.md)
- [模型选择指南](docs/model-guide.md)
- [使用示例和案例](docs/examples.md)

## 🔧 主要模块说明

| 模块 | 功能 | 输入 | 输出 |
|------|------|------|------|
| `problem_analyzer` | 问题分解和分析 | 问题描述 | 结构化问题信息 |
| `model_recommender` | 推荐合适的数学模型 | 问题特征 | 模型建议列表 |
| `parameter_identifier` | 识别关键参数 | 模型和数据 | 参数列表和约束 |
| `data_processor` | 处理和预处理数据 | 原始数据 | 清洗后的数据 |
| `validator` | 验证模型和结果 | 模型、数据、结果 | 验证报告 |
| `visualizer` | 可视化结果 | 数据和模型 | 图表和可视化 |

## 💡 支持的问题类型

- ✅ 预测问题（时间序列、回归）
- ✅ 优化问题（资源分配、最优决策）
- ✅ 动态系统（微分方程模型）
- ✅ 分类问题（机器学习方法）
- ✅ 网络问题（图论、路径规划）
- ✅ 统计问题（假设检验、置信区间）

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

如有问题或建议，请提交 Issue 或联系项目维护者。

---

**开始你的数学建模之旅吧！** 🚀