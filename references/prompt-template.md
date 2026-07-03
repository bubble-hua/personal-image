# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## 角色参考图

**泡泡的官方形象设定图（reference sheet）位于：**
`assets/reference-sheet-bubble.png`

**重要提示**：ImageGen 的 image-to-image 模式不可用，因此**每次生图都使用纯文字精确描述**来确保泡泡形象一致。以下角色描述是从参考图中提取的视觉特征，必须严格遵守。

**从参考图提取的精确特征（必须匹配）：**
- 头身比：2.5 头身 chibi Q 版
- 画风：精致日系 Q 版手绘风（类似 chiikawa / Sumikko Gurashi 的专业质感），线条柔和干净
- 发型：深棕色**利落 bob 短发，薄侧分刘海**，发尾微内扣，头发蓬松有厚度，干净利落
- 脸型：圆偏鹅蛋脸，脸颊微圆，有粉色腮红
- 眼睛：超大圆眼（占面部 1/3+），深棕色瞳孔，有高光点，眼睫毛清晰
- 鼻子：极小几乎不画或一个小点
- 嘴唇：小嘴，根据表情变化
- 肤色：暖肤色 `#FFE0BD`
- 身材：小巧 chibi 身形，手脚圆润不尖锐
- 标准穿搭：宽松白衬衫（袖子挽起）+ 暖卡其阔腿裤 + 白色帆布鞋
- 眼镜：**黑框无镜片眼镜**（学术知性模式）/ **圆框墨镜**（酷飒日常模式），二选一
- 整体画风：日系 Q 版手绘风，线条柔和干净，**角色有饱满鲜亮的色块填充**

---

## 标准 Prompt 模板（精简版 — 推荐使用）

经过多轮测试验证，精简版 prompt 效果更好——过长的 prompt 会导致内容偏差。以下为经过验证的成功模板结构：

```text
16:9 illustration, pure white #FFFFFF background.

Character: 泡泡(Bubble), refined Japanese chibi, 2.5 heads tall. Dark brown bob hair with thin side-swept bangs. Huge round eyes (half face) with sparkle highlights and long lashes. Round cheeks, pink blush. Wearing: ivory white shirt + camel khaki wide-leg pants + white sneakers + {眼镜选择}. NO backpack. Professional chibi quality like chiikawa — cute polished adorable.

SCENE: {具体场景描述，泡泡在哪里、在做什么、动作姿态}

Elements: {关键视觉元素，用英文列出}

Colors: Lake blue #6DA4BA outlines. Hair #5D4037. Skin #FFE0BD. Pants #C9A86C. Shirt #FFF8E7. Arrow #E8D478. Circle #E8AC98. Leaf #88B880. Background pure white #FFFFFF.

50%+ empty white space. Only {3-5} text labels max. No title.
```

**变量说明：**
- `{眼镜选择}`：black-frame glasses (no lenses) 或 round-frame sunglasses
- `{具体场景描述}`：泡泡的动作、位置、与环境的关系。必须大写强调关键约束（如 "NOT stairs, NOT steps"）
- `{关键视觉元素}`：图中有哪些物件、标注、箭头、路径等
- `{3-5}`：标注文字数量上限

**场景描述编写要点：**
- 用英文大写强调否定约束，如：`Bubble is placing a rectangular BRICK on the ground. The bricks form a PATH — NOT stairs, NOT steps. Just flat bricks laid on the ground.`
- 明确泡泡的位置（left/right/center）和姿态（kneeling/squatting/standing/sitting）
- 明确物体的空间关系

---

## 完整版 Prompt 模板（需要更多细节时使用）

当精简版无法精确控制画面时，使用以下完整模板：

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background (#FFFFFF). Hand-drawn illustration style with lake blue (#6DA4BA) line art for all outlines. **Characters have BRIGHT WARM FILL COLORS inside the outlines** — this is NOT a bare line sketch! Lots of empty white space. Sparse handwritten Chinese annotations in cream yellow (#E8D478) for flow paths, shell pink (#E8AC98) for key highlights, and mint green (#88B880) for supplementary notes. Clean warm healing feeling — like a colorful chibi character illustration mixed with a hand-drawn sketch. The overall look should be vivid, luminous, and warm. No gradients, no shadows, no paper texture, no complex background, no commercial vector style.

Recurring IP character (match reference sheet exactly):
泡泡 (Bubble) — a 2.5-heads-tall chibi Q-version character with BRIGHT WARM FILL COLORS. CRITICAL: short dark brown bob hair **with thin side-swept bangs**, clean neat style, slightly inward-curled ends, fluffy — filled with `#5D4037` dark warm brown; round-oval face with soft cheeks filled with warm skin tone `#FFE0BD`; very large round eyes (1/3+ of face) with dark brown pupils and highlight dots; tiny nose; small mouth; small rounded chibi body. Standard outfit: loose white/ivory shirt `#FFF8E7` with rolled-up sleeves + warm khaki wide-leg pants `#C9A86C` + white canvas shoes. NO backpack. Lake blue `#6DA4BA` outlines everything. Bubble looks like a vivid colorful chibi character, not a line sketch. Refined Japanese chibi quality like chiikawa.
In this illustration, show Bubble in action pose — {具体动作描述}. Eyewear: round-frame sunglasses for casual/cool mode; black-frame glasses without lenses for intellectual mode. Bubble participates actively.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜 / 泡泡手帐 / 泡泡课堂}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：泡泡在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Lake blue (#6DA4BA) for ALL line art outlines (character, objects, structures). Bubble's fill colors: hair #5D4037 dark warm brown, skin #FFE0BD warm tone, shirt #FFF8E7 ivory white, pants #C9A86C warm khaki. Cream yellow (#E8D478) for main flow/path/arrows. Shell pink (#E8AC98) only for key highlights, warnings, or results. Mint green (#88B880) only for secondary notes. The illustration should feel VIVID, WARM, and LUMINOUS — characters have bright fill colors like a colorful chibi comic, not bare line art. Do NOT use pure black for lines.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, warm but not childish, artsy but not pretentious. Bubble must be the active participant, not decoration. Bubble's appearance must match the reference sheet exactly. Pure white background — no tint, no cream, no blue-grey.
```

---

## 后处理：纯白背景

ImageGen 倾向于给画面添加淡蓝灰/米白色氛围底色，无法直接生成纯白（#FFFFFF）背景。**每次生图后必须运行后处理脚本**将背景刷成纯白：

```bash
python3.11 scripts/corner_whiten_bg.py <输入图路径> <输出图路径> 210
```

**工作原理**：从图片四角 + 四边边缘出发，通过 flood fill 找到所有与边缘连通的浅色像素区域（亮度 > threshold），将其强制设为纯白 #FFFFFF。前景角色和元素完全不受影响。

**阈值说明**：
- `210`：推荐默认值。适合大部分 ImageGen 输出的淡底色。
- 如果刷白过度（刷到了角色边缘）：提高到 `220-230`。
- 如果背景没刷干净（残留底色）：降低到 `190-200`。

**预期效果**：约 80%+ 的像素被刷白，角色和内容元素完整保留。

---

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强泡泡参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 泡泡 more central to the conceptual action. 泡泡 should be actively writing, pointing, thinking, or guiding — not standing beside the diagram. Keep it clean, warm, sparse, hand-drawn, and not childish. Keep 泡泡's appearance matching the reference sheet.
```
