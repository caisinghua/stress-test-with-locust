# 利用 Locust 做壓測

## 前置作業

安裝 Python extension for Visual Studio Code

### Step01. 建立虛擬環境
```
python3 -m venv .venv
```

### Step02. 啟用虛擬環境
```
source .venv/bin/activate
```

### Step03. 安裝需要的套件
安裝 Locust
```
pip3 install locust
```

確認 locust 版本
```
locust --version
```
or 
```
locust -V
```

### Step04. 確認目前安裝的套件版本

現在有安裝哪一些套件
```
pip3 list
```

匯出當前安裝的套件與版本
```
pip3 freeze > requirements.txt
```

依照 requirements.txt 內定義的套件進行安裝
```
pip3 install -r requirements.txt
```


<br> 

---

<br>


# Locust 壓測 SOP
參考資料：[Internal Stress Test SOP](https://chocotv.atlassian.net/wiki/spaces/LTRT/pages/74940417/Internal+Stress+Test+SOP)
