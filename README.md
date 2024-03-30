## 1. Environment

* WSL(Ubuntu 20.04.6 LTS)
* Python 3.12.2

## 2. Reference

PythonによるWebスクレイピング \.入門編\. 業務効率化への第一歩 - Udemy

## 3. Sample Websites for Web Scraping

* [ログイン - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/login_page)
* [講師情報 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/mypage)
* [ランキング - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/ranking/)
* [画像 - Webスクレイピング入門](https://scraping-for-beginner.herokuapp.com/image)

## 4. Install Chrome Browser(WSL Users Only)

This step is required for the webdriver to avoid failure to find binary of Chrome.

```command
$ sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
$ sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
$ sudo apt update && apt install -y google-chrome-stable
```

## 5. Download Chrome Webdriver

```command
# For Linux(WSL) Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.58/linux64/chromedriver-linux64.zip -P ./webdrivers/ && \\
    cd ./webdrivers/ && \\
    unzip chromedriver-linux64.zip && \\
    mv chromedriver-linux64/chromedriver chromedriver-for-linux && \\
    rm -rf chromedriver-linux64*

# For Mac Users
$ wget https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.58/mac-arm64/chromedriver-mac-arm64.zip -P ./webdrivers/ && \\
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
$ webdrivers/chromedriver-for-linux
Starting ChromeDriver 123.0.6312.58 (6b4b19e9dfbb93aa414dc045bd445287977d8d7a-refs/branch-heads/6312_46@{#3}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```

## 8. Run Unit Tests

```command
$ python test/test_application.py
..
----------------------------------------------------------------------
Ran 2 tests in 2.197s

OK

$ python test/test_image_collector.py
.....
----------------------------------------------------------------------
Ran 5 tests in 45.932s

OK

$ python test/test_info_collector.py 
.....
----------------------------------------------------------------------
Ran 5 tests in 13.142s

OK

$ python test/test_pillow_sample.py
.../home/hayat01sh1da/.pyenv/versions/3.12.2/lib/python3.12/unittest/suite.py:107: ResourceWarning: unclosed file <_io.BufferedReader name='./imgs/bird.jpg'>
  for index, test in enumerate(self):
ResourceWarning: Enable tracemalloc to get the object allocation traceback
..../home/hayat01sh1da/.pyenv/versions/3.12.2/lib/python3.12/unittest/suite.py:84: ResourceWarning: unclosed file <_io.BufferedReader name='./imgs/bird.jpg'>
  return self.run(*args, **kwds)
ResourceWarning: Enable tracemalloc to get the object allocation traceback

----------------------------------------------------------------------
Ran 7 tests in 7.664s

OK

$ python test/test_text_extractor.py
.....
----------------------------------------------------------------------
Ran 5 tests in 11.330s

OK
