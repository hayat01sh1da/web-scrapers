## 1. Environment

- WSL(Ubuntu 20.04.6 LTS)
- Python 3.13.0

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
$ sudo chmod -R 777 /dev/null
$ wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/google.gpg > /dev/null
$ sudo apt update && sudo apt install -y google-chrome-stable
```

## 5. Download Chrome Webdriver

```command
# For Linux(WSL) Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-linux64.zip && \\
    mv chromedriver-linux64/chromedriver chromedriver && \\
    rm -rf chromedriver-linux64*

# For Mac Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/mac-arm64/chromedriver-mac-arm64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-mac-arm64.zip && \\
    mv chromedriver-mac-arm64/chromedriver chromedriver-for-mac && \\
    rm -rf chromedriver-mac-arm64*
```

## 6. Set Path to a Specific WebDriver as an Environment Variable according to Your OS

```bash
# For Linux(WSL) Users
echo 'export PATH_TO_WEBDRIVER="./webdrivers/chromedriver-for-linux"' >> ~/.bash_profile

# For Mac Users
echo 'export PATH_TO_WEBDRIVER="./webdrivers/chromedriver-for-mac"' >> ~/.zprofile
```

## 7. Make Webdriver Ready for Web Scraping

```command
# For Linux(WSL) Users
$ webdrivers/chromedriver-for-linux
Starting ChromeDriver 125.0.6422.141 (6b4b19e9dfbb93aa414dc045bd445287977d8d7a-refs/branch-heads/6312_46@{#3}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.

# For Mac Users
$ webdrivers/chromedriver-for-mac
Starting ChromeDriver 125.0.6422.141 (6b4b19e9dfbb93aa414dc045bd445287977d8d7a-refs/branch-heads/6312_46@{#3}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```

## 8. Bulk Execution of Unit Tests

```command
$ python -m unittest discover ./test
.............../home/hayat01sh1da/.pyenv/versions/3.13.0/lib/python3.13/unittest/suite.py:107: ResourceWarning: unclosed file <_io.BufferedReader name='/mnt/c/Users/binlh/Documents/web/web-scrapers/imgs/bird.jpg'>
  for index, test in enumerate(self):
ResourceWarning: Enable tracemalloc to get the object allocation traceback
..../home/hayat01sh1da/.pyenv/versions/3.13.0/lib/python3.13/unittest/suite.py:84: ResourceWarning: unclosed file <_io.BufferedReader name='/mnt/c/Users/binlh/Documents/web/web-scrapers/imgs/bird.jpg'>
  return self.run(*args, **kwds)
ResourceWarning: Enable tracemalloc to get the object allocation traceback
.....
----------------------------------------------------------------------
Ran 24 tests in 74.834s

OK
```
