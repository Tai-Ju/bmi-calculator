import bmi_calculator

# 計算你的BMI
weight = 94
height = 169 / 100  # 轉換為公尺
unit_system = 'metric'

# 驗證輸入
is_valid, error_msg = bmi_calculator.validate_input(weight, height, unit_system)
if not is_valid:
    print(f'錯誤: {error_msg}')
else:
    # 計算 BMI
    bmi = bmi_calculator.calculate_bmi(weight, height, unit_system)
    print(f'你的BMI: {bmi}')
    
    # 獲取狀態
    status, status_error = bmi_calculator.get_status(bmi)
    if status is None:
        print(f'錯誤: {status_error}')
    else:
        print(f'分類: {status["category"]}')
        print(f'建議: {status["advice"]}')
        print(f'顏色提示: {status["color"]}')