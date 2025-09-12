# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
This is a Jekyll-based documentation site using the "Just the Docs" theme about Apple's road to mobile devices. The site is published on GitHub Pages and contains historical documentation about Apple products, particularly the iPod and Apple's transition to mobile computing.

## Commands
- `bundle install` - Install Ruby gem dependencies
- `bundle exec jekyll serve` - Start local development server at localhost:4000
- `bundle exec jekyll build` - Build the site to `_site` directory
- `bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"` - Build for GitHub Pages deployment

## Architecture and Structure

### Jekyll Configuration
- Uses Jekyll 4.3.3 with the Just the Docs theme (version 0.8.2)
- Site configuration in `_config.yml` with title "Apple: Road to Mobile"
- GitHub Pages deployment configured via GitHub Actions workflow

### Content Organization
- `docs/` - Main documentation content organized by product categories
  - `docs/ipod/` - iPod-related articles and documentation
- `index.md` - Homepage with Jekyll front matter
- Content uses Markdown with Jekyll front matter for navigation and metadata

### Theme Customization
- `_includes/` - Custom Jekyll includes and components
  - `components/sidebar.html` - Custom sidebar component
  - `custom_nav_footer.html` - Custom navigation footer
- `_layouts/` - Custom Jekyll layouts extending the theme
- `_sass/` - Custom SCSS styling
  - `custom.scss` - Site-specific styles
  - `vendor/OneDarkJekyll/` - Syntax highlighting theme
- `assets/` - Static assets and additional CSS

### Jekyll Front Matter Structure
Pages use YAML front matter with these common fields:
- `title` - Page title
- `layout` - Layout template (default, home)
- `nav_order` - Navigation ordering
- `has_children` / `has_toc` - Navigation hierarchy
- `year` / `products` - Custom metadata for content organization

### Development Workflow
- Content is written in Markdown files
- Local development uses `bundle exec jekyll serve`
- GitHub Actions automatically builds and deploys to GitHub Pages on push to main
- Ruby 3.3 is used for builds

## GitHub Pages Deployment
The site is automatically deployed to GitHub Pages via GitHub Actions workflow in `.github/workflows/pages.yml`. The workflow:
- Triggers on pushes to main branch
- Sets up Ruby 3.3 environment
- Installs dependencies with bundler
- Builds site with Jekyll
- Deploys to GitHub Pages

## Content Guidelines
- Historical documentation about Apple products and mobile computing evolution
- Articles are organized chronologically and by product category
- Focus on factual historical narrative with detailed context
- Custom CSS available at `assets/custom.css` for styling enhancements