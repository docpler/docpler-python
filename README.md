# docpler

A Python library for converting HWP documents to Markdown.

HWP is a document format used by [Hancom Office](https://www.hancom.com/), the most widely used word processor in South Korea — commonly found in government, legal, and academic documents.

docpler uses a high-performance Rust core to parse HWP 5.0 files and produce clean Markdown output, including tables, equations, and text boxes.

## Supported Formats

| Format | Read | Output |
|--------|------|--------|
| HWP 5.0 | ✅ | Markdown |

## Installation

```bash
pip install docpler
```

## Usage

```python
from docpler.hwp import convert

markdown = convert("document.hwp")
print(markdown)
```

### MarkItDown Plugin

```bash
pip install markitdown-hwp
```

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True)
result = md.convert("document.hwp")
print(result.text_content)
```

---

# 한국어

HWP(한글 워드프로세서) 문서를 Markdown으로 변환하는 Python 패키지입니다.
Rust 코어 기반으로 빠르고 정확한 파싱을 제공합니다.

## 설치

```bash
pip install docpler
```

## 사용법

```python
from docpler.hwp import convert

markdown = convert("document.hwp")
print(markdown)
```

### markitdown 플러그인

```bash
pip install markitdown-hwp
```

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True)
result = md.convert("document.hwp")
print(result.text_content)
```

---

## License

MIT

- Python wrapper: open source (MIT)
- Rust core engine: distributed as compiled binary, source code is private.

## HWP Format Notice

This product was developed with reference to the HWP document file (.hwp) specification published by [Hancom](https://www.hancom.com/etc/hwpDownload.do).
