# blog

Personal blog of Anas Zokronain: structural engineering, BIM, Revit and construction technology.

Built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com). Hosted free on GitHub Pages.

## Write a new post (from your phone)

1. Open this repo on GitHub in Safari (or the GitHub app).
2. Go to `src/content/blog/`.
3. Tap **Add file → Create new file**. Name it like `my-new-post.md` (lowercase, no spaces). The file name becomes the web address.
4. Paste this at the top, then write your post below it in Markdown:

   ```markdown
   ---
   title: My new post
   description: One sentence summary.
   date: 2026-11-01
   tags: [revit, bim]
   ---

   Your text here.
   ```

5. Tap **Commit changes**. The site rebuilds itself in about 2 minutes.

Set `draft: true` in the top section to hide a post without deleting it.

## Change your details

Edit `src/config.ts` (name, role, email, LinkedIn, GitHub).

## Where things are

| File or folder | What it is |
|---|---|
| `src/config.ts` | Your name, email and links |
| `src/content/blog/` | Blog posts (one Markdown file each) |
| `src/pages/index.astro` | About page (home) |
| `src/pages/blog/` | Blog list and single post pages |
| `src/pages/contact.astro` | Contact page |
| `src/styles/global.css` | Colors and the frosted glass look |
| `.github/workflows/deploy.yml` | Automatic build and publish |
