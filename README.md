# ⚖️ BMI 計算機 — 學習歷程

從簡單的 CLI 腳本到完整的 FastAPI 後端，展示 Python 程式設計的學習進展。

🌐 **Portfolio 網站：[https://Tai-Ju.github.io/bmi-calculator/](https://Tai-Ju.github.io/bmi-calculator/)**

---

## 專案結構

```
bmi-calculator/
├── 01_cli/              # 入門：純 Python CLI
│   ├── spec.txt         # AI Agent 技術規格書
│   ├── bmi_calculator.py
│   └── calculate_my_bmi.py
└── 02_api/              # 進階：FastAPI 後端系統
    ├── src/
    │   ├── api/         # 路由與入口
    │   ├── models/      # Pydantic 資料模型
    │   ├── services/    # 核心商業邏輯
    │   └── ui/          # CLI 介面
    ├── tests/           # 單元測試
    ├── test_skills/     # OpenCode skills 練習
    └── requirements.txt
```

---

## 01 — CLI 版（入門）

純 Python 實作，無需任何套件，由 AI Agent 根據 `spec.txt` 規格書自動產生。

**功能**
- 公制（kg/m）與英制（lb/ft+in）雙單位
- 輸入驗證與極端值檢查
- BMI 分類與健康建議

```bash
python 01_cli/bmi_calculator.py
```

| BMI | 分類 | 顏色提示 |
|-----|------|---------|
| < 18.5 | 體重過輕 | 藍色 |
| 18.5–24.9 | 正常範圍 | 綠色 |
| 25.0–29.9 | 過重 | 黃色 |
| ≥ 30.0 | 肥胖 | 紅色 |

---

## 02 — FastAPI 版（進階）

完整的 REST API 後端，採用分層架構設計。

**功能**
- `POST /calculate` — 計算 BMI 並返回 JSON
- 自動偵測身高單位（cm 或 m）
- Pydantic 自動驗證輸入
- 完整單元測試覆蓋

```bash
cd 02_api
pip install -r requirements.txt
uvicorn src.api.main:app --reload
```

API 啟動後，開啟 `http://localhost:8000/docs` 查看互動式文件。

**請求範例**
```json
POST /calculate
{
  "height": 170,
  "weight": 65
}
```

**回應範例**
```json
{
  "bmi": 22.49,
  "category": "Normal weight",
  "suggestion": "Maintain current lifestyle and healthy diet."
}
```

---

## 學習歷程對比

| | 01 CLI | 02 FastAPI |
|---|---|---|
| 類型 | 命令列腳本 | REST API 後端 |
| 套件 | 無 | FastAPI, Pydantic, Uvicorn |
| 架構 | 單一檔案 | 分層（api / models / services）|
| 驗證 | 手動 if/else | Pydantic 自動 |
| 測試 | 無 | unittest 覆蓋 |
| 開發方式 | AI Agent 生成 | OpenCode 輔助開發 |

---

## 環境需求

```bash
# CLI 版（無需安裝）
python 01_cli/bmi_calculator.py

# API 版
pip install fastapi uvicorn pydantic
uvicorn src.api.main:app --reload
```

- Python 3.10+
- 課程：高等程式語言與軟體設計｜國立臺北護理健康大學
