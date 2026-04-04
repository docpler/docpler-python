"""
HWP (한글 워드프로세서) → Markdown 변환기.
markitdown 플러그인 및 독립 사용 모두 지원.
"""
from pathlib import Path
from typing import Optional


ACCEPTED_EXTENSIONS = frozenset({".hwp"})
ACCEPTED_MIME_TYPES = frozenset({
    "application/x-hwp",
    "application/haansofthwp",
    "application/vnd.hancom.hwp",
})


def convert(path: str | Path) -> str:
    """HWP 파일을 Markdown 문자열로 변환한다."""
    from ._docpler import hwp_to_markdown
    return hwp_to_markdown(str(path))


class HwpConverter:
    """markitdown 플러그인: HWP 파일을 Markdown으로 변환."""

    def accepts(
        self,
        filename: str = "",
        mime_type: str = "",
        **kwargs,
    ) -> bool:
        ext = Path(filename).suffix.lower() if filename else ""
        return ext in ACCEPTED_EXTENSIONS or mime_type in ACCEPTED_MIME_TYPES

    def convert(self, local_path: str, **kwargs):
        if not Path(str(local_path)).suffix.lower() == ".hwp":
            return None

        try:
            from markitdown import DocumentConverterResult
            markdown_text = convert(local_path)
            return DocumentConverterResult(
                title=None,
                text_content=markdown_text,
            )
        except Exception as exc:
            raise ValueError(f"HWP 변환 실패: {exc}") from exc
