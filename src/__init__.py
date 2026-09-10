"""数学建模头脑风暴工具 - 主模块"""

__version__ = "0.1.0"
__author__ = "Jasonnsy"

from .problem_analyzer import ProblemAnalyzer
from .model_recommender import ModelRecommender
from .parameter_identifier import ParameterIdentifier
from .data_processor import DataProcessor
from .validator import ModelValidator
from .visualizer import Visualizer

__all__ = [
    "ProblemAnalyzer",
    "ModelRecommender",
    "ParameterIdentifier",
    "DataProcessor",
    "ModelValidator",
    "Visualizer",
]