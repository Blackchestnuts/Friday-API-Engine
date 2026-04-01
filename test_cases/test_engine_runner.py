import sys
import os
import glob
import pytest
import allure
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.engine import FridayEngine

@allure.epic("Friday 自动化测试平台")
@allure.feature("数据驱动引擎")
@allure.story("Excel 接口自动化")
def test_run_all_excel_cases():
    """
    引擎总入口：自动扫描 test_data 目录下的所有业务 Excel 并执行
    【警告】用户永远不需要修改此文件
    """
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'env_config.yaml')
    
    if not os.path.exists(config_path):
        pytest.skip("未找到 env_config.yaml，请参考 env_config.example.yaml 创建")
        
    # 【核心进化】动态获取 test_data 目录路径
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'test_data')
    
    # 【核心进化】使用 glob 雷达，扫描目录下所有 .xlsx 文件，排除掉 example 模板
    excel_files = glob.glob(os.path.join(data_dir, '*.xlsx'))
    excel_files = [f for f in excel_files if 'example' not in os.path.basename(f).lower()]
    
    if not excel_files:
        pytest.skip("test_data 目录下未找到任何业务 Excel 文件 (*.xlsx)")
        
    engine = FridayEngine(config_path)
    
    total_passed = 0
    total_failed = 0
    
    # 【核心进化】遍历雷达扫到的所有 Excel，挨个执行
    for excel_path in excel_files:
        file_name = os.path.basename(excel_path)
        print(f"\n{'='*50}\n📂 [装载弹药] 发现目标: {file_name}\n{'='*50}")
        
        # 将文件名作为 Allure 报告的子标签
        with allure.step(f"执行测试集: {file_name}"):
            passed, failed = engine.run_excel(excel_path)
            total_passed += passed
            total_failed += failed
            
    # 汇总断言
    assert total_failed == 0, f"全域扫描完毕，共 {total_failed} 个用例失败！"