# 🧱 Bubbletea Components Reference

This page documents the built-in UI components available in the `bubbletea_chat` package. These components allow your bot to communicate with users in rich, interactive formats.

---

## 📄 Text & Rich Display

### `bt.Text`

Plain text message from the bot.

```python
bt.Text(content: str)
```

**Example:**
```python
yield bt.Text("Hello! How can I help you today?")
```

---

### `bt.Markdown`

Supports bold, italics, lists, links, etc.

```python
bt.Markdown(content: str)
```

**Example:**
```python
yield bt.Markdown("**Welcome!**\nHere’s a [link](https://example.com).")
```

---

### `bt.Code`

Renders syntax-highlighted code blocks.

```python
bt.Code(code: str, language: str = "python")
```

**Example:**
```python
yield bt.Code("print('Hello, world!')", language="python")
```

---

### `bt.Error`

Visually styled error message (e.g., red box).

```python
bt.Error(message: str)
```

**Example:**
```python
yield bt.Error("Something went wrong. Please try again.")
```

---

### `bt.RichLink`

Displays a preview of a link with metadata.

```python
bt.RichLink(url: str)
```

**Example:**
```python
yield bt.RichLink("https://openai.com")
```

---

## 🎛️ Interaction Components

### `bt.Buttons`

Clickable button choices.

```python
bt.Buttons(buttons: List[str])
```

**Example:**
```python
yield bt.Text("Would you like to continue?")
yield bt.Buttons(["Yes", "No"])
```

---

### `bt.Pills`

Horizontally stacked pill-style options.

```python
bt.Pills(options: List[str])
```

**Example:**
```python
yield bt.Text("When works best?")
yield bt.Pills(["Today", "Tomorrow", "Next week"])
```

---

### `bt.Cards`

Carousel cards with image, title, description, and buttons.

```python
bt.Cards(cards: List[bt.Card])
```

Each card is:

```python
bt.Card(
    title: str,
    description: str = "",
    image_url: str = "",
    buttons: List[str] = []
)
```

**Example:**
```python
yield bt.Cards([
    bt.Card(
        title="Joe's Pizza",
        description="Famous NY slices",
        image_url="https://picsum.photos/seed/pizza/300/200",
        buttons=["View Menu", "Order Now"]
    ),
    bt.Card(
        title="Sushi Spot",
        description="Fresh fish, daily",
        image_url="https://picsum.photos/seed/sushi/300/200",
        buttons=["Reserve", "Details"]
    )
])
```

---

### `bt.Table`

Renders tabular data.

```python
bt.Table(columns: List[str], rows: List[List[str]])
```

**Example:**
```python
yield bt.Table(
    columns=["Task", "Status"],
    rows=[
        ["Walk the dog", "✅ Done"],
        ["Buy milk", "⏳ Pending"]
    ]
)
```

---

### `bt.FileUpload`

Allows the user to upload a file.

```python
bt.FileUpload(prompt: str = "Upload a file")
```

**Example:**
```python
yield bt.FileUpload("Please upload a CSV file to analyze:")
```

---

## 🖼️ Media Components

### `bt.Image`

Displays an image inline.

```python
bt.Image(url: str, alt: str = None)
```

**Example:**
```python
yield bt.Image("https://picsum.photos/400/300", alt="Random image")
```

---

### `bt.Video`

Embeds a video player.

```python
bt.Video(url: str)
```

**Example:**
```python
yield bt.Video("https://example.com/video.mp4")
```

---

### `bt.Audio`

Embeds an audio player.

```python
bt.Audio(url: str)
```

**Example:**
```python
yield bt.Audio("https://example.com/audio.mp3")
```

---

### `bt.YouTubeVideo`

Embeds a YouTube video player.

```python
bt.YouTubeVideo(video_id: str)
```

**Example:**
```python
yield bt.YouTubeVideo("dQw4w9WgXcQ")
```

---

## 🔧 Misc

### `bt.Divider`

Visual separator between sections.

```python
bt.Divider()
```

**Example:**
```python
yield bt.Text("Step 1: Upload your resume")
yield bt.Divider()
yield bt.Text("Step 2: Answer some questions")
```

---

## 💬 Usage Notes

- Use `yield` to return each component from your bot’s generator.
- Each component renders as a separate message in the UI.
- You can mix and match components in a single response.

---
