# blog

Personal blog of Anas Zokronain: structural engineering, BIM, Revit and construction technology.

Built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com). Hosted free on GitHub Pages.

## Write a new post with Pages CMS (easiest on a phone)

1. Open [app.pagescms.org](https://app.pagescms.org) in Safari and sign in with GitHub.
2. Pick the **blog** repo, then **Blog posts → Add an entry**.
3. Fill in the form. New posts start as **Draft**, so they stay hidden.
4. Tap **Save**. When ready to publish, switch **Draft** off and save again.

The editor settings live in `.pages.yml`.

## Write a new post in GitHub (manual way)

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
