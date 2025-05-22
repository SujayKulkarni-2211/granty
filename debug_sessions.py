# debug_sections.py - Run this to check your templates and sections

import os
import json
import storage

def debug_sections():
    print("=== DEBUGGING SECTIONS ISSUE ===\n")
    
    # Check if directories exist
    print("1. Checking directory structure:")
    dirs = ['data', 'data/templates', 'data/drafts']
    for dir_path in dirs:
        exists = os.path.exists(dir_path)
        print(f"   {dir_path}: {'✓ EXISTS' if exists else '✗ NOT FOUND'}")
        if exists and os.path.isdir(dir_path):
            files = os.listdir(dir_path)
            print(f"      Files: {files}")
    print()
    
    # Check templates
    print("2. Checking templates:")
    try:
        templates = storage.get_templates()
        print(f"   Found {len(templates)} templates")
        
        for i, template in enumerate(templates):
            print(f"\n   Template {i+1}:")
            print(f"      ID: {template.get('id', 'NO ID')}")
            print(f"      Name: {template.get('name', 'NO NAME')}")
            print(f"      Sections: {len(template.get('sections', []))}")
            
            # Check first section details
            sections = template.get('sections', [])
            if sections:
                first_section = sections[0]
                print(f"      First section:")
                print(f"         Title: {first_section.get('title', 'NO TITLE')}")
                print(f"         Questions: {len(first_section.get('questions', []))}")
                
                # Check first question
                questions = first_section.get('questions', [])
                if questions:
                    first_q = questions[0]
                    print(f"         First question: {first_q.get('text', 'NO TEXT')[:50]}...")
            else:
                print("      ✗ NO SECTIONS FOUND IN TEMPLATE!")
                
    except Exception as e:
        print(f"   ✗ ERROR getting templates: {e}")
    print()
    
    # Check drafts
    print("3. Checking drafts:")
    try:
        drafts = storage.get_drafts()
        print(f"   Found {len(drafts)} drafts")
        
        for i, draft in enumerate(drafts):
            print(f"\n   Draft {i+1}:")
            print(f"      ID: {draft.get('id', 'NO ID')}")
            print(f"      Title: {draft.get('title', 'NO TITLE')}")
            print(f"      Template ID: {draft.get('template_id', 'NO TEMPLATE ID')}")
            print(f"      Sections: {len(draft.get('sections', []))}")
            
            if not draft.get('sections'):
                print("      ✗ NO SECTIONS IN DRAFT!")
                
    except Exception as e:
        print(f"   ✗ ERROR getting drafts: {e}")
    print()
    
    # Initialize templates if needed
    print("4. Checking if templates need initialization:")
    if not os.path.exists('data/templates') or len(os.listdir('data/templates')) == 0:
        print("   Initializing default templates...")
        try:
            storage.initialize_default_templates()
            print("   ✓ Templates initialized successfully")
        except Exception as e:
            print(f"   ✗ ERROR initializing templates: {e}")
    else:
        print("   Templates directory exists and has files")
    print()
    
    print("=== DEBUG COMPLETE ===")
    print("\nIf you see errors above, those might be causing your sections issue.")
    print("Make sure your Flask app is loading templates properly on startup.")

if __name__ == "__main__":
    debug_sections()