# uPhoto Album Downloader / UPhoto优拍云摄影相册下载器

A Python script to automatically download all photos from a specific uphoto.cn album (UPhoto Cloud Photography) using stable keyboard navigation.

一个通过稳定的键盘导航，自动下载 UPhoto优拍云摄影 (uphoto.cn) 指定相册中所有照片的 Python 脚本。

## English

### Features

- **Keyboard Navigation**: Uses keyboard arrow keys (`→`) to navigate between photos.
  
- **Automated Browsing**: Automatically opens the album page and initiates the photo viewer.
  
- **Sequential Download**: Clicks the download button for each photo one by one.
  
- **Configurable**: Easily change the WebDriver path, album URL, and download directory.
  
- **Progress Tracking**: Real-time progress is displayed in the console.
  

### Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.x**: [Download Python](https://www.python.org/downloads/ "null")
  
2. **Microsoft Edge Browser**: Must be installed on your system.
  
3. **Microsoft Edge WebDriver**: The WebDriver version must match your installed Edge browser version. [Download WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "null")
  
4. **Selenium Library**: The required Python package.
  

### How to Use

1. **Clone or Download Repository**
  
  ```
  git clone https://github.com/WuChanging/uphoto-downloader.git
  cd uphoto-downloader
  ```
  
  Or simply download the `uphoto_downloader.py` file.
  
2. **Install Dependencies** Open your terminal or command prompt and install the Selenium library.
  
  ```
  pip install selenium
  ```
  
3. **Setup Edge WebDriver**
  
  - Download the correct version of `msedgedriver.exe` from the [official site](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "null").
    
  - Place the `msedgedriver.exe` file in the same directory as the script, or note its full path.
    
4. **Configure the Script** Open `uphoto_downloader.py` with a text editor and modify the parameters in the configuration section at the top of the file.
  
5. **Run the Script** Execute the script from your terminal.
  
  ```
  python uphoto_downloader.py
  ```
  
  The script will launch an Edge browser window and begin the download process. All photos will be saved to the specified `DOWNLOAD_DIRECTORY`.
  

### Configuration

You must set the following variables at the top of the `uphoto_downloader.py` script:

- `EDGE_DRIVER_PATH`: The file path to your `msedgedriver.exe`.
  
  - Example (if in the same folder): `r'./edgedriver_win64/msedgedriver.exe'`
    
  - Example (absolute path): `r'C:\webdrivers\msedgedriver.exe'`
    
- `ALBUM_URL`: The full URL of the UPhoto (uphoto.cn) album you want to download.
  
- `DOWNLOAD_DIRECTORY`: The folder where you want to save the downloaded photos. The script will create this folder if it doesn't exist.
  

### Disclaimer

- This script is intended for educational and personal use only.
  
- Please respect the copyright of the photos. Do not use this script for any malicious purposes.
  
- The script's functionality depends on the website's structure. If uphoto.cn updates its site, this script may need to be modified.
  

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT "null").

## 中文

### 功能特性

- **键盘导航**: 使用键盘方向键 (`→`) 切换照片。
  
- **自动浏览**: 自动打开相册页面，并进入照片查看模式。
  
- **顺序下载**: 自动为每张照片点击下载按钮。
  
- **可配置**: 轻松修改 WebDriver 路径、相册网址和下载目录。
  
- **进度跟踪**: 在控制台中实时显示下载进度。
  

### 环境要求

在运行脚本之前，请确保您已安装以下环境和工具：

1. **Python 3.x**: [下载 Python](https://www.python.org/downloads/ "null")
  
2. **微软 Edge 浏览器**: 您的电脑上必须已安装此浏览器。
  
3. **微软 Edge WebDriver**: WebDriver 的版本必须与您安装的 Edge 浏览器版本完全对应。[下载 WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "null")
  
4. **Selenium 库**: 必需的 Python 第三方库。
  

### 如何使用

1. **克隆或下载项目**
  
  ```
  git clone https://github.com/WuChanging/uphoto-downloader.git
  cd uphoto-downloader
  ```
  
  或者直接下载 `uphoto_downloader.py` 文件。
  
2. **安装依赖库** 打开终端或命令提示符，安装 Selenium 库。
  
  ```
  pip install selenium
  ```
  
3. **配置 Edge WebDriver**
  
  - 从[官方网站](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ "null")下载与您浏览器版本匹配的 `msedgedriver.exe`。
    
  - 将 `msedgedriver.exe` 文件放置在与脚本相同的文件夹中，或者记下它的完整路径。
    
4. **配置脚本参数** 使用文本编辑器打开 `uphoto_downloader.py` 文件，修改文件顶部的配置参数。
  
5. **运行脚本** 在终端中执行脚本。
  
  ```
  python uphoto_downloader.py
  ```
  
  脚本将自动启动一个 Edge 浏览器窗口并开始下载。所有照片都会被保存到您指定的 `DOWNLOAD_DIRECTORY` 文件夹中。
  

### 参数配置

您必须在 `uphoto_downloader.py` 脚本的顶部设置以下变量：

- `EDGE_DRIVER_PATH`: 指向 `msedgedriver.exe` 文件的路径。
  
  - 示例 (文件在同一目录下): `r'./edgedriver_win64/msedgedriver.exe'`
    
  - 示例 (使用绝对路径): `r'D:\Python\webdrivers\msedgedriver.exe'`
    
- `ALBUM_URL`: 您想要下载的 UPhoto优拍云摄影 (uphoto.cn) 相册的完整网址。
  
- `DOWNLOAD_DIRECTORY`: 您希望保存下载照片的文件夹路径。如果该文件夹不存在，脚本会自动创建。
  

### 免责声明

- 本脚本仅供学习交流和个人使用。
  
- 请尊重照片的版权，请勿将此脚本用于任何非法或商业用途。
  
- 脚本的可用性取决于目标网站的页面结构。如果 UPhoto优拍云摄影 (uphoto.cn) 网站更新，此脚本可能需要相应修改才能继续工作。
  

### 许可协议

本项目基于 [MIT 许可证](https://opensource.org/licenses/MIT "null") 开源。