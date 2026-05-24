import os

strat_file = "/home/nauman/Desktop/desk/MUN/Helping material/japan_unsc_strategy.html"
prep_file = "/home/nauman/Desktop/desk/MUN/Helping material/japan_unsc_hormuz_mun_prep.html"
out_file = "/home/nauman/Desktop/desk/MUN/Helping material/japan_unsc_merged_hub.html"

with open(strat_file, 'r', encoding='utf-8') as f:
    strat = f.read()
with open(prep_file, 'r', encoding='utf-8') as f:
    prep = f.read()

# Extract styles and bodies
strat_style = strat.split('<style>')[1].split('</style>')[0]
strat_body = strat.split('<body>')[1].split('<script>')[0]

prep_style = prep.split('<style>')[1].split('</style>')[0]
prep_body = prep.split('</style>')[1].split('<script>')[0]

# Scope strat CSS
strat_style = strat_style.replace('body {', '.strat-wrapper {')
strat_style = strat_style.replace('html {', '/* html */ {')
strat_style = strat_style.replace('* {', '.strat-wrapper * {')
strat_style = strat_style.replace('h2 {', '.strat-wrapper h2 {')

# Scope prep CSS
prep_style = prep_style.replace('body{', '.prep-wrapper{')
prep_style = prep_style.replace('*{', '.prep-wrapper *{')
prep_style = prep_style.replace('h2{', '.prep-wrapper h2{')
prep_style = prep_style.replace('h3{', '.prep-wrapper h3{')
prep_style = prep_style.replace('p,li{', '.prep-wrapper p, .prep-wrapper li{')
prep_style = prep_style.replace('ul{', '.prep-wrapper ul{')
prep_style = prep_style.replace('ul li{', '.prep-wrapper ul li{')

# Rename intersecting classes
# Both use .card
prep_style = prep_style.replace('.card{', '.prep-card{')
prep_body = prep_body.replace('class="card"', 'class="prep-card"')

# Rename show() functions
strat_body = strat_body.replace('show(', 'showStrat(')
prep_body = prep_body.replace('show(', 'showPrep(')

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🇯🇵 Japan UNSC — Unified Hub</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
/* --- HUB STYLES --- */
:root {{
    --hub-bg: #f8fafc;
    --hub-text: #0f172a;
    --hub-accent: #3b82f6; /* Matching Japan's blue badge */
}}
body {{
    margin: 0; padding: 0;
    font-family: 'Inter', sans-serif;
    background: var(--hub-bg);
    color: var(--hub-text);
}}

.hub-header-main {{
    background: #080c14;
    padding: 1.5rem 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}}

.hub-title-container {{
    display: flex;
    align-items: center;
    gap: 1rem;
}}

.hub-flag {{
    width: 48px; height: 48px;
    border-radius: 50%;
    background: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
    box-shadow: 0 0 0 2px #bc002d, 0 0 20px rgba(188,0,45,0.4);
}}

.hub-title-container h1 {{
    font-family: 'Syne', sans-serif;
    font-size: 22px; font-weight: 800;
    letter-spacing: -0.02em;
    color: #e8edf5;
    margin: 0;
}}

.hub-tabs {{
    display: flex;
    gap: 0.5rem;
    background: rgba(255,255,255,0.05);
    padding: 6px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}}

.hub-btn {{
    padding: 10px 24px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    background: transparent;
    color: #8a9bb8;
    transition: all 0.2s;
    font-family: 'Syne', sans-serif;
}}

.hub-btn:hover:not(.active) {{
    background: rgba(255,255,255,0.05);
    color: #fff;
}}

.hub-btn.active {{
    background: var(--hub-accent);
    color: white;
    box-shadow: 0 4px 12px rgba(59,130,246,0.3);
}}

.hub-section {{
    display: none;
}}

.hub-section.active {{
    display: block;
    animation: fadeInHub 0.3s ease;
}}

@keyframes fadeInHub {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}

/* --- STRATEGY STYLES --- */
{strat_style}

