import sys
import os
import pytest
import allure
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.engine import FridayEngine

@allure.epic("Friday 自动化测试平台")
@allure.feature("数据驱动引擎")
@allure.story("Excel 接口自动化")
def test_run_excel_cases():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'env_config.yaml')
    excel_path = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'business_test_cases.xlsx')
    
    if not os.path.exists(config_path):
        pytest.skip("未找到 env_config.yaml，请参考 env_config.example.yaml 创建配置文件")
        
    engine = FridayEngine(config_path)
    passed, failed = engine.run_excel(excel_path)
    assert failed == 0, f"存在 {failed} 个失败用例，请检查日志！"