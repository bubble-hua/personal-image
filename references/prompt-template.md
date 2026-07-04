# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

## 角色参考图

**泡泡的官方形象设定图（reference sheet）位于：**
`assets/reference-sheet-bubble.png`

**重要提示**：ImageGen 的 image-to-image 模式不可用，因此**每次生图都使用纯文字精确描述**来确保泡泡形象一致。以下角色描述是从参考图中提取的视觉特征，必须严格遵守。

**从参考图和真人照片提取的精确特征（必须匹配）：**
- 头身比：**2.5 头身** chibi Q 版
- **发型（核心特征！）：深棕色酷酷的利落短发**（偏分，长度到下巴/耳下，有层次感，蓬松有厚度，干净利落带酷感。参考Q版形象设定图的三视角——正视图/侧视图/后视图）。薄侧分刘海。填充色 `#5D4037`。
- 脸型：鹅蛋脸偏长（参考真人），脸颊微圆，有粉色腮红
- **眼镜（核心标识！）：圆框近视眼镜（有透明镜片）**——这是泡泡最标志性的特征，默认必须佩戴！偶尔可用圆框墨镜做酷飒切换，但默认是戴眼镜。
- 眼睛：超大圆眼（占面部 1/3+），深棕色瞳孔，有高光点，眼睫毛清晰。笑眼弯弯是标志性表情。
- 鼻子：极小几乎不画或一个小点
- 嘴唇：小嘴，温暖灿烂的笑容（标志性！）
- 肤色：暖肤色 `#FFE0BD`
- 身材：小巧 chibi 身形，手脚圆润不尖锐
- 标准穿搭：宽松白衬衫（袖子挽起）+ 暖卡其阔腿裤 + 白色帆布鞋（无背包）
- 整体画风：日系 Q 版手绘风，**彩色铅笔线条质感**，线条清晰饱和度高，角色有饱满鲜亮的色块填充

---

## 标准 Prompt 模板（精简版 — 推荐使用）

经过多轮测试验证，精简版 prompt 效果更好——过长的 prompt 会导致内容偏差。以下为经过验证的成功模板结构：

```text
Colored pencil hand-drawn illustration, picture book style. **A square image (1024x1024) with a HORIZONTAL LETTERBOX composition.** The top 224 pixels and the bottom 224 pixels are PURE WHITE (#FFFFFF) — completely empty, no content at all. The illustration ONLY exists in the middle 576-pixel-high horizontal band. **This middle band should be FULL and RICH with content — use ALL of this 1024x576 space!**

Character: 泡泡(Bubble), refined Japanese chibi, **2.5 heads tall**. **Dark brown cool SHORT hair** (NOT long/wavy! NOT shoulder-length! clean stylish SHORT bob, length to chin/ear, side-swept bangs, volume, layered). **Round-frame glasses with clear lenses** (always wearing — signature!). Warm bright smile. Huge round eyes (half face) with sparkle highlights and long lashes. Round cheeks, pink blush. Wearing: ivory white shirt + camel khaki wide-leg pants + white sneakers. NO backpack.

SCENE: {具体场景描述，泡泡在哪里、在做什么、动作姿态}

Elements: {关键视觉元素，用英文列出}. **Fill the entire middle band with rich content: character on one side, diagram/concept/mindmap on the other side, handwritten Chinese labels, arrows, decorative elements. Don't leave large empty spaces!**

Colors: Lake blue #6DA4BA outlines with visible colored pencil texture (NOT digital vector, NOT soft airbrush). Hair #5D4037. Skin #FFE0BD. Pants #C9A86C. Shirt #FFF8E7. Arrow #E8D478. Circle #E8AC98. Leaf #88B880. Background pure white #FFFFFF.

Line quality: **Lines should be clear and legible, with enough definition to read easily, but still light, airy, and natural — like gentle but confident colored pencil marks. NOT thick heavy lines. NOT dark or black. CRITICAL COMPOSITION RULE — LETTERBOX:** The top and bottom 224px of this square image are pure white empty letterbox bars. All content is inside the middle 576px band only.

50%+ empty white space overall (within the middle band). Only {3-5} text labels max. No title.
```

**变量说明：**
- `{具体场景描述}`：泡泡的动作、位置、与环境的关系。必须大写强调关键约束（如 "NOT stairs, NOT steps"）
- `{关键视觉元素}`：图中有哪些物件、标注、箭头、路径等
- `{3-5}`：标注文字数量上限
- **注意：泡泡的发型固定为酷酷的利落短发（参考Q版设定图三视角），眼镜默认佩戴圆框近视眼镜。不要在每张图中切换这些基础特征。**

**场景描述编写要点：**
- 用英文大写强调否定约束，如：`Bubble is placing a rectangular BRICK on the ground. The bricks form a PATH — NOT stairs, NOT steps. Just flat bricks laid on the ground.`
- 明确泡泡的位置（left/right/center）和姿态（kneeling/squatting/standing/sitting）
- 明确物体的空间关系
- **⚠️ 16:9 Letterbox 安全区约束（核心构图规则）**：使用 "HORIZONTAL LETTERBOX composition" 描述方式——明确要求正方形画布的顶部 224px 和底部 224px 完全纯白空白（#FFFFFF），所有内容只在中间 576px 横向区域内生成。不要在上下留白区域放置任何元素。中间区域必须充分利用——角色 + 图表/概念图 + 中文标注 + 箭头 + 装饰元素，铺满整个 1024×576 的空间。

