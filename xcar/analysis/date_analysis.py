"""使用结巴分词并统计词频"""
from jieba import Tokenizer
import jieba.analyse
from collections import Counter


class MyJieba(Tokenizer):
    """自定义jieba分词"""

    def __init__(self):
        super().__init__()
        self.text = ""
        self.path = "./xcar/analysis/stop_word.txt"

    def my_add_word(self, word, **kwargs):
        """添加词典"""
        self.add_word(word, **kwargs)

    def add_text(self, text):
        """添加文本"""
        self.text = text
        return self.text

    def add_stop_word(self, word):
        """添加停止词"""
        try:
            w = word + "\n"
            s = w.encode("utf-8")
            with open(self.path, 'ab') as f:
                f.write(s)
        except:
            print("停止词插入失败")

    def tf_idf(self, text, **kwargs):
        """tf_idf关键词"""
        jieba.analyse.set_stop_words(self.path)
        tags = jieba.analyse.extract_tags(text, topK=100)
        return tags

    def describe(self):
        """统计描述"""
        # 读取停止词
        with open(self.path, 'rb') as f:
            stop_words = [
                lines.decode('utf-8').strip() for lines in f.readlines()
            ]

        # 分词
        words = [
            x for x in self.cut(self.text)
            if len(x) >= 2 and x not in stop_words
        ]  # 过滤掉
        sample_size = len(words)  # 样本量
        c = Counter(words).most_common(100)
        tf = self.tf_idf(self.text)
        for sample in c:
            word, times = sample
            frequency = times / sample_size  # 频率
            yes = True if word in tf else False  # 是不是tf_idf关键词
            yield word, times, frequency, yes
