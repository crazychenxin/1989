#  1.电话和邮件匹配  - 找到剪贴板上的电话和邮件
import pyperclip
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? #area code
    (\s|-|\.)? #separator
    (\d{3}) #first 3 digits
    (\s|-|\.) #separator
    (\d{4}) #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5})))? #extension
    )''',re.VERBOSE)

print(mo.group(1))
# TODO:Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._ % +-] +# 名字
    @                  # @ 分割
    [a-zA-Z0-9.-] +           # 域名
    (\.[a-zA-Z{2, 4}])        

）)