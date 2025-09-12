#!/usr/bin/env python3
"""
Process Apple book content and create Jekyll structure
"""

import re
import os
from pathlib import Path

def extract_year_from_content(content):
    """Extract years from content based on patterns"""
    year_patterns = [
        r'\b(19\d{2})\b',  # 1990s
        r'\b(20\d{2})\b',  # 2000s
        r'\b(19\d{2})-?(20\d{2})\b',  # Range like 1997-2001
    ]
    
    years_found = set()
    for pattern in year_patterns:
        matches = re.findall(pattern, content[:1000])  # Check first 1000 chars
        for match in matches:
            if isinstance(match, tuple):
                years_found.add(f"{match[0]}-{match[1]}")
            else:
                years_found.add(match)
    
    if years_found:
        # Return the most relevant year or range
        if len(years_found) == 1:
            return list(years_found)[0]
        else:
            # Prefer ranges, or the earliest year
            ranges = [y for y in years_found if '-' in y]
            if ranges:
                return ranges[0]
            else:
                return min(years_found)
    
    return None

def extract_products_from_content(content):
    """Extract products mentioned in content"""
    product_keywords = [
        'iPod', 'iPhone', 'iPad', 'iMac', 'MacBook', 'PowerBook', 'Power Macintosh',
        'Newton', 'Apple TV', 'iTunes', 'iLife', 'iMovie', 'iPhoto', 'iDVD', 'GarageBand',
        'Mac OS X', 'Mac OS 9', 'NeXT', 'WebObjects', 'FireWire', 'USB', 'Thunderbolt',
        'Apple Watch', 'AirPods', 'HomePod', 'Final Cut Pro', 'Logic Pro', 'Xcode'
    ]
    
    products_found = []
    content_lower = content[:2000].lower()  # Check first 2000 chars
    
    for product in product_keywords:
        if product.lower() in content_lower:
            products_found.append(product)
    
    return products_found[:5]  # Limit to first 5 products

def extract_people_from_content(content):
    """Extract people mentioned in content"""
    people_keywords = [
        'Steve Jobs', 'Steve Wozniak', 'Jonathan Ive', 'Tim Cook', 'Phil Schiller',
        'Craig Federighi', 'John Sculley', 'Gil Amelio', 'Tony Fadell', 'Scott Forstall',
        'Jony Ive', 'John Rubinstein', 'Jon Rubinstein', 'Walter Isaacson', 'Mike Markkula',
        'Ed Zander', 'Andy Hertzfeld', 'Bill Atkinson', 'Susan Kare'
    ]
    
    people_found = []
    
    for person in people_keywords:
        if person in content[:2000]:  # Check first 2000 chars
            people_found.append(person)
    
    return people_found[:3]  # Limit to first 3 people

def create_slug(title):
    """Create URL-friendly slug from title"""
    # Remove special characters and convert to lowercase
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces with hyphens
    slug = re.sub(r'[-\s]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug

def determine_category(title, content):
    """Determine which category this chapter belongs to"""
    title_lower = title.lower()
    content_lower = content[:1000].lower()
    
    # Define categories based on content
    categories = {
        'ipod': ['ipod', 'music', 'itunes', 'song', 'player', 'portable', 'walkman'],
        'iphone': ['iphone', 'mobile', 'phone', 'cellular', 'smartphone', 'motorola', 'touchscreen'],
        'ipad': ['ipad', 'tablet', 'touch', 'multi-touch', 'newton'],
        'imac': ['imac', 'computer', 'desktop', 'all-in-one', 'bondi', 'usb'],
        'company': ['apple', 'jobs', 'company', 'ceo', 'business', 'strategy', 'return'],
        'technology': ['firewire', 'usb', 'processor', 'operating system', 'mac os', 'next']
    }
    
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower or keyword in content_lower:
                return category
    
    return 'general'

def process_book_content():
    """Process the book content and create Jekyll structure"""
    
    # Read the converted markdown file
    with open('kniha-apple-content.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by chapter headings
    chapters = re.split(r'\n\*\*(.*?)\*\*\n', content)
    
    # Remove empty elements and combine titles with content
    processed_chapters = []
    for i in range(1, len(chapters), 2):  # Skip first element (before first heading)
        if i + 1 < len(chapters):
            title = chapters[i].strip()
            chapter_content = chapters[i + 1].strip()
            
            # Skip very short chapters or table of contents
            if len(chapter_content) > 200 and title.lower() not in ['contents', 'a decade in the spotlight of apple']:
                processed_chapters.append({
                    'title': title,
                    'content': chapter_content
                })
    
    print(f"Found {len(processed_chapters)} chapters to process")
    
    # Create directory structure
    categories_created = set()
    nav_order = 1
    
    for i, chapter in enumerate(processed_chapters):
        title = chapter['title']
        content = chapter['content']
        
        # Determine category and metadata
        category = determine_category(title, content)
        slug = create_slug(title)
        year = extract_year_from_content(content)
        products = extract_products_from_content(content)
        people = extract_people_from_content(content)
        
        # Create category directory if needed
        category_dir = Path(f'docs/{category}')
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Create category index if this is the first chapter in category
        if category not in categories_created:
            categories_created.add(category)
            category_title = {
                'ipod': 'iPod Era',
                'iphone': 'iPhone Revolution', 
                'ipad': 'iPad Innovation',
                'imac': 'iMac Renaissance',
                'company': 'Apple Company',
                'technology': 'Technology & Innovation',
                'general': 'General Topics'
            }.get(category, category.title())
            
            category_index_content = f"""---
layout: default
title: {category_title}
nav_order: {nav_order}
has_children: true
has_toc: true
---

# {category_title}

This section covers the {category_title.lower()} period in Apple's history.
"""
            
            with open(category_dir / 'index.md', 'w', encoding='utf-8') as f:
                f.write(category_index_content)
            
            nav_order += 1
        
        # Prepare front matter
        front_matter = {
            'layout': 'default',
            'title': title,
            'parent': {
                'ipod': 'iPod Era',
                'iphone': 'iPhone Revolution',
                'ipad': 'iPad Innovation', 
                'imac': 'iMac Renaissance',
                'company': 'Apple Company',
                'technology': 'Technology & Innovation',
                'general': 'General Topics'
            }.get(category, category.title()),
            'nav_order': i + 1,
            'has_children': False,
            'has_toc': False
        }
        
        if year:
            front_matter['year'] = year
        if products:
            front_matter['products'] = products
        if people:
            front_matter['people'] = people
        
        # Create YAML front matter manually with proper escaping
        yaml_content = "---\n"
        for key, value in front_matter.items():
            if isinstance(value, list):
                if value:  # Only add if list is not empty
                    yaml_content += f"{key}:\n"
                    for item in value:
                        yaml_content += f"  - {item}\n"
            else:
                # Escape values that contain colons or special characters
                if isinstance(value, str) and (':' in value or '"' in value):
                    escaped_value = value.replace('"', '\\"')
                    yaml_content += f'{key}: "{escaped_value}"\n'
                else:
                    yaml_content += f"{key}: {value}\n"
        yaml_content += "---\n\n"
        
        # Create the markdown file
        file_content = yaml_content
        file_content += f"# {title}\n\n"
        file_content += content.replace('\\', '')  # Remove escape characters
        
        # Write to file
        filename = f"{slug}.md"
        file_path = category_dir / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(file_content)
        
        print(f"Created: {file_path}")
        print(f"  Year: {year}, Products: {products[:2]}, People: {people[:1]}")

if __name__ == "__main__":
    process_book_content()
    print("Book processing completed!")