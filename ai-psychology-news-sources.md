# AI & 心理学新闻抓取地址汇总

> 适用场景：供 AI Agent 自动抓取、RSS 订阅、API 调用。  
> 格式：每条来源给出**直接可用的抓取地址**，标注类型和免费情况。

---

## 一、AI 新闻 — RSS Feed（无需 API Key，直接抓取）

| 来源 | RSS 地址 | 更新频率 | 说明 |
|------|----------|----------|------|
| The Verge · AI | `https://www.theverge.com/ai-artificial-intelligence/rss/index.xml` | 高（30-50篇/天） | 科技媒体，AI 编辑视角 |
| MIT Technology Review | `https://www.technologyreview.com/feed/` | 中 | 学术级深度报道 |
| Anthropic News | `https://www.anthropic.com/news/rss` | 低（官方公告为主） | Claude 相关第一手信息 |
| OpenAI Blog | `https://openai.com/news/rss.xml` | 低（官方公告为主） | GPT/DALL-E 官方发布 |
| Hugging Face Blog | `https://huggingface.co/blog/feed.xml` | 中 | 开源模型与工具教程 |
| The Rundown AI | `https://www.therundown.ai/rss` | 高（每日简报） | AI 要闻精简汇总 |
| Ars Technica | `https://feeds.arstechnica.com/arstechnica/index` | 高 | 技术深度分析 |
| Unite.AI | `https://www.unite.ai/feed/` | 高 | AI 新闻与教程综合 |
| Google DeepMind Blog | `https://deepmind.google/blog/rss.xml` | 低 | DeepMind 研究发布 |
| VentureBeat · AI | `https://venturebeat.com/category/ai/feed/` | 高 | 商业与技术结合 |

---

## 二、心理学新闻 — RSS Feed（无需 API Key，直接抓取）

| 来源 | RSS 地址 | 说明 |
|------|----------|------|
| Psychology Today | `https://www.psychologytoday.com/us/front-page/rss` | 全球最大心理健康门户 |
| Psych Central | `https://psychcentral.com/feed` | 心理健康科普，面向大众 |
| Positive Psychology News | `https://positivepsychologynews.com/feed` | 积极心理学，幸福感研究 |
| Greater Good (UC Berkeley) | `https://greatergood.berkeley.edu/feeds/news` | 幸福感与社会科学 |
| APA Monitor | `https://www.apa.org/monitor/rss` | 美国心理学会官方期刊 |
| ScienceDaily · Psychology | `https://www.sciencedaily.com/rss/mind_brain/psychology.xml` | 心理学研究摘要每日推送 |
| Neurosciencenews | `https://neurosciencenews.com/feed/` | 神经科学与心理学交叉 |

---

## 三、新闻聚合 API（需 API Key，支持关键词搜索）

### 3.1 免费 / Freemium

#### GNews
- **文档**：https://gnews.io/docs/v4
- **抓取地址**：
  ```
  GET https://gnews.io/api/v4/search?q={关键词}&lang=en&token={API_KEY}
  ```
- **示例**：
  ```
  https://gnews.io/api/v4/search?q=artificial+intelligence&lang=en&token=YOUR_KEY
  ```
- **免费配额**：100 次/天，每次最多 10 条
- **注册**：https://gnews.io

---

#### TheNewsAPI
- **文档**：https://www.thenewsapi.com/documentation
- **抓取地址**：
  ```
  GET https://api.thenewsapi.com/v1/news/all?search={关键词}&language=en&api_token={API_KEY}
  ```
- **示例**：
  ```
  https://api.thenewsapi.com/v1/news/all?search=psychology&language=en&api_token=YOUR_KEY
  ```
- **免费配额**：100 次/天
- **注册**：https://www.thenewsapi.com

---

#### NewsData.io
- **文档**：https://newsdata.io/documentation
- **抓取地址**：
  ```
  GET https://newsdata.io/api/1/news?q={关键词}&language=en&apikey={API_KEY}
  ```
- **示例**：
  ```
  https://newsdata.io/api/1/news?q=AI+psychology&language=en&apikey=YOUR_KEY
  ```
- **免费配额**：200 次/天，支持全文字段
- **注册**：https://newsdata.io

---

#### Mediastack
- **文档**：https://mediastack.com/documentation
- **抓取地址**：
  ```
  GET http://api.mediastack.com/v1/news?keywords={关键词}&languages=en&access_key={API_KEY}
  ```
- **免费配额**：500 次/月
- **注册**：https://mediastack.com

---

### 3.2 开发测试免费（生产环境需付费）

#### NewsAPI.org
- **文档**：https://newsapi.org/docs
- **抓取地址**：
  ```
  GET https://newsapi.org/v2/everything?q={关键词}&language=en&sortBy=publishedAt&apiKey={API_KEY}
  ```
- **示例**：
  ```
  https://newsapi.org/v2/everything?q=artificial+intelligence&language=en&sortBy=publishedAt&apiKey=YOUR_KEY
  ```
