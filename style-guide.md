# Farm-to-Table Design System — Style Guide

A warm, organic design system built with **Tailwind CSS v4**, **shadcn/ui** (new-york style), and **oklch** color tokens.

---

## 1. Tech Stack

| Layer | Tool |
|---|---|
| Styling | Tailwind CSS v4 (`@import "tailwindcss"` + `@theme inline`) |
| Components | shadcn/ui — style: `new-york`, base color: `slate`, CSS variables: yes |
| Icons | `lucide-react` |
| Utilities | `class-variance-authority`, `clsx`, `tailwind-merge`, `tw-animate-css` |
| Fonts | Fraunces (display) + Inter (body) via Google Fonts |

---

## 2. Color Palette (oklch)

### Light Mode — Warm farm-to-table

| Token | oklch | ~Hex | Use |
|---|---|---|---|
| `--cream` / `--background` | `oklch(0.972 0.018 90)` | `#F8F4E9` | Page background |
| `--foreground` | `oklch(0.22 0.025 75)` | `#3A322A` | Body text |
| `--card` | `oklch(0.99 0.012 90)` | `#FDFAF1` | Card surface |
| `--primary` / `--forest` | `oklch(0.36 0.06 150)` | `#2F5A3F` | Deep forest green |
| `--primary-foreground` | `oklch(0.98 0.012 90)` | `#FBF7EC` | Text on primary |
| `--secondary` | `oklch(0.93 0.025 90)` | `#EDE6D3` | Subtle surface |
| `--muted` | `oklch(0.93 0.02 85)` | `#ECE5D2` | Muted bg |
| `--muted-foreground` | `oklch(0.45 0.02 75)` | `#776B5C` | Muted text |
| `--accent` / `--harvest` | `oklch(0.72 0.16 55)` | `#D9883E` | Harvest orange CTA |
| `--accent-foreground` | `oklch(0.99 0.01 90)` | `#FDFAF1` | Text on accent |
| `--destructive` | `oklch(0.55 0.22 27)` | `#C9412B` | Errors |
| `--border` / `--input` | `oklch(0.88 0.025 85)` | `#E0D8C7` | Borders |
| `--ring` | `oklch(0.36 0.06 150)` | `#2F5A3F` | Focus ring |

### Dark Mode

| Token | oklch |
|---|---|
| `--background` | `oklch(0.18 0.02 140)` |
| `--foreground` | `oklch(0.96 0.015 90)` |
| `--card` | `oklch(0.22 0.025 145)` |
| `--primary` / `--forest` | `oklch(0.75 0.1 145)` |
| `--accent` / `--harvest` | `oklch(0.72 0.16 55)` |
| `--border` | `oklch(1 0 0 / 10%)` |
| `--input` | `oklch(1 0 0 / 15%)` |

### Chart Colors
```
--chart-1: oklch(0.36 0.06 150)   /* forest */
--chart-2: oklch(0.72 0.16 55)    /* harvest */
--chart-3: oklch(0.6 0.12 130)    /* sage */
--chart-4: oklch(0.55 0.1 60)     /* amber */
--chart-5: oklch(0.45 0.08 100)   /* olive */
```

---

## 3. Gradients & Shadows

```css
--gradient-hero: linear-gradient(135deg,
  oklch(0.36 0.06 150 / 0.85),
  oklch(0.28 0.05 140 / 0.65));

--gradient-warm: linear-gradient(135deg,
  oklch(0.72 0.16 55),
  oklch(0.65 0.15 40));

--shadow-soft: 0 10px 40px -15px oklch(0.36 0.06 150 / 0.25);
--shadow-warm: 0 12px 30px -12px oklch(0.72 0.16 55 / 0.35);
```

---

## 4. Typography

```css
--font-display: "Fraunces", ui-serif, Georgia, serif;  /* h1–h4 */
--font-sans:    "Inter",   ui-sans-serif, system-ui;   /* body  */
```

Headings get `letter-spacing: -0.01em`. Selection uses harvest orange.

**Google Fonts link:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## 5. Radius Scale

```
--radius:      0.75rem  (12px)  ← base
--radius-sm:   8px
--radius-md:   10px
--radius-lg:   12px
--radius-xl:   16px
--radius-2xl:  20px
--radius-3xl:  24px
--radius-4xl:  28px
```

---

## 6. Animations & Utilities

| Class | Effect |
|---|---|
| `.lift` | Hover translateY(-6px) + soft shadow |
| `.kenburns` | Scales 1 → 1.08 on parent `.group:hover` |
| `.animate-float` | 5s gentle vertical bob |
| `.animate-hero-zoom` | 14s slow zoom-in (hero images) |
| `.animate-marquee` | 30s infinite horizontal scroll |
| `[data-reveal]` | Fade + translate on scroll. Variants: `scale`, `left`, `right`. Toggle with `data-revealed="true"` |

All animations respect `prefers-reduced-motion: reduce`.

---

## 7. Complete `src/styles.css`

