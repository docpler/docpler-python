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

md = MarkItDown(enable_plugins=True)
result = md.convert("document.hwp")
print(result.text_content)
```

## 라이선스

이 프로젝트는 MIT 라이선스로 제공되며, 현재 버전의 사용에 별도의 제약은 없습니다.

- **Python 래퍼 코드**: 오픈소스 (MIT)
- **Rust 코어 엔진**: 컴파일된 바이너리로 배포되며, 소스 코드는 비공개입니다.

## HWP 포맷 관련 고지

본 제품은 한글과컴퓨터의 한글 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.

HWP 파일 포맷 공개 문서의 저작권은 (주)한글과컴퓨터에 있으며,
공개 문서의 전문은 [한글과컴퓨터 공식 페이지](https://www.hancom.com/etc/hwpDownload.do)에서 확인할 수 있습니다.
