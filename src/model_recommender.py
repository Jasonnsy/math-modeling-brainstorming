"""模型推荐模块 - 根据问题特征推荐合适的数学模型"""

from typing import List, Dict, Any
from dataclasses import dataclass
from .problem_analyzer import Problem


@dataclass
class ModelSuggestion:
    """模型建议的数据结构"""
    name: str
    suitability: float  # 0-1 之间的适用性评分
    description: str
    advantages: List[str]
    disadvantages: List[str]
    complexity: str  # 低、中、高
    data_requirement: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "suitability": self.suitability,
            "description": self.description,
            "advantages": self.advantages,
            "disadvantages": self.disadvantages,
            "complexity": self.complexity,
            "data_requirement": self.data_requirement,
        }


class ModelRecommender:
    """模型推荐器 - 为不同类型的问题推荐合适的数学模型"""
    
    def __init__(self):
        self.models = self._initialize_models()
    
    def _initialize_models(self) -> Dict[str, List[ModelSuggestion]]:
        """初始化所有可用的模型"""
        return {
            "prediction": [
                ModelSuggestion(
                    name="线性回归",
                    suitability=0.85,
                    description="假设因变量与自变量之间存在线性关系",
                    advantages=["模型简单", "易于解释", "计算速度快"],
                    disadvantages=["无法捕捉非线性关系"],
                    complexity="低",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="多项式回归",
                    suitability=0.75,
                    description="使用多项式函数进行拟合",
                    advantages=["灵活性高", "可以拟合曲线"],
                    disadvantages=["容易过拟合", "高阶多项式数值不稳定"],
                    complexity="中",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="时间序列模型 (ARIMA)",
                    suitability=0.90,
                    description="专门用于时间序列预测",
                    advantages=["考虑时间依赖性", "效果好"],
                    disadvantages=["需要平稳性假设", "需要较多历史数据"],
                    complexity="中",
                    data_requirement="较高"
                ),
                ModelSuggestion(
                    name="神经网络",
                    suitability=0.80,
                    description="深度学习方法",
                    advantages=["非常灵活", "可以学习复杂模式"],
                    disadvantages=["需要大量数据", "难以解释"],
                    complexity="高",
                    data_requirement="很高"
                ),
            ],
            "optimization": [
                ModelSuggestion(
                    name="线性规划 (LP)",
                    suitability=0.95,
                    description="目标函数和约束都是线性的优化问题",
                    advantages=["求解高效", "最优解保证"],
                    disadvantages=["只能处理线性问题"],
                    complexity="低",
                    data_requirement="低"
                ),
                ModelSuggestion(
                    name="非线性规划 (NLP)",
                    suitability=0.80,
                    description="包含非线性目标函数或约束的优化",
                    advantages=["更灵活", "应用范围广"],
                    disadvantages=["求解困难", "可能陷入局部最优"],
                    complexity="高",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="整数规划 (IP)",
                    suitability=0.85,
                    description="决策变量必须是整数的优化",
                    advantages=["适合决策问题"],
                    disadvantages=["计算复杂度高"],
                    complexity="高",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="动态规划 (DP)",
                    suitability=0.80,
                    description="分阶段决策问题的最优化方法",
                    advantages=["理论完善", "适合多阶段问题"],
                    disadvantages=["维数灾难"],
                    complexity="中",
                    data_requirement="中等"
                ),
            ],
            "classification": [
                ModelSuggestion(
                    name="逻辑回归",
                    suitability=0.85,
                    description="用于二分类问题的线性模型",
                    advantages=["简单", "易解释", "概率输出"],
                    disadvantages=["只适用二分类或一对多"],
                    complexity="低",
                    data_requirement="低"
                ),
                ModelSuggestion(
                    name="决策树",
                    suitability=0.80,
                    description="树形结构的分类方法",
                    advantages=["易解释", "无需数据预处理"],
                    disadvantages=["容易过拟合"],
                    complexity="中",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="支持向量机 (SVM)",
                    suitability=0.85,
                    description="基于最大间隔分类",
                    advantages=["高维数据表现好", "内存高效"],
                    disadvantages=["需要特征缩放"],
                    complexity="中",
                    data_requirement="中等"
                ),
            ],
            "dynamics": [
                ModelSuggestion(
                    name="常微分方程 (ODE)",
                    suitability=0.90,
                    description="描述系统随时间的变化",
                    advantages=["理论完善", "物理意义清晰"],
                    disadvantages=["求解困难"],
                    complexity="中",
                    data_requirement="中等"
                ),
                ModelSuggestion(
                    name="偏微分方程 (PDE)",
                    suitability=0.75,
                    description="涉及多个自变量的动态系统",
                    advantages=["描述能力强"],
                    disadvantages=["求解非常困难"],
                    complexity="高",
                    data_requirement="很高"
                ),
            ],
            "network": [
                ModelSuggestion(
                    name="最短路径算法",
                    suitability=0.90,
                    description="找到网络中两点间的最短路",
                    advantages=["算法成熟", "计算快"],
                    disadvantages=["只适用特定问题"],
                    complexity="低",
                    data_requirement="低"
                ),
                ModelSuggestion(
                    name="网络流",
                    suitability=0.85,
                    description="描述网络中的流动",
                    advantages=["应用广泛"],
                    disadvantages=["需要图结构"],
                    complexity="中",
                    data_requirement="中等"
                ),
            ],
            "statistical": [
                ModelSuggestion(
                    name="假设检验",
                    suitability=0.90,
                    description="基于样本数据进行统计推断",
                    advantages=["理论严格"],
                    disadvantages=["需要足够样本量"],
                    complexity="中",
                    data_requirement="中等"
                ),
            ]
        }
    
    def recommend(self, problem: Problem, top_k: int = 5) -> List[ModelSuggestion]:
        """为问题推荐合适的模型
        
        Args:
            problem: 分析后的问题
            top_k: 返回前k个建议
        
        Returns:
            模型建议列表，按适用性排序
        """
        problem_type = problem.problem_type or "statistical"
        available_models = self.models.get(problem_type, [])
        
        # 按适用性排序
        sorted_models = sorted(
            available_models,
            key=lambda x: x.suitability,
            reverse=True
        )
        
        return sorted_models[:top_k]
    
    def get_model_details(self, model_name: str) -> Dict[str, Any]:
        """获取特定模型的详细信息"""
        for models in self.models.values():
            for model in models:
                if model.name == model_name:
                    return model.to_dict()
        return {}
