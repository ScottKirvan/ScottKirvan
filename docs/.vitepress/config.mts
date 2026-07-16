import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "ScottKirvan",
  description: "TODO: Replace with your project description.",
  base: '/ScottKirvan/',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'GitHub', link: 'https://github.com/ScottKirvan/ScottKirvan' }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ScottKirvan/ScottKirvan' },
      { icon: 'discord', link: 'https://discord.gg/TN6XJSNK5Y' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © Scott Kirvan'
    }
  }
})