---

## 完整版 Prompt 模板（需要更多细节时使用）

当精简版无法精确控制画面时，使用以下完整模板：

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background (#FFFFFF). **Colored pencil hand-drawn illustration style** with high-saturation outlines — all lines are crisp, vivid, and clearly visible like real colored pencil strokes on white paper. Picture book / children's book illustration aesthetic. Lake blue (#6DA4BA) line art for all outlines. **Characters have BRIGHT WARM FILL COLORS inside the outlines** — this is NOT a bare line sketch! Lots of empty white space. Sparse handwritten Chinese annotations in cream yellow (#E8D478) for flow paths, shell pink (#E8AC98) for key highlights, and mint green (#88B880) for supplementary notes. Clean warm healing feeling — like a colorful chibi character illustration drawn with colored pencils. The overall look should be vivid, luminous, and warm with **clear visible pencil stroke texture**. No gradients, no shadows, no paper texture (pure white bg), no complex background, no commercial vector style.

Recurring IP character (match reference sheet AND real photos exactly):
泡泡 (Bubble) — a **2.5-heads-tall** chibi Q-version character with BRIGHT WARM FILL COLORS. CRITICAL UNIQUE FEATURES: **dark brown cool SHORT hair** (NOT long/wavy! clean stylish short bob with side-swept bangs, volume to chin/ear, layered — match the reference sheet's three-view exactly) — filled with `#5D4037` dark warm brown; round-oval face (slightly elongated like the real person) with soft cheeks filled with warm skin tone `#FFE0BD`; very large round eyes (1/3+ of face) with dark brown pupils, highlight dots, and **warm bright smile**; tiny nose; small mouth; **round-frame glasses with CLEAR LENSES** (always wearing — this is her signature identifier!); small rounded chibi body. Standard outfit: loose white/ivory shirt `#FFF8E7` with rolled-up sleeves + warm khaki wide-leg pants `#C9A86C` + white canvas shoes. NO backpack. Lake blue `#6DA4BA` outlines everything with **high-saturation colored-pencil texture**. Bubble looks like a vivid colorful chibi character drawn with colored pencils, not a digital vector or soft airbrush style.
In this illustration, show Bubble in action pose — {具体动作描述}. She is wearing her **signature round glasses** and has her **warm bright smile**. Bubble participates actively.

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
Lake blue (#6DA4BA) for ALL line art outlines (character, objects, structures) — **lines must be high-saturation, crisp, and clearly visible with colored pencil texture**. Bubble's fill colors: hair #5D4037 dark warm brown (cool short bob style, NOT long/wavy), skin #FFE0BD warm tone, shirt #FFF8E7 ivory white, pants #C9A86C warm khaki. Cream yellow (#E8D478) for main flow/path/arrows. Shell pink (#E8AC98) only for key highlights, warnings, or results. Mint green (#88B880) only for secondary notes. The illustration should feel VIVID, WARM, and LUMINOUS with **colored pencil hand-drawn texture and clear visible outlines** — like a colorful chibi comic drawn with real colored pencils on white paper. Do NOT use pure black for lines.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. **CRITICAL COMPOSITION — LETTERBOX LAYOUT:** This is a 1024x1024 square image with HORIZONTAL LETTERBOX composition. The top 224 pixels and bottom 224 pixels are PURE WHITE #FFFFFF — completely empty, no content at all. All illustration content exists ONLY in the middle 576-pixel-high horizontal band, and this band must be FULL and RICH with content (character + diagram/flowchart + Chinese labels + arrows + decorative elements). Use the entire middle band space! Preserve at least 35% blank white space within the middle band. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, warm but not childish, artsy but not pretentious. Bubble must be the active participant, not decoration. **Bubble's appearance: cool short dark brown hair (NEVER long/wavy — match reference sheet three-view!), round-frame glasses with clear lenses (ALWAYS wearing — signature feature!), warm bright smile.** Pure white background — no tint, no cream, no blue-grey.
**Line quality: Lines should be clear and legible with enough definition to read easily, but still light, airy, and natural — like gentle but confident colored pencil marks. NOT thick heavy lines. NOT dark or black.**
```

---

## 后处理（两步：先裁剪 16:9，再智能刷白背景）

**⚠️ 最终输出比例必须严格为 16:9 横版。**

ImageGen 仅支持 1024x1024 正方形输出，因此每次生图后需要两步后处理：

### 第1步：裁剪为 16:9

```bash
python3.11 scripts/crop_16_9.py <原始生成图> <裁剪后中间图>
```

裁剪脚本从正方形图片的中心区域裁剪为 16:9 横版（1024x576），移除上下各 224px 的 letterbox 留白区域。

### 第2步：智能刷白背景

```bash
python3.11 scripts/smart_whiten_bg.py <裁剪后中间图> <最终输出图> 30 28 150
```

智能刷白脚本使用 Color Key + Uniform Gray 双重检测算法清除残留灰色背景。默认参数 `30 28 150`（距离阈值/均匀灰偏差/最小亮度）。

**完整示例：**
```bash
python3.11 scripts/crop_16_9.py raw_output.png cropped.png
python3.11 scripts/smart_whiten_bg.py cropped.png final_output.png 30 28 150
```

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