.strat-wrapper {{
    /* Ensure the strategy section takes up full height and correctly displays its dark theme */
    background: #080c14; 
    color: #e8edf5;
    padding-bottom: 3rem;
}}

/* --- PREP STYLES --- */
:root {{
    --font-sans: 'Inter', sans-serif;
    --color-background-primary: #ffffff;
    --color-background-secondary: #f8fafc;
    --color-background-tertiary: #f1f5f9;
    --color-border-secondary: #cbd5e1;
    --color-border-tertiary: #e2e8f0;
    --color-text-primary: #0f172a;
    --color-text-secondary: #334155;
    --color-text-tertiary: #64748b;
    --border-radius-md: 8px;
    --border-radius-lg: 12px;
}}
{prep_style}

.prep-wrapper {{
    background: #ffffff;
    padding: 2rem;
    max-width: 1100px;
    margin: 2rem auto;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border: 1px solid #e2e8f0;
}}

@media (max-width: 600px) {{
    .hub-header-main {{ padding: 1rem; }}
    .prep-wrapper {{ padding: 1.25rem 1rem; margin: 1rem; }}
}}
</style>
</head>
<body>

<div class="hub-header-main">
    <div class="hub-title-container">
        <div class="hub-flag">🇯🇵</div>
        <h1>Japan — UNSC Master Hub</h1>
    </div>
    <div class="hub-tabs">
        <button class="hub-btn active" onclick="showHub('strat')">🌍 Strategy & Room Control</button>
        <button class="hub-btn" onclick="showHub('prep')">📚 MUN Prep & Speeches</button>
    </div>
</div>

<div id="strat-section" class="hub-section active">
    <div class="strat-wrapper">
        {strat_body}
    </div>
</div>

<div id="prep-section" class="hub-section">
    <div class="prep-wrapper">
        {prep_body}
    </div>
</div>

<script>
// Master Hub Navigation
function showHub(id) {{
    document.querySelectorAll('.hub-section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.hub-btn').forEach(b => b.classList.remove('active'));
    
    document.getElementById(id + '-section').classList.add('active');
    event.target.classList.add('active');
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Strategy Tabs (Fixing the shifting bug by robustly matching elements without relying on exact index arrays)
function showStrat(id) {{
    // Hide all strategy panels
    document.querySelectorAll('.strat-wrapper .panel').forEach(p => p.classList.remove('active'));
    // Remove active state from all strategy buttons
    document.querySelectorAll('.strat-wrapper .tbtn').forEach(b => b.classList.remove('active'));
    
    // Show the target panel
    const targetPanel = document.getElementById(id);
    if(targetPanel) {{
        targetPanel.classList.add('active');
    }}
    
    // Find the corresponding top navigation button and make it active
    const buttons = Array.from(document.querySelectorAll('.strat-wrapper .tbtn'));
    const targetBtn = buttons.find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes("showStrat('" + id + "')"));
    if(targetBtn) {{
        targetBtn.classList.add('active');
    }}
    
    // Scroll to the panel slightly below the sticky header
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

// Prep Tabs Navigation
function showPrep(id) {{
    // Hide all prep tabs
    document.querySelectorAll('.prep-wrapper .tab').forEach(t => t.classList.remove('active'));
    // Remove active state from all prep nav buttons
    document.querySelectorAll('.prep-wrapper .nav button').forEach(b => b.classList.remove('active'));
    
    // Show the target tab
    const targetTab = document.getElementById(id);
    if(targetTab) {{
        targetTab.classList.add('active');
    }}
    
    // Find the clicked button and make it active
    const buttons = Array.from(document.querySelectorAll('.prep-wrapper .nav button'));
    const targetBtn = buttons.find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes("showPrep('" + id + "')"));
    if(targetBtn) {{
        targetBtn.classList.add('active');
    }}
}}
</script>
</body>
</html>
"""

# Strip out the duplicated header from strat_body since we have a master header now
html_template = html_template.replace('<div class="header">', '<div class="header" style="display:none;">')

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html_template)
print("Merge complete!")
