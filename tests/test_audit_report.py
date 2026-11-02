"""Render the audit starter with a local figure and verify portable HTML."""

import base64
from pathlib import Path
import re
import shutil
import subprocess

import pytest


TEMPLATE = (
    Path(__file__).resolve().parents[1]
    / "neuroimaging-validity-audit/templates/audit_template.qmd"
)
PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
    "/x8AAwMCAO+aD1sAAAAASUVORK5CYII="
)


@pytest.fixture
def rendered_report(tmp_path):
    assert TEMPLATE.is_file(), "The skill needs a renderable Quarto report template"
    assert shutil.which("quarto"), "Install Quarto to run report integration tests"
    figures = tmp_path / "figures"
    figures.mkdir()
    (figures / "check.png").write_bytes(PNG)
    source = tmp_path / "audit.qmd"
    source.write_text(
        TEMPLATE.read_text()
        + '\n![Executed check C1: fixture figure.](figures/check.png){#fig-check}\n'
    )
    result = subprocess.run(
        ["uv", "run", "quarto", "render", source.name],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    html = tmp_path / "audit.html"
    assert html.is_file(), result.stdout + result.stderr
    return html.read_text()


def test_report_embeds_figure_bytes(rendered_report):
    images = re.findall(r'src="data:image/png;base64,([^\"]+)"', rendered_report)
    assert PNG in [base64.b64decode(value) for value in images]
    assert "Executed check C1: fixture figure." in rendered_report


def test_report_has_no_external_display_resources(rendered_report):
    resources = re.findall(
        r'<(?:script|img)\b[^>]*\bsrc="([^\"]+)"'
        r'|<link\b[^>]*\bhref="([^\"]+)"',
        rendered_report,
    )
    assert all(
        (src or href).startswith(("data:", "#")) for src, href in resources
    ), resources