- **注意**：免费层仅限开发（localhost），生产部署有 CORS 限制
- **注册**：https://newsapi.org

---

### 3.3 付费（AI/企业级）

#### Perigon（推荐用于 LLM Pipeline / RAG）
- **文档**：https://docs.goperigon.com
- **抓取地址**：
  ```
  GET https://api.goperigon.com/v1/all?q={关键词}&language=en&apiKey={API_KEY}
  ```
- **特点**：内置实体提取、事件聚类、全文输出，JSON 格式干净，适合直接喂给 LLM
- **注册**：https://www.goperigon.com

---

## 四、学术论文抓取（免费，无需 API Key 或有免费配额）

### 4.1 arXiv RSS（最新预印本，每日更新）

| 方向 | RSS 地址 |
|------|----------|
| AI (cs.AI) | `https://rss.arxiv.org/rss/cs.AI` |
| 机器学习 (cs.LG) | `https://rss.arxiv.org/rss/cs.LG` |
| 神经科学 (q-bio.NC) | `https://rss.arxiv.org/rss/q-bio.NC` |
| 人机交互 (cs.HC) | `https://rss.arxiv.org/rss/cs.HC` |

---

### 4.2 PubMed E-utilities API（NIH 官方，完全免费）

- **文档**：https://www.ncbi.nlm.nih.gov/home/develop/api/
- **搜索接口**：
  ```
  GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={关键词}&retmode=json&retmax=20
  ```
- **获取摘要**：
  ```
  GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={PMID列表}&retmode=xml
  ```
- **示例**：
  ```
  https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=psychology+AI&retmode=json&retmax=10
  ```
- **RSS（搜索转订阅）**：
  ```
  https://pubmed.ncbi.nlm.nih.gov/rss/search/[搜索词]/?format=rss
  ```

---

### 4.3 Semantic Scholar API（免费，学术搜索）

- **文档**：https://api.semanticscholar.org/api-docs/
- **论文搜索**：
  ```
  GET https://api.semanticscholar.org/graph/v1/paper/search?query={关键词}&fields=title,abstract,year,authors,url
  ```
- **示例**：
  ```
  https://api.semanticscholar.org/graph/v1/paper/search?query=AI+mental+health&fields=title,abstract,year,url
  ```
- **限速**：无 Key 时 100 次/5min，申请 Key 后更高

---

### 4.4 OpenAlex API（完全免费，2.5亿+ 论文）

- **文档**：https://docs.openalex.org
- **搜索接口**：
  ```
  GET https://api.openalex.org/works?search={关键词}&filter=language:en&per-page=20&mailto=your@email.com
  ```
- **示例**：
  ```
  https://api.openalex.org/works?search=psychology+artificial+intelligence&filter=language:en&per-page=20
  ```
- **注意**：请求头或参数带上邮箱可获得更高速率

---

### 4.5 GDELT Project（全球新闻大数据，完全免费）

- **文档**：https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/
- **全文搜索 API**：
  ```
  GET https://api.gdeltproject.org/api/v2/doc/doc?query={关键词}&mode=artlist&maxrecords=25&format=json
  ```
- **示例**：
  ```
  https://api.gdeltproject.org/api/v2/doc/doc?query=artificial+intelligence+psychology&mode=artlist&maxrecords=25&format=json
  ```
- **特点**：历史数据极深，支持情感分析字段，适合学术研究

---

## 五、快速参考：按用途选择

| 用途 | 推荐方案 |
|------|----------|
| 每日 AI 资讯追踪 | The Verge RSS + The Rundown AI RSS |
| 心理学科普追踪 | Psychology Today RSS + Greater Good RSS |
| 学术论文追踪 | arXiv RSS (cs.AI / q-bio.NC) + PubMed RSS |
| 开发原型/测试 | NewsAPI.org（免费开发 Key） |
| 生产环境抓取 | GNews 或 TheNewsAPI（有免费配额） |
| LLM / RAG 数据管道 | Perigon（全文 + NLP 结构化输出） |
| 大规模学术数据 | OpenAlex API 或 GDELT（完全免费） |
| 自定义关键词论文订阅 | PubMed RSS + Google Scholar Alerts |

---

## 六、RSS 抓取示例代码（Python）

```python
import feedparser
import json

feeds = {
    "verge_ai": "https://www.theverge.com/ai-artificial-intelligence/rss/index.xml",
    "mit_tech": "https://www.technologyreview.com/feed/",
    "psychology_today": "https://www.psychologytoday.com/us/front-page/rss",
    "arxiv_ai": "https://rss.arxiv.org/rss/cs.AI",
    "greater_good": "https://greatergood.berkeley.edu/feeds/news",
}

for name, url in feeds.items():
    feed = feedparser.parse(url)
    print(f"\n=== {name} ===")
    for entry in feed.entries[:3]:  # 取最新 3 条
        print(f"  标题: {entry.title}")
        print(f"  链接: {entry.link}")
        print(f"  时间: {entry.get('published', 'N/A')}")
```

---

*最后更新：2026-06*
