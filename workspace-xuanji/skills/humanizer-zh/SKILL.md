---
name: humanizer-zh
description: 识别并去除中英文文本中的 AI 写作痕迹，让文字读起来更自然更像人写的。当用户说 humanize、润色、去AI味、或要求将文本改得更自然时触发。
---

# Humanizer-ZH: 去除 AI 写作痕迹

中英文双语的 AI 写作痕迹去除器。基于 Wikipedia "Signs of AI writing" 指南，补充大量中文 AI 写作特征。

## 核心原则

**避免 AI 模式只是的一半工作。** 干巴巴的、毫无特色的文字和垃圾一样显眼。好的文字背后是有人的。

- 有自己的观点，别光罗列事实
- 句子长短要交错
- 承认复杂性和不确定性
- 该用"我"就用"我"
- 让文章有点"乱糟糟"的真实感

## 工作流程

1. 识别文本语言（中文 / 英文 / 混合）
2. 扫描 AI 写作特征（中英文模式都要检查）
3. 重写有问题的段落
4. 保留核心信息和语气
5. 输出 humanized 版本

---

# 英文 AI 写作模式（24大类）

## 1. 过度强调重要性、遗产和宏观趋势

**警惕词：**
stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**问题：** LLM 通过添加"代表/贡献于更广阔主题"的陈述来夸大意义。

**修复：** 删掉浮夸的陈述，只保留具体事实。

## 2. 过度强调知名性和媒体曝光

**警惕词：**
independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**问题：** AI 用"被XX媒体报道"来强行表示重要性。

**修复：** 给出具体采访内容，而不是罗列媒体名称。

## 3. 浅层"-ing"分析

**警惕词：**
highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**问题：** AI 在句子上加上现在分词短语来增加虚假深度。

**修复：** 删掉这些插入语，让句子直接说事。

## 4. 宣传性/广告性语言

**警惕词：**
boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**问题：** LLM 在"文化遗产"类话题上很难保持中立。

**修复：** 用具体描述替代形容词堆砌。

## 5. 模糊归属和滑头词汇

**警惕词：**
Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**问题：** AI 把观点归到模糊的权威人士名下，没有具体来源。

**修复：** 给出具体来源（人名/机构/时间/文章名）。

## 6. 公式化的"挑战与未来展望"章节

**警惕词：**
Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**问题：** 很多 LLM 生成的文本包含公式化的"挑战"章节。

**修复：** 用具体的项目和数据替代空话。

## 7. 过度使用的"AI 词汇"

**高频 AI 词：**
Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**问题：** 这些词在 2023 年后的文本里出现频率超高，经常搭配出现。

**修复：** 用简单直接的词替代。

## 8. 回避"is/are"（系词回避）

**警惕词：**
serves as/stands as/marks/represents [a], boasts/features/offers [a]

**问题：** LLM 用复杂的句式来替代简单的系词。

**修复：** 用 "is" / "has" /简单的主动句。

## 9. 负面排比

**问题：** "Not only...but..." / "It's not just about..., it's..." 过度使用。

**修复：** 直接说重点。

## 10. 三分法滥用

**问题：** AI 把观点强行凑成三件套来显得全面。

**修复：** 自然罗列，不凑数。

## 11. 同义反复（词循环）

**问题：** AI 有重复惩罚代码，导致过度使用同义词替换。

**修复：** 保持主语一致，不要换着词说同一件事。

## 12. 虚假范围

**问题：** "from X to Y" 结构里 X 和 Y 不在同一个有意义的尺度上。

**修复：** 删掉夸张的范围词，直接说覆盖了什么。

## 13. Em Dash 滥用

**问题：** AI 用破折号（—）比人类还多，模仿"有力"的推销文案。

**修复：** 用逗号或句号替代。

## 14. 过度加粗

**问题：** AI 机械地在粗体里强调短语。

**修复：** 该加粗就加粗，不要过度使用。

## 15. 标题式垂直列表

**问题：** AI 输出列表时，每个 item 以粗体标题+冒号开头。

**修复：** 用连贯的段落替代列表堆砌。

## 16. 标题用 Title Case

**问题：** AI 大写标题里所有主要单词。

**修复：** 句子式大小写（只有第一个单词和专有名词大写）。

## 17. Emoji 装饰

**问题：** AI 在标题或要点前加 emoji。

**修复：** 删掉 emoji，用纯文字。

## 18. 花式引号

**问题：** ChatGPT 用花式引号（"..."）代替直引号（"..."）。

**修复：** 统一用直引号。

## 19. 协作性沟通语气

**警惕词：**
I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**问题：** 聊天语气被当成内容直接贴出来了。

**修复：** 删掉客套话，直接陈述。

## 20. 知识截止免责声明

**警惕词：**
as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information...

**修复：** 有具体信息就说具体信息，没有就省略。

## 21. 谄媚/奴性语气

**问题：** 过于积极、讨好的语言。

**修复：** 中性陈述，不跪舔。

## 22. 填充短语

| Before | After |
|--------|-------|
| In order to achieve this goal | To achieve this |
| Due to the fact that it was raining | Because it was raining |
| At this point in time | Now |
| In the event that you need help | If you need help |
| The system has the ability to process | The system can process |
| It is important to note that the data shows | The data shows |

## 23. 过度委婉

**问题：** 过度限定语句。

**修复：** 直接表达。

## 24. 空洞的正面结尾

**问题：** 含糊乐观的结尾。

