// All your personal details live here. Edit this one file to update the whole site.
export const SITE = {
  name: 'Anas Zokronain',
  title: 'Anas Zokronain | Structural, BIM and Construction Tech',
  description:
    'Structural and BIM engineer bridging construction technology and buildings. Notes on Revit, automation, and AEC tech.',
  role: 'Structural Engineer · BIM Engineer',
  email: 'anaszok.work@gmail.com',
  linkedin: '',
  github: 'https://github.com/anaszok',
};

// Turns a path like "/contact" into "/blog/contact" so links work on GitHub Pages.
export function url(path = '/') {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  return `${base}${path.startsWith('/') ? path : `/${path}`}`;
}
