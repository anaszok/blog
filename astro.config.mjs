// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';

// GitHub Actions passes BASE_PATH (for example "/blog") when it builds.
// On a local build it falls back to the repo name.
const base = process.env.BASE_PATH || '/blog';

export default defineConfig({
  site: 'https://anaszok.github.io',
  base,
  integrations: [sitemap()],
  markdown: {
    shikiConfig: { theme: 'github-dark-dimmed', wrap: false },
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
