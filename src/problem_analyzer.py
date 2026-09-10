"""问题分析模块 - 帮助分解和结构化数学建模问题"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class Problem:
    """问题的结构化表示"""
    title: str
    description: str
    variables: List[str]
    constraints: List[str]
    objective: Optional[str] = None
    data_available: bool = False
    problem_type: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "title": self.title,
            "description": self.description,
            "variables": self.variables,
            "constraints": self.constraints,
            "objective": self.objective,
            "data_available": self.data_available,
            "problem_type": self.problem_type,
        }


class ProblemAnalyzer:
    """问题分析器 - 分解和分析数学建模问题"""
    
    def __init__(self):
        self.problem_types = [
            "prediction",      # 预测问题
            "optimization",    # 优化问题
            "classification",  # 分类问题
            "dynamics",        # 动态系统
            "network",         # 网络问题
            "statistical",     # 统计问题
        ]
    
    def analyze(self, problem_info: Dict[str, Any]) -> Problem:
        """分析和结构化问题
        
        Args:
            problem_info: 包含问题描述的字典，可包含以下键：
                - title: 问题标题
                - description: 问题描述
                - variables: 变量列表
                - constraints: 约束条件列表
                - objective: 目标函数
                - data_available: 是否有可用数据
        
        Returns:
            Problem: 结构化的问题对象
        """
        problem = Problem(
            title=problem_info.get("title", "Untitled Problem"),
            description=problem_info.get("description", ""),
            variables=problem_info.get("variables", []),
            constraints=problem_info.get("constraints", []),
            objective=problem_info.get("objective"),
            data_available=problem_info.get("data_available", False),
        )
        
        # 推断问题类型
        problem.problem_type = self._infer_problem_type(problem)
        
        return problem
    
    def _infer_problem_type(self, problem: Problem) -> str:
        """根据问题特征推断问题类型"""
        description_lower = problem.description.lower()
        
        # 简单的启发式规则
        if any(word in description_lower for word in ["预测", "forecast", "predict"]):
            return "prediction"
        elif any(word in description_lower for word in ["优化", "maximize", "minimize"]):
            return "optimization"
        elif any(word in description_lower for word in ["分类", "classify"]):
            return "classification"
        elif any(word in description_lower for word in ["动态", "变化", "evolution"]):
            return "dynamics"
        elif any(word in description_lower for word in ["网络", "路径", "图"]):
            return "network"
        else:
            return "statistical"
    
    def extract_key_information(self, problem: Problem) -> Dict[str, Any]:
        """从问题中提取关键信息"""
        return {
            "number_of_variables": len(problem.variables),
            "number_of_constraints": len(problem.constraints),
            "has_objective": problem.objective is not None,
            "data_requirement": "数据" if problem.data_available else "需要数据",
            "problem_type": problem.problem_type,
        }
    
    def suggest_modeling_approach(self, problem: Problem) -> List[str]:
        """根据问题类型建议建模方法"""
        approaches = {
            "prediction": [
                "时间序列分析",
                "回归模型",
                "机器学习方法",
            ],
            "optimization": [
                "线性规划",
                "非线性规划",
                "整数规划",
                "动态规划",
            ],
            "classification": [
                "逻辑回归",
                "决策树",
                "支持向量机",
                "神经网络",
            ],
            "dynamics": [
                "常微分方程 (ODE)",
                "偏微分方程 (PDE)",
                "差分方程",
            ],
            "network": [
                "图论方法",
                "网络流",
                "最短路径算法",
            ],
            "statistical": [
                "假设检验",
                "置信区间估计",
                "贝叶斯推断",
            ],
        }
        
        return approaches.get(problem.problem_type, [])
