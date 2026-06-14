[![Actions Status: UnitTest](https://github.com/hayat01sh1da/web-scrapers/workflows/UnitTest/badge.svg)](https://github.com/hayat01sh1da/web-scrapers/actions?query=workflow%3A%22UnitTest%22)
[![Actions Status: CodeQL](https://github.com/hayat01sh1da/web-scrapers/workflows/CodeQL/badge.svg)](https://github.com/hayat01sh1da/web-scrapers/actions?query=workflow%3A%22CodeQL%22)

## 1. Environment

- WSL (Ubuntu 25.10)
- Python 3.14.6

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
$ wget https://storage.googleapis.com/chrome-for-testing-public/149.0.7827.22/linux64/chromedriver-linux64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-linux64.zip && \\
    mv chromedriver-linux64/chromedriver chromedriver && \\
    rm -rf chromedriver-linux64*

# For Mac Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/149.0.7827.22/linux64/chromedriver-linux64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-linux64.zip && \\
    mv chromedriver-linux64/chromedriver chromedriver-for-mac && \\
    rm -rf chromedriver-linux64*
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
Starting ChromeDriver 149.0.7827.22 (52183f9e99a61056f9b78535f53d256f1516f2a0-refs/branch-heads/6778_155@{#7}) on port 0
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
$ invoke
============================= test session starts ==============================
platform linux -- Python 3.14.6, pytest-9.0.3, pluggy-1.6.0
rootdir: web-scrapers
configfile: pyproject.toml
collected 8 items

test/test_application.py ..                                              [ 25%]
test/test_image_collector.py .                                           [ 37%]
test/test_info_collector.py .                                            [ 50%]
test/test_pillow_sample.py ...                                           [ 87%]
test/test_text_extractor.py .                                            [100%]

============================== 8 passed in 6.79s ===============================
```

## 10. Static Code Analysis

```command
$ flake8 .
./src/image_collector.py:21:80: E501 line too long (84 > 79 characters)
./test/test_application.py:15:80: E501 line too long (87 > 79 characters)
./test/test_info_collector.py:8:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:9:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:10:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:11:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:12:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:13:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:14:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:15:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:16:80: E501 line too long (104 > 79 characters)
./test/test_info_collector.py:17:80: E501 line too long (105 > 79 characters)
./test/test_info_collector.py:18:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:19:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:20:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:21:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:22:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:23:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:24:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:25:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:26:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:27:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:28:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:29:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:30:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:31:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:32:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:33:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:34:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:35:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:36:80: E501 line too long (106 > 79 characters)
./test/test_info_collector.py:37:80: E501 line too long (106 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 11. Type Checks

```command
$ mypy .
Success: no issues found in 17 source files
```