```css
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

@theme inline {
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --radius-2xl: calc(var(--radius) + 8px);

  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-cream: var(--cream);
  --color-harvest: var(--harvest);
  --color-forest: var(--forest);

  --font-display: "Fraunces", ui-serif, Georgia, serif;
  --font-sans: "Inter", ui-sans-serif, system-ui, sans-serif;
}

:root {
  --radius: 0.75rem;

  --cream: oklch(0.972 0.018 90);
  --background: oklch(0.972 0.018 90);
  --foreground: oklch(0.22 0.025 75);
  --card: oklch(0.99 0.012 90);
  --card-foreground: oklch(0.22 0.025 75);
  --popover: oklch(0.99 0.012 90);
  --popover-foreground: oklch(0.22 0.025 75);
  --primary: oklch(0.36 0.06 150);
  --primary-foreground: oklch(0.98 0.012 90);
  --secondary: oklch(0.93 0.025 90);
  --secondary-foreground: oklch(0.28 0.04 150);
  --muted: oklch(0.93 0.02 85);
  --muted-foreground: oklch(0.45 0.02 75);
  --accent: oklch(0.72 0.16 55);
  --accent-foreground: oklch(0.99 0.01 90);
  --harvest: oklch(0.72 0.16 55);
  --forest: oklch(0.36 0.06 150);
  --destructive: oklch(0.55 0.22 27);
  --destructive-foreground: oklch(0.98 0.01 90);
  --border: oklch(0.88 0.025 85);
  --input: oklch(0.88 0.025 85);
  --ring: oklch(0.36 0.06 150);

  --gradient-hero: linear-gradient(135deg, oklch(0.36 0.06 150 / 0.85), oklch(0.28 0.05 140 / 0.65));
  --gradient-warm: linear-gradient(135deg, oklch(0.72 0.16 55), oklch(0.65 0.15 40));
  --shadow-soft: 0 10px 40px -15px oklch(0.36 0.06 150 / 0.25);
  --shadow-warm: 0 12px 30px -12px oklch(0.72 0.16 55 / 0.35);
}

.dark {
  --background: oklch(0.18 0.02 140);
  --foreground: oklch(0.96 0.015 90);
  --card: oklch(0.22 0.025 145);
  --primary: oklch(0.75 0.1 145);
  --primary-foreground: oklch(0.18 0.02 140);
  --accent: oklch(0.72 0.16 55);
  --harvest: oklch(0.72 0.16 55);
  --forest: oklch(0.75 0.1 145);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.75 0.1 145);
}

@layer base {
  * { border-color: var(--color-border); }
  html { scroll-behavior: smooth; }
  body {
    background: var(--color-background);
    color: var(--color-foreground);
    font-family: var(--font-sans);
    -webkit-font-smoothing: antialiased;
  }
  h1, h2, h3, h4, .font-display {
    font-family: var(--font-display);
    letter-spacing: -0.01em;
  }
  ::selection { background: var(--harvest); color: var(--harvest-foreground); }
}

@layer utilities {
  [data-reveal] {
    opacity: 0;
    transform: translateY(24px);
    transition: opacity .8s cubic-bezier(.22,1,.36,1), transform .8s cubic-bezier(.22,1,.36,1);
  }
  [data-revealed="true"] { opacity: 1 !important; transform: none !important; }

  .lift { transition: transform .45s cubic-bezier(.22,1,.36,1), box-shadow .45s cubic-bezier(.22,1,.36,1); }
  .lift:hover { transform: translateY(-6px); box-shadow: var(--shadow-soft); }

  @keyframes float-y { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
  .animate-float { animation: float-y 5s ease-in-out infinite; }

  @keyframes hero-zoom { from{transform:scale(1.08)} to{transform:scale(1)} }
  .animate-hero-zoom { animation: hero-zoom 14s ease-out forwards; }

  @keyframes marquee { from{transform:translateX(0)} to{transform:translateX(-50%)} }
  .animate-marquee { animation: marquee 30s linear infinite; }

  @media (prefers-reduced-motion: reduce) {
    [data-reveal], .animate-float, .animate-hero-zoom, .animate-marquee {
      animation: none !important; opacity: 1 !important; transform: none !important;
    }
  }
}
```

---

## 8. Setup in a New VS Code Project

```bash
# 1. Create Vite + React + TS
npm create vite@latest my-app -- --template react-ts
cd my-app

# 2. Install Tailwind v4 + helpers
npm install tailwindcss @tailwindcss/vite tw-animate-css \
  class-variance-authority clsx tailwind-merge lucide-react

# 3. Init shadcn/ui — choose: new-york, slate, CSS vars: yes
npx shadcn@latest init

# 4. Add components as needed
npx shadcn@latest add button card input dialog form
```

Then paste the `styles.css` block above into `src/styles.css` and add the Google Fonts `<link>` to `index.html`.

---

## 9. Usage Rules

- **Never** use raw color classes like `bg-white`, `text-black`. Always use semantic tokens: `bg-background`, `text-foreground`, `bg-primary`, `text-muted-foreground`.
- Use `font-display` for headings, default sans for body.
- Wrap hero/feature images in `.group` and add `.kenburns` to the `<img>` for hover zoom.
- Apply `data-reveal` to sections you want to animate in on scroll.
