### 维护者

- Jclian91

### 模型使用

&emsp;&emsp;笔者将在PyTorch框架下使用HuggingFace的`中译英模型`和`英译中模型`。其中`中译英模型`的模型名称为：opus-mt-zh-en，下载网址为：[https://huggingface.co/Helsinki-NLP/opus-mt-zh-en/tree/main](https://huggingface.co/Helsinki-NLP/opus-mt-zh-en/tree/main)；`英译中模型`的模型名称为opus-mt-en-zh，下载网址为：[https://huggingface.co/Helsinki-NLP/opus-mt-en-zh/tree/main](https://huggingface.co/Helsinki-NLP/opus-mt-en-zh/tree/main) 。
&emsp;&emsp;首先我们先尝试`中译英模型`，即把中文翻译成英语，代码参考`zh_en_mt.py` .
&emsp;&emsp;接着我们先尝试`英译中模型`，即把英文翻译成汉语，代码参考`en_zh_mt.py` .

### 模型解释

&emsp;&emsp;`shap`是Python开发的一个模型解释包，可以任何机器学习模型的输出。其名称来源于SHapley Additive exPlanation，在合作博弈论的启发下SHAP构建一个加性的解释模型，所有的特征都视为“贡献者”。对于每个预测样本，模型都产生一个预测值，SHAP value就是该样本中每个特征所分配到的数值。
&emsp;&emsp;我们尝试着使用`shap`模块来对翻译模型进行解释，可以看到`shap`可视化效果非常棒的解释界面，如下：
![中译英模型代码](https://img-blog.csdnimg.cn/20210310215842225.png)
默认输出结果为翻译结果，如下：

![默认输出结果](https://img-blog.csdnimg.cn/20210310220014211.png)

模型解释的热力图效果如下：

![模型解释的热力图效果](https://img-blog.csdnimg.cn/20210310220457968.png)
从热力图中我们可以发现，空间站这个词语被翻译成space station。
&emsp;&emsp;同样，我们可以看到`英译中模型`的热力图解释效果，如下：
![`英译中模型`的热力图解释效果](https://img-blog.csdnimg.cn/20210310221033757.png)


### 参考网址

1. HuggingFace translation model: [https://huggingface.co/models?filter=zh&pipeline_tag=translation](https://huggingface.co/models?filter=zh&pipeline_tag=translation)
2. Text to Text Explanation: Machine Translation Example: [https://shap.readthedocs.io/en/latest/example_notebooks/text_examples/translation/Machine%20Translation%20Explanation%20Demo.html](https://shap.readthedocs.io/en/latest/example_notebooks/text_examples/translation/Machine%20Translation%20Explanation%20Demo.html)
