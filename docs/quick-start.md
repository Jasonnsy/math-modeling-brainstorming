# 快速开始指南

## 安装

```bash
pip install -r requirements.txt
```

## 基本工作流

### 步骤1：定义你的问题

```python
from src.problem_analyzer import ProblemAnalyzer

analyzer = ProblemAnalyzer()

problem = analyzer.analyze({
    "title": "销售量预测",
    "description": "根据过去3年的销售数据预测下个月的销售量",
    "variables": ["月份", "销售量", "市场指数"],
    "constraints": ["历史数据完整", "无异常值"],
    "data_available": True
})
```

### 步骤2：获取模型建议

```python
from src.model_recommender import ModelRecommender

recommender = ModelRecommender()
suggestions = recommender.recommend(problem, top_k=3)

for model in suggestions:
    print(f"模型: {model.name}")
    print(f"适用性: {model.suitability}")
    print(f"复杂度: {model.complexity}")
    print("---")
```

### 步骤3：识别参数

```python
from src.parameter_identifier import ParameterIdentifier

identifier = ParameterIdentifier()
parameters = identifier.identify_parameters(problem, "线性回归")
```

### 步骤4：数据处理

```python
import pandas as pd
from src.data_processor import DataProcessor

df = pd.read_csv("sales_data.csv")
processor = DataProcessor()
processed_data = processor.preprocess(df)
```

### 步骤5：验证结果

```python
from src.validator import ModelValidator

validator = ModelValidator()
report = validator.validate(model, data, results)
print(report)
```

## 更多资源

- [模型选择指南](model-guide.md)
- [使用示例](examples.md)