**修复：** 给出具体下一步或具体信息。

---

# 中文 AI 写作模式（新增）

## C1. 套路化序数词

**警惕模式：**
"首先、其次、最后"，"第一、第二、第三"，"一方面、另一方面"

**问题：** 中文 AI 写作最爱用这套顺序词，把内容强行框进三段式结构。

**修复：** 自然段落承接，不用每个点都标序号。

## C2. 废话插入语

**警惕词/句式：**
"值得一提的是"，"值得注意的是"，"需要指出的是"，"不言而喻的是"，"毋庸置疑的是"，"实际上"，"事实上"

**问题：** 废话一样的插入语，假装有洞见。

**修复：** 删掉这些词，直接说后面那句话。

## C3. 冗余目的句式

**警惕词/句式：**
"为更好地xxx"，"为了更好地xxx"，"以便xxx"，"从而xxx"，"以期xxx"

**问题：** 中文 AI 喜欢在动词前加一堆目的修饰。

**修复：** 直接用动词。

## C4. 夸大作用/意义句式

**警惕词/句式：**
"起到了...的重要作用"，"具有...的重大意义"，"对...具有深远影响"，"是...的关键所在"

**问题：** AI 喜欢给每个东西都扣上"重大""关键"帽子。

**修复：** 说具体怎么起作用的。

## C5. 虚假时代背景

**警惕词/句式：**
"在新时代背景下"，"在新形势下的"，"在XX大的指引下"，"面对百年未有之大变局"

**问题：** 强行把具体内容和宏大叙事绑一起。

**修复：** 删除这些政治套话。

## C6. 主语堆砌"我们/本人"

**问题：** 过度使用"我们"或"本人"来假装有观点。

**修复：** 该用具体主语就用具体主语，或者偶尔用"我"。

## C7. 中文排比滥用

**问题：** 三个及以上的"和"或"以及"并列，把简单事情复杂化。

**修复：** 精简并列项。

## C8. "有"字句过度

**警惕句式：**
"有一定的xxx"，"具有xxx的特点"，"具备xxx的能力"，"拥有xxx的优势"

**问题：** 句句带"有"，空洞无实质。

**修复：** 直接说是什么或做什么。

## C9. 形容词堆砌

**警惕词：**
"积极有效的"，"科学合理的"，"规范有序的"，"扎实有效的"，"全面深入的"

**问题：** AI 喜欢在名词前塞一堆形容词。

**修复：** 只留最有意义的形容词，或者直接删。

## C10. 引用滥用

**警惕词/句式：**
"正如XX所说"，"XX曾指出"，"根据XX的观点"，"据不完全统计"

**问题：** 强行引用权威来背书，但没有给出具体引用内容。

**修复：** 给出具体引用，或者删掉引言直接说观点。

## C11. 程度副词滥用

**警惕词：**
"非常"，"十分"，"极其"，"尤为"，"尤为突出"，"相当重要"

**问题：** AI 用程度副词来强化观点，但削弱了可信度。

**修复：** 删掉程度副词，让事实说话。

## C12. 被动语态堆砌

**警惕句式：**
"被广泛应用于"，"被大量用于"，"已被证明"

**问题：** 中文里过度使用被动语态显得拗口。

**修复：** 改成主动句。

## C13. 标题党句式

**警惕词/句式：**
"关于...的一切"，"带你了解..."，"原来...是这样的"

**问题：** 过于标题党，不像严肃写作。

**修复：** 正常标题。

## C14. 绝对化词汇

**警惕词：**
"完全一致"，"完全正确"，"毫无例外"，"不可或缺"

**问题：** 绝对化表达降低可信度。

**修复：** 用"基本"、"总体"、"大多数"替代。

## C15. 结束语套路

**警惕词/句式：**
"综上所述"，"总之"，"由此可见"，"综上所述，我们可以看出"

**问题：** 强行总结，啰嗦。

**修复：** 直接结束，或者用一句具体的话收尾。

---

# 中英混合处理原则

## 混合语言文本

如果文本同时包含中英文，分别按各自语言规则处理。

## 标点符号

- 中文文本用中文标点（全角：，。：；？！""）
- 英文文本用英文标点（半角：.,:;?!\""）
- 混用时保持一致性和可读性

## 专业术语

- 保留技术术语、缩写、专有名词
- 不强行翻译或解释

---

# 输出格式

```
[Humanized 版本]

---
修改说明：
- 删除了...（可选，如果改动明显）
- 改写了...（可选）
```

## 完整示例

**Before（AI味十足）：**

```
首先，我们需要认识到，人工智能技术的发展对社会产生了深远的影响。
其次，人工智能技术在各个领域都有广泛的应用，包括医疗、金融、教育等。
最后，我们相信，在不久的将来，人工智能将会更好地服务于人类社会。
此外，我们还应该看到，人工智能技术的发展也带来了一些挑战，
如就业替代、隐私保护等问题，这些问题不容忽视。
值得注意的是，这些挑战并非不可克服，我们可以通过制定相应的政策
和法规来解决这些问题，从而让人工智能技术更好地造福人类。
```

**After（有人味）：**

```
AI 对社会的影响已经在发生。医疗、金融、教育等行业都在用这套技术。
但就业和隐私方面的担忧也是真的——与其视而不见，不如认真对待。
与其喊口号，不如看看具体在发生什么，再判断该不该管、怎么管。
```

---

# 参考

本技能基于 [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，由 WikiProject AI Cleanup 维护。
