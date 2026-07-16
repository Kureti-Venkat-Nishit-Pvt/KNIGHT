#!/usr/bin/env python3
"""
Render KNIGHT presenter diagrams locally as high-resolution PNG files.

No Node.js, mermaid-cli, or external APIs required — uses Pillow only.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Pillow is required. Install with: pip install pillow"
    ) from exc

ROOT = Path(__file__).resolve().parent.parent
WIDTH = 2400
MARGIN = 48
LINE_GAP = 8
BOX_PAD_X = 20
BOX_PAD_Y = 14
FONT_SIZE = 22
TITLE_SIZE = 30
SUBTITLE_SIZE = 24

# Colour palette (KNIGHT / AWS-inspired)
C_BG = (248, 250, 252)
C_TEXT = (17, 24, 39)
C_GATE = (255, 243, 205)
C_GATE_BORDER = (133, 100, 4)
C_PIPELINE = (209, 236, 241)
C_PIPELINE_BORDER = (12, 84, 96)
C_AWS = (255, 153, 0)
C_AWS_BORDER = (35, 47, 62)
C_AWS_TEXT = (255, 255, 255)
C_SCENE = (232, 244, 253)
C_SCENE_BORDER = (21, 101, 192)
C_ACTION = (241, 248, 233)
C_ACTION_BORDER = (51, 105, 30)
C_HIGHLIGHT = (255, 243, 224)
C_HIGHLIGHT_BORDER = (230, 81, 0)
C_ARROW = (75, 85, 99)
C_SUBGRAPH = (237, 242, 247)
C_SUBGRAPH_BORDER = (148, 163, 184)


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if bold:
        candidates += [
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
    else:
        candidates += [
            "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.multiline_textbbox((0, 0), text, font=font, spacing=LINE_GAP)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> str:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            trial = f"{current} {word}"
            w, _ = text_size(draw, trial, font)
            if w <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return "\n".join(lines)


def draw_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    label: str,
    *,
    fill: tuple[int, int, int],
    border: tuple[int, int, int],
    text_color: tuple[int, int, int] = C_TEXT,
    font: ImageFont.ImageFont,
    radius: int = 12,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=border, width=2)
    x0, y0, x1, y1 = xy
    inner_w = (x1 - x0) - 2 * BOX_PAD_X
    wrapped = wrap_text(label, font, inner_w, draw)
    tw, th = text_size(draw, wrapped, font)
    tx = x0 + ((x1 - x0) - tw) // 2
    ty = y0 + ((y1 - y0) - th) // 2
    draw.multiline_text((tx, ty), wrapped, fill=text_color, font=font, spacing=LINE_GAP, align="center")


def draw_arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    *,
    width: int = 3,
) -> None:
    draw.line([start, end], fill=C_ARROW, width=width)
    # Simple arrowhead
    ex, ey = end
    sx, sy = start
    if abs(ey - sy) >= abs(ex - sx):
        # vertical dominant
        direction = 1 if ey > sy else -1
        draw.polygon(
            [(ex, ey), (ex - 10, ey - 14 * direction), (ex + 10, ey - 14 * direction)],
            fill=C_ARROW,
        )
    else:
        direction = 1 if ex > sx else -1
        draw.polygon(
            [(ex, ey), (ex - 14 * direction, ey - 10), (ex - 14 * direction, ey + 10)],
            fill=C_ARROW,
        )


def draw_subgraph(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    *,
    title_font: ImageFont.ImageFont,
) -> None:
    draw.rounded_rectangle(xy, radius=16, fill=C_SUBGRAPH, outline=C_SUBGRAPH_BORDER, width=2)
    x0, y0, x1, _ = xy
    draw.text((x0 + 16, y0 + 10), title, fill=C_TEXT, font=title_font)


def render_workflow_architecture() -> Image.Image:
    font = load_font(FONT_SIZE)
    title_font = load_font(TITLE_SIZE, bold=True)
    sub_font = load_font(SUBTITLE_SIZE, bold=True)

    height = 2100
    img = Image.new("RGB", (WIDTH, height), C_BG)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), "KNIGHT — Workflow Architecture", fill=C_TEXT, font=title_font)
    draw.text(
        (MARGIN, MARGIN + 42),
        "Commit → Pre-commit → GitHub → Terragrunt/Terraform → AWS (KNIGHT_mark_1)",
        fill=C_ARROW,
        font=font,
    )

    cx = WIDTH // 2
    y = 130
    box_w, box_h = 360, 88

    def centered_box(label: str, top: int, w: int = box_w, h: int = box_h, **kwargs) -> tuple[int, int, int, int]:
        x0 = cx - w // 2
        rect = (x0, top, x0 + w, top + h)
        draw_box(draw, rect, label, font=font, **kwargs)
        return rect

    dev = centered_box("Developer", y, fill=(255, 255, 255), border=(100, 116, 139))
    y += box_h + 36
    commit = centered_box("git commit\nbranch: K_Test_1", y, fill=(255, 255, 255), border=(100, 116, 139))
    draw_arrow(draw, (cx, dev[3]), (cx, commit[1]))

    # Pre-commit subgraph
    pg_top = y + box_h + 28
    pg = (MARGIN + 40, pg_top, WIDTH - MARGIN - 40, pg_top + 170)
    draw_subgraph(draw, pg, "Pre-commit Governance Hooks (local gate)", title_font=sub_font)
    hooks = ["terraform_fmt", "terraform_validate", "tflint", "tfsec"]
    hw, hh = 220, 72
    gap = 36
    total_w = len(hooks) * hw + (len(hooks) - 1) * gap
    hx = cx - total_w // 2
    hy = pg_top + 58
    prev_right = None
    for hook in hooks:
        rect = (hx, hy, hx + hw, hy + hh)
        draw_box(draw, rect, hook, fill=C_GATE, border=C_GATE_BORDER, font=font)
        if prev_right is not None:
            draw_arrow(draw, (prev_right, hy + hh // 2), (hx, hy + hh // 2))
        prev_right = hx + hw
        hx += hw + gap

    draw_arrow(draw, (cx, commit[3]), (cx, pg[1]))

    y = pg[3] + 36
    push = centered_box("git push", y, w=280, h=72, fill=(255, 255, 255), border=(100, 116, 139))
    draw_arrow(draw, (cx, pg[3]), (cx, push[1]))

    y += 72 + 36
    gh = centered_box("GitHub\nbranch: K_Test_1", y, w=320, h=88, fill=(255, 255, 255), border=(100, 116, 139))
    draw_arrow(draw, (cx, push[3]), (cx, gh[1]))

    # Parallel pipelines subgraph
    pl_top = y + 88 + 28
    pl = (MARGIN + 20, pl_top, WIDTH - MARGIN - 20, pl_top + 220)
    draw_subgraph(draw, pl, "Parallel GitHub Actions Workflows", title_font=sub_font)
    tf_rect = (pl[0] + 80, pl_top + 58, pl[0] + 80 + 520, pl_top + 58 + 130)
    tg_rect = (pl[2] - 80 - 520, pl_top + 58, pl[2] - 80, pl_top + 58 + 130)
    draw_box(
        draw,
        tf_rect,
        "Terraform Pipeline\nfmt → init → validate\n→ plan → apply\n(per-env matrix: stage, prod)",
        fill=C_PIPELINE,
        border=C_PIPELINE_BORDER,
        font=font,
    )
    draw_box(
        draw,
        tg_rect,
        "Terragrunt Pipeline\nrun-all plan\n→ run-all apply\n(DRY · single root config)",
        fill=C_PIPELINE,
        border=C_PIPELINE_BORDER,
        font=font,
    )
    draw_arrow(draw, (cx, gh[3]), (cx, pl[1]))
    draw_arrow(draw, (cx, pl[1] + 30), (tf_rect[0] + 260, tf_rect[1]))
    draw_arrow(draw, (cx, pl[1] + 30), (tg_rect[0] + 260, tg_rect[1]))

    # Backends subgraph
    be_top = pl[3] + 36
    be = (MARGIN + 20, be_top, WIDTH - MARGIN - 20, be_top + 260)
    draw_subgraph(draw, be, "Remote State Backends", title_font=sub_font)
    tf_be = (be[0] + 80, be_top + 58, be[0] + 80 + 520, be_top + 58 + 170)
    tg_be = (be[2] - 80 - 520, be_top + 58, be[2] - 80, be_top + 58 + 170)
    draw_box(
        draw,
        tf_be,
        "Raw Terraform — HARDCODED\nknight-tfstate-<env>-manual\nknight-tf-locks-<env>\n(manual bootstrap required)",
        fill=(254, 226, 226),
        border=(185, 28, 28),
        font=font,
    )
    draw_box(
        draw,
        tg_be,
        "Terragrunt — AUTO-BOOTSTRAP\nknight-tfstate-<account-id>\nknight-terragrunt-locks\nkey = path_relative_to_include()",
        fill=(220, 252, 231),
        border=(22, 101, 52),
        font=font,
    )
    draw_arrow(draw, ((tf_rect[0] + tf_rect[2]) // 2, tf_rect[3]), ((tf_be[0] + tf_be[2]) // 2, tf_be[1]))
    draw_arrow(draw, ((tg_rect[0] + tg_rect[2]) // 2, tg_rect[3]), ((tg_be[0] + tg_be[2]) // 2, tg_be[1]))

    y = be[3] + 36
    iam = centered_box("AWS IAM User: KNIGHT_mark_1\n(via GitHub Secrets / local env)", y, w=560, h=96, fill=C_AWS, border=C_AWS_BORDER, text_color=C_AWS_TEXT)
    draw_arrow(draw, ((tf_be[0] + tf_be[2]) // 2, tf_be[3]), (cx - 80, iam[1]))
    draw_arrow(draw, ((tg_be[0] + tg_be[2]) // 2, tg_be[3]), (cx + 80, iam[1]))

    y += 96 + 36
    res = centered_box(
        "Resource Deployment\nknight-raw-<env>-storage (raw TF)  ·  knight-<env>-storage (Terragrunt)\nencrypted · versioned · private S3 buckets",
        y,
        w=900,
        h=120,
        fill=C_AWS,
        border=C_AWS_BORDER,
        text_color=C_AWS_TEXT,
    )
    draw_arrow(draw, (cx, iam[3]), (cx, res[1]))

    return img.crop((0, 0, WIDTH, res[3] + MARGIN))


def render_live_demo_runbook() -> Image.Image:
    font = load_font(FONT_SIZE)
    title_font = load_font(TITLE_SIZE, bold=True)
    scene_font = load_font(SUBTITLE_SIZE, bold=True)
    small_font = load_font(19)

    scenes = [
        (
            "Scene 1 · Repository Overview · 5 min",
            C_SCENE,
            C_SCENE_BORDER,
            [
                "Branch strategy: K_Test_1 · AWS_Destroy_KNIGHT_mark_1",
                "Walk terraform/ (anti-pattern) vs terragrunt/ (DRY)",
                "Show CI badges and .pre-commit-config.yaml",
            ],
        ),
        (
            "Scene 2 · Raw Terraform Anti-Pattern · 10 min",
            C_SCENE,
            C_SCENE_BORDER,
            [
                "cat terraform/stage/backend.tf — hardcoded bucket",
                "Manual S3 + DynamoDB bootstrap (pain point)",
                "terraform init → plan → apply",
            ],
        ),
        (
            "Scene 3 · Terragrunt DRY Pattern · 10 min",
            C_SCENE,
            C_SCENE_BORDER,
            [
                "cat terragrunt/terragrunt.hcl — single remote_state",
                "terragrunt run-all plan — AUTO-BOOTSTRAP backend ✦",
                "terragrunt run-all apply — module reuse",
            ],
        ),
        (
            "Scene 4 · Governance & CI/CD · 10 min",
            C_SCENE,
            C_SCENE_BORDER,
            [
                "pre-commit run --all-files (fmt · validate · tflint · tfsec)",
                "git push to K_Test_1",
                "Watch parallel Actions: Terraform matrix + Terragrunt run-all",
            ],
        ),
        (
            "Scene 5 · Cost Control & Destroy · 5 min",
            C_HIGHLIGHT,
            C_HIGHLIGHT_BORDER,
            [
                "git checkout AWS_Destroy_KNIGHT_mark_1",
                "Review knight-destroy-pipeline.yml (KNIGHT_mark_1 IAM)",
                "Parallel destroy: terraform matrix + terragrunt run-all destroy ✦",
            ],
        ),
        (
            "Scene 6 · Q&A & Discussion · 10 min",
            C_SCENE,
            C_SCENE_BORDER,
            [
                "Scalability and team collaboration",
                "State isolation and migration path",
                "Emergency teardown and cost savings",
            ],
        ),
    ]

    scene_h = 220
    gap = 28
    header = 120
    height = header + len(scenes) * (scene_h + gap) + MARGIN
    img = Image.new("RGB", (WIDTH, height), C_BG)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN, MARGIN), "KNIGHT — Live Demo Runbook", fill=C_TEXT, font=title_font)
    draw.text(
        (MARGIN, MARGIN + 42),
        "6-Scene Presenter Script  ·  Total runtime ~50 minutes",
        fill=C_ARROW,
        font=font,
    )

    y = header
    prev_bottom = None
    for title, fill, border, bullets in scenes:
        rect = (MARGIN, y, WIDTH - MARGIN, y + scene_h)
        draw.rounded_rectangle(rect, radius=16, fill=fill, outline=border, width=2)
        draw.text((rect[0] + 20, rect[1] + 14), title, fill=C_TEXT, font=scene_font)

        by = rect[1] + 56
        for bullet in bullets:
            draw.text((rect[0] + 36, by), f"•  {bullet}", fill=C_TEXT, font=small_font)
            by += 34

        if prev_bottom is not None:
            draw_arrow(draw, (WIDTH // 2, prev_bottom), (WIDTH // 2, rect[1]))
        prev_bottom = rect[3]
        y += scene_h + gap

    return img


def main() -> int:
    outputs = {
        "workflow_architecture.png": render_workflow_architecture(),
        "live_demo_runbook.png": render_live_demo_runbook(),
    }

    print(f"KNIGHT local diagram renderer — output: {ROOT}")
    for name, image in outputs.items():
        path = ROOT / name
        image.save(path, format="PNG", optimize=True)
        print(f"  OK  {name} ({image.width}x{image.height})")

    print("\nAll diagrams rendered successfully (local Pillow renderer).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
