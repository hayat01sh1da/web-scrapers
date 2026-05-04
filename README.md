[![Actions Status: UnitTest](https://github.com/hayat01sh1da/web-scrapers/workflows/UnitTest/badge.svg)](https://github.com/hayat01sh1da/web-scrapers/actions?query=workflow%3A%22UnitTest%22)
[![Actions Status: CodeQL](https://github.com/hayat01sh1da/web-scrapers/workflows/CodeQL/badge.svg)](https://github.com/hayat01sh1da/web-scrapers/actions?query=workflow%3A%22CodeQL%22)

## 1. Environment

- WSL (Ubuntu 25.10)
- Python 3.14.4

## 2. Reference

PythonによるWebスクレイピング \.入門編\. 業務効率化への第一歩 - Udemy

## 3. Sample Websites for Web Scraping

- [ログイン - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/login_page)
- [講師情報 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/mypage)
- [ランキング - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/ranking/)
- [画像 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/image)

## 4. Install Chrome Browser(WSL Users Only)

This step is required for the webdriver to avoid failure to find binary of Chrome.

```command
$ sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
$ sudo chmod -R +x /dev/null
$ wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/google.gpg > /dev/null
$ sudo apt update && sudo apt install -y google-chrome-stable
```

## 5. Download Chrome Webdriver

```command
# For Linux(WSL) Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chromedriver-linux64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-linux64.zip && \\
    mv chromedriver-linux64/chromedriver chromedriver && \\
    rm -rf chromedriver-linux64*

# For Mac Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/mac-arm64/chromedriver-mac-arm64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-mac-arm64.zip && \\
    mv chromedriver-mac-arm64/chromedriver chromedriver-for-mac && \\
    rm -rf chromedriver-mac-arm64*
```

## 6. Set Path to a Specific WebDriver as an Environment Variable according to Your OS

```bash
# For Linux(WSL) Users
echo 'export PATH_TO_WEBDRIVER="./webdrivers/chromedriver"' >> ~/.bash_profile

# For Mac Users
echo 'export PATH_TO_WEBDRIVER="./webdrivers/chromedriver"' >> ~/.zprofile
```

## 7. Make Webdriver Ready for Web Scraping

```command
$ sudo apt install libnss3-dev
$ webdrivers/chromedriver
Starting ChromeDriver 131.0.6778.264 (52183f9e99a61056f9b78535f53d256f1516f2a0-refs/branch-heads/6778_155@{#7}) on port 0
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully on port 35997.
```

## 8. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 9. Unit Test

```command
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/web-scrapers
collected 24 items

test/test_application.py ..                                              [  8%]
test/test_image_collector.py .....                                       [ 29%]
test/test_info_collector.py .....                                        [ 50%]
test/test_pillow_sample.py .......                                       [ 79%]
test/test_text_extractor.py .....                                        [100%]

============================== 24 passed in 7.58s ==============================
```
