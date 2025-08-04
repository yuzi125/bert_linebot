專案分析與解釋

這是一個淡江大學校務問答LINE Bot系統，結合了Django Web框架和BERT自然語言處理技術。以下是詳細的分析：

🎯 專案目的

建立一個智能的LINE聊天機器人
自動回答淡江大學相關的校務問題
使用AI模型提供準確的問答服務

🏗️ 技術架構
1. Web框架：Django 3.1.4
主要配置：專題/settings.py
語言：繁體中文 (zh-Hant)
時區：台北時間 (Asia/Taipei)
數據庫：SQLite
安裝了 import_export 套件用於數據管理

2. LINE Bot整合
認證配置：
LINE Channel Access Token
LINE Channel Secret
主要功能：接收LINE用戶訊息並回覆智能答案

3. AI模型：BERT
模型種類：支援BERT和ALBERT模型
功能：文本分類，將用戶問題分類到149個類別中
模型文件：
配置：config.json
模型權重：pytorch_model.bin
詞彙表：bert-base-chinese-vocab.txt

4. 檔案結構說明
核心應用 (Q_A/)
views.py：處理LINE Bot的Webhook回調
models.py：定義問答對的數據模型
bert.py：BERT模型預測邏輯
core.py：機器學習核心功能

5. 關鍵功能文件
core.py：包含完整的BERT模型處理pipeline
db.sqlite3：存儲問答對的SQLite數據庫
ngrok.exe：用於建立本地到公網的tunnel

6. 系統流程
用戶發送訊息 → LINE平台
Webhook觸發 → Django的callback視圖
文本預處理 → BERT tokenizer
模型預測 → 分類到149個答案類別之一
回覆答案 → 透過LINE Bot API發送給用戶

7. 問答分類
系統支援149個不同的答案類別，涵蓋：
常見校務問答
輔系、雙主修相關問題
校園相關資訊
各學院相關問題（文學院、理學院、工學院等）

8. 使用方式
根據使用教學.txt：
啟動Django服務器：python manage.py runserver
啟動ngrok tunnel：./ngrok http 8000
將ngrok提供的HTTPS網址設定到LINE開發者平台的Webhook URL

9. 特色功能
智能問答：使用BERT模型進行自然語言理解
多模型支援：可切換使用BERT或ALBERT模型
管理後台：Django admin用於管理問答對
數據導入導出：支援CSV格式的數據管理
特殊回覆：對特定關鍵字有特製回應

10. 技術亮點
深度學習整合：將最新的BERT模型整合到實際應用中
中文自然語言處理：專門針對繁體中文進行優化
即時問答：透過LINE平台提供即時的校務諮詢服務
可擴展性：模組化設計，便於添加新的問答類別
這個專案展現了如何將現代AI技術應用到實際的校園服務中，為學生提供便利的校務查詢服務。
