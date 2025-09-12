#!/bin/bash
set -e

echo "Starting Jekyll build process..."
echo "Ruby version: $(ruby -v)"
echo "Bundler version: $(bundle -v)"

# Install dependencies
echo "Installing dependencies..."
bundle install --frozen

# Build the site
echo "Building Jekyll site..."
bundle exec jekyll build

echo "Build completed successfully!"