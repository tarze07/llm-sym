# -*- coding: utf-8 -*-
"""
Build script to assemble index.html for the METR Hugging Face Incident Simulation.
"""

import json
import os
from data_events import (
    TIMELINE_MILESTONES,
    HISTORICAL_MESSAGES,
    AGENT_PROFILES,
    ATTACK_STAGES,
    TOOL_SPOOFING_TECHNIQUES,
    WHAT_IF_SCENARIOS
)
from styles import CSS_STYLES
from templates import HTML_TEMPLATE
from scripts_js import JS_CODE

def main():
    print("Assembling simulation index.html...")
    
    # Format data injection into JavaScript
    injected_data = f"""
    window.DATA_MILESTONES = {json.dumps(TIMELINE_MILESTONES, ensure_ascii=False, indent=2)};
    window.DATA_MESSAGES = {json.dumps(HISTORICAL_MESSAGES, ensure_ascii=False, indent=2)};
    window.DATA_PROFILES = {json.dumps(AGENT_PROFILES, ensure_ascii=False, indent=2)};
    window.DATA_ATTACK_STAGES = {json.dumps(ATTACK_STAGES, ensure_ascii=False, indent=2)};
    window.DATA_SPOOF_METHODS = {json.dumps(TOOL_SPOOFING_TECHNIQUES, ensure_ascii=False, indent=2)};
    window.DATA_WHAT_IF = {json.dumps(WHAT_IF_SCENARIOS, ensure_ascii=False, indent=2)};
    """
    
    full_js = injected_data + "\n" + JS_CODE
    
    final_html = HTML_TEMPLATE.format(
        css_content=CSS_STYLES,
        js_content=full_js
    )
    
    out_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Successfully generated {out_path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
