
# VimeoAuto

VimeoAuto is an automation script.
Demonstrates using vimeo API to comment on a specific video, then using webUI steps to open vimeo.com via chrome, log in to account and verify that the comment added via API does appear on the video comments section.



## Deployment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
pip install selenium
```

Install the required web driver via this link:
```
https://sites.google.com/chromium.org/driver/
```
Make sure that the file is located at the same location as the .py file

## Usage

```python
import vimeo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

