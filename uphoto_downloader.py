# -*- coding: utf-8 -*-

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# ==============================================================================
# --- 请在这里修改参数 ---
# ==============================================================================

# 1. Edge WebDriver 的路径
#    请确保这个路径是正确的。您可以将 msedgedriver.exe 放在项目文件夹中，或者使用绝对路径。
#    示例: r'C:\Users\YourUser\Downloads\edgedriver_win64\msedgedriver.exe'
EDGE_DRIVER_PATH = r'./edgedriver_win64/msedgedriver.exe'

# 2. UPhoto优拍云摄影 的相册网址
ALBUM_URL = 'https://www.uphoto.cn/******.html'

# 3. 图片下载目录
#    代码会自动在当前脚本所在的目录下创建一个名为 'uphoto_downloads' 的文件夹。
#    您也可以指定一个绝对路径，例如: r'D:\MyPhotos\Uphoto'
DOWNLOAD_DIRECTORY = os.path.join(os.getcwd(), 'uphoto_downloads')

# ==============================================================================
# --- 主程序逻辑 (通常不需要修改以下代码) ---
# ==============================================================================

def setup_driver():
    """配置并初始化 Edge WebDriver"""
    print("--- 正在配置 WebDriver ---")
    
    # 检查 WebDriver 路径是否存在
    if not os.path.exists(EDGE_DRIVER_PATH):
        print(f"错误: WebDriver 未在指定路径找到: {EDGE_DRIVER_PATH}")
        print("请下载 Microsoft Edge WebDriver 并更新 EDGE_DRIVER_PATH 变量。")
        return None

    # 创建下载目录（如果不存在）
    if not os.path.exists(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
        print(f"已创建下载目录: {DOWNLOAD_DIRECTORY}")

    # 配置 Edge 浏览器选项
    edge_options = EdgeOptions()
    # 设置自定义下载路径
    prefs = {
        "download.default_directory": DOWNLOAD_DIRECTORY,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    edge_options.add_experimental_option("prefs", prefs)

    service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=edge_options)
    print("--- WebDriver 启动成功 ---")
    return driver

def download_album(driver):
    """执行打开相册、遍历和下载图片的核心逻辑"""
    try:
        print(f"--- 正在打开相册页面: {ALBUM_URL} ---")
        driver.get(ALBUM_URL)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # 等待相册列表加载完成
        print("--- 正在等待图片列表加载... ---")
        first_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.item")))
        
        print("--- 成功定位到第一张图片，正在点击... ---")
        first_image.click()
        
        # 等待图片查看器加载
        time.sleep(2)

        current_index_text = "0"
        while True:
            try:
                # --- 获取当前图片编号和总数 ---
                # 增加稳定性：等待“当前页码”的文本发生变化后再继续
                wait.until(lambda d: d.find_element(By.ID, 'lblCurrIndex').text != current_index_text)
                current_index_elem = driver.find_element(By.ID, "lblCurrIndex")
                total_qty_elem = driver.find_element(By.ID, "lblTotalQty")
                
                current_index_text = current_index_elem.text
                current_index = int(current_index_text)
                total_qty = int(total_qty_elem.text)
                
                print(f"--- 正在处理图片: {current_index} / {total_qty} ---")

                # --- 点击下载按钮 ---
                download_button = wait.until(EC.element_to_be_clickable((By.ID, "download")))
                download_button.click()
                print(f"    > 已点击下载按钮。图片将保存到: {DOWNLOAD_DIRECTORY}")
                time.sleep(1.5) # 适当延长等待，确保下载进程开始

                # --- 检查是否为最后一张图片 ---
                if current_index >= total_qty:
                    print(f"--- 已到达最后一张图片 ({total_qty}/{total_qty})。下载任务完成。 ---")
                    break

                # --- 使用键盘右箭头切换到下一张图片 ---
                ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
                print("    > 已模拟键盘右箭头，切换到下一张。")
                

            except (TimeoutException, NoSuchElementException) as e:
                print(f"错误：在处理图片时找不到元素或超时。当前图片编号：{current_index_text}")
                print(f"错误详情: {e}")
                print("可能是网络问题或页面结构变化。脚本将终止。")
                break
            except Exception as e:
                print(f"发生未知错误: {e}")
                break

    finally:
        print("--- 脚本执行完毕，将在5秒后关闭浏览器。 ---")
        time.sleep(5)
        if 'driver' in locals() and driver:
            driver.quit()

if __name__ == "__main__":
    driver = setup_driver()
    if driver:
        download_album(driver)