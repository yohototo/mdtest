
```
import requests

# 访问令牌
access_token = 'YOUR_ACCESS_TOKEN'

# 请求笔记本的 URL
onenote_url = 'https://graph.microsoft.com/v1.0/me/onenote/notebooks'

# 设置请求头部
headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json'
}

# 获取 OneDrive 笔记本列表
response = requests.get(onenote_url, headers=headers)

if response.status_code == 200:
    notebooks = response.json()['value']
    if notebooks:
        # 获取第一个笔记本的 ID
        notebook_id = notebooks[0]['id']
        
        # 使用笔记本的 ID 构建笔记本内容的 URL
        notebook_content_url = f'https://graph.microsoft.com/v1.0/me/onenote/notebooks/{notebook_id}/sections'
        
        # 获取笔记本内容
        content_response = requests.get(notebook_content_url, headers=headers)
        
        if content_response.status_code == 200:
            sections = content_response.json()['value']
            if sections:
                # 获取第一个部分（section）的 ID
                section_id = sections[0]['id']
                
                # 使用部分（section）的 ID 构建获取部分内容的 URL
                section_content_url = f'https://graph.microsoft.com/v1.0/me/onenote/sections/{section_id}/pages'
                
                # 获取部分内容（笔记内容）
                pages_response = requests.get(section_content_url, headers=headers)
                
                if pages_response.status_code == 200:
                    pages = pages_response.json()['value']
                    if pages:
                        # 输出第一个页面的内容
                        first_page_content = pages[0]['content']
                        print('第一个页面的内容：', first_page_content)
                    else:
                        print('没有找到页面')
                else:
                    print('无法获取部分内容：', pages_response.text)
            else:
                print('没有找到部分')
        else:
            print('无法获取笔记本部分：', content_response.text)
    else:
        print('没有找到笔记本')
else:
    print('无法获取笔记本列表：', response.text)

```
