# docpler

HWP(한글 워드프로세서) 등 문서 파일을 Markdown으로 변환하는 Python 패키지.
Rust 코어 기반으로 빠르고 정확한 파싱을 제공합니다.

## 지원 포맷

| 포맷 | 읽기 | 출력 |
|------|------|------|
| HWP 5.0 | ✅ | Markdown |

## 설치

```bash
pip install docpler
```

## 사용법

### 기본 사용

```python
from docpler.hwp import convert

markdown = convert("document.hwp")
print(markdown)
```

### markitdown 플러그인

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.hwp")
print(result.text_content)
```

## 라이선스

MIT
