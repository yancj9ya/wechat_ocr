import wcocr  # type: ignore
import os

wx_dir = r"ver4\wx"
ocr_dir = r"ver4\ocr\wxocr.dll"
# 获取当前目录
current_file_dir = os.path.dirname(os.path.realpath(__file__))
# 拼接路径
wx_dir = os.path.join(current_file_dir, wx_dir)
ocr_dir = os.path.join(current_file_dir, ocr_dir)


class WxOcr:
    def __init__(self):
        self.wcocr = self.init_wcocr()

    def init_wcocr(self):
        if os.path.isfile(ocr_dir) and os.path.isdir(wx_dir):
            if wcocr.init(ocr_dir, wx_dir):
                print("WeChatOCR初始化成功")
                return wcocr
            else:
                print("WeChatOCR初始化失败")
                return None

    def get_ocr_result(self, img_path):
        print(f"开始识别图片 typr:{type(self.wcocr)}")
        if os.path.isfile(img_path) and self.wcocr:
            return self.wcocr.ocr(img_path)
        else:
            if self.wcocr is None:
                print("请检查图片路径是否正确")
                raise FileNotFoundError
            else:
                print("weiXinOCR未初始化")


if __name__ == "__main__":
    wx_ocr = WxOcr()
    img_path = os.path.join(current_file_dir, "6.png")
    result = wx_ocr.get_ocr_result(img_path)
    print(result)
