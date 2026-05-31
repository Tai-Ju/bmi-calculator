import re

def validate_input(weight, height, unit_system):
    """
    驗證輸入參數
    
    Args:
        weight (float): 體重
        height (float): 身高
        unit_system (str): 單位系統 ('metric' 或 'imperial')
    
    Returns:
        tuple: (is_valid, error_message)
    """
    # 檢查 weight 和 height 是否為數字
    try:
        weight = float(weight)
        height = float(height)
    except (ValueError, TypeError):
        return False, "輸入格式錯誤，請輸入數字"
    
    # 檢查 weight 和 height 是否大於 0
    if weight <= 0:
        return False, "體重必須大於 0"
    if height <= 0:
        return False, "身高必須大於 0"
    
    # 檢查 unit_system 是否有效
    if unit_system not in ['metric', 'imperial']:
        return False, "單位系統必須為 'metric' 或 'imperial'"
    
    return True, ""

def calculate_bmi(weight, height, unit_system):
    """
    計算 BMI
    
    Args:
        weight (float): 體重
        height (float): 身高
        unit_system (str): 單位系統 ('metric' 或 'imperial')
    
    Returns:
        float: BMI 值
    """
    if unit_system == 'metric':
        # 公制系統：BMI = 體重(kg) / 身高(m)^2
        bmi = weight / (height ** 2)
    else:
        # 英制系統：BMI = 703 * 體重(lb) / 身高(in)^2
        bmi = 703 * weight / (height ** 2)
    
    return round(bmi, 1)

def get_status(bmi):
    """
    根據 BMI 值獲取狀態分類
    
    Args:
        bmi (float): BMI 值
    
    Returns:
        dict: 包含分類、建議和顏色提示
    """
    # 檢查極端數值
    if bmi >= 60 or bmi < 10:
        return None, "數值異常，請重新確認身高體重"
    
    # 分類 BMI 範圍
    if bmi < 18.5:
        category = "體重過輕"
        advice = "建議攝取充足營養，並諮詢營養師。"
        color = "藍色 / Blue"
    elif 18.5 <= bmi < 25:
        category = "正常範圍"
        advice = "非常棒！請繼續保持健康的飲食與運動。"
        color = "綠色 / Green"
    elif 25 <= bmi < 30:
        category = "過重"
        advice = "建議開始調整飲食，並增加有氧運動。"
        color = "黃色 / Yellow"
    else:  # bmi >= 30
        category = "肥胖"
        advice = "建議諮詢醫師或健身專家，制定減重計畫。"
        color = "紅色 / Red"
    
    return {
        'category': category,
        'advice': advice,
        'color': color
    }, ""

def main_interface():
    """
    主介面 - CLI 版本
    """
    print("=== BMI 計算機 ===")
    print("1. 公制系統 (kg, m)")
    print("2. 英制系統 (lb, ft/in)")
    
    try:
        choice = int(input("請選擇單位系統 (1/2): "))
    except ValueError:
        print("輸入格式錯誤")
        return
    
    if choice == 1:
        unit_system = 'metric'
        weight_unit = 'kg'
        height_unit = 'm'
        
        weight = input(f"請輸入體重 ({weight_unit}): ")
        height = input(f"請輸入身高 ({height_unit}): ")
        
    elif choice == 2:
        unit_system = 'imperial'
        weight_unit = 'lb'
        height_unit = 'in'
        
        weight = input(f"請輸入體重 ({weight_unit}): ")
        
        try:
            ft = float(input("請輸入身高 (英呎): "))
            inch = float(input("請輸入身高 (英吋): "))
            height = ft * 12 + inch  # 轉換為英吋
        except ValueError:
            print("輸入格式錯誤")
            return
        
    else:
        print("無效的選擇")
        return
    
    # 驗證輸入
    is_valid, error_msg = validate_input(weight, height, unit_system)
    if not is_valid:
        print(error_msg)
        return
    
    # 轉換為 float
    weight = float(weight)
    height = float(height)
    
    # 計算 BMI
    bmi = calculate_bmi(weight, height, unit_system)
    
    # 獲取狀態
    status, status_error = get_status(bmi)
    if status is None:
        print(status_error)
        return
    
    # 顯示結果
    print("\n=== 計算結果 ===")
    print(f"BMI: {bmi}")
    print(f"分類: {status['category']}")
    print(f"建議: {status['advice']}")
    print(f"顏色提示: {status['color']}")

if __name__ == "__main__":
    main_interface()