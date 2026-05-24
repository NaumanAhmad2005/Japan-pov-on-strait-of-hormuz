import os
import re

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

prep_body = prep.split('</style>')[1].split('<script>')[0]

# Remove the duplicated headers
strat_body = re.sub(r'<div class="header">.*?</div>\s*</div>', '', strat_body, flags=re.DOTALL) # wait, header closes after </div></div>? No, header has 3 divs inside.
# Better to just regex out the whole `<div class="header"> ... </div>` exactly
header_match = re.search(r'<div class="header">.*?</div>\s*</div>\s*</div>', strat_body, flags=re.DOTALL)
if not header_match:
    # Try simpler
    strat_body = re.sub(r'<div class="header">.*?</div>\s*</div>\s*</div>', '', strat_body, flags=re.DOTALL)
    # The header in strat: 
    # <div class="header">
    #   <div class="header-flag">🇯🇵</div>
    #   <div class="header-info">...</div>
    #   <div class="header-badges">...</div>
    # </div>
    strat_body = re.sub(r'<div class="header">.*?</div>\s*<div class="tab-bar">', '<div class="tab-bar">', strat_body, flags=re.DOTALL)

# Prep Body translation to Strategy styling
# Remove its manual header banner by splitting on the nav div — everything before
# <div class="nav"> is the outer wrapper + the header block; we discard it and
# reconstruct just the opening <div> wrapper + nav onwards.
nav_split = '<div class="nav">'
if nav_split in prep_body:
    prep_body = '<div>\n\n' + nav_split + prep_body.split(nav_split, 1)[1]
else:
    # Fallback: just strip the padding wrapper div attribute
    prep_body = prep_body.replace('<div style="padding:1rem 0 0">', '<div>')

# 1. Nav to Tab Bar
prep_body = prep_body.replace('<div class="nav">', '<div class="tab-bar">')
prep_body = re.sub(r'<button class="active" onclick="show\(\'(.*?)\'\)">', lambda m: '<button class="tbtn active" onclick="showPrep(\'' + m.group(1) + '\',this)">', prep_body)
prep_body = re.sub(r'<button onclick="show\(\'(.*?)\'\)">', lambda m: '<button class="tbtn" onclick="showPrep(\'' + m.group(1) + '\',this)">', prep_body)

# 2. Tabs to Panels
prep_body = prep_body.replace('class="tab active"', 'class="panel active"')
prep_body = prep_body.replace('class="tab"', 'class="panel"')

# 3. Cards and Block Titles
prep_body = prep_body.replace('class="block-title"', 'class="section-title"')

# 4. Speech
prep_body = prep_body.replace('class="speech-box"', 'class="speech"')

# 5. Badges
prep_body = prep_body.replace('badge badge-blue', 'hbadge hb-blue')
prep_body = prep_body.replace('badge badge-red', 'hbadge hb-red')
prep_body = prep_body.replace('badge badge-green', 'cbadge cb-ally')
prep_body = prep_body.replace('badge badge-amber', 'cbadge cb-swing')
prep_body = prep_body.replace('badge badge-gray', 'cbadge cb-neutral')

# 6. Stat Row
prep_body = prep_body.replace('class="stat"', 'class="stat-box"')
prep_body = prep_body.replace('class="label"', 'class="stat-lbl"')
prep_body = prep_body.replace('class="value"', 'class="stat-num" style="color:var(--accent)"')

# 7. Strategy Card
prep_body = prep_body.replace('class="strategy-card"', 'class="card accent-card"')
prep_body = prep_body.replace('class="s-title"', 'class="card-head" style="font-family:\'Syne\',sans-serif;font-size:15px;font-weight:700;color:var(--text)"')

# 8. Misc
prep_body = prep_body.replace('class="ally"', 'class="ally-item"')
strat_body = strat_body.replace('show(', 'showStrat(')
# Inject `this` into all showStrat calls in button onclicks
strat_body = re.sub(r"onclick=\"showStrat\('([^']+)'\)\"", r"onclick=\"showStrat('\1',this)\"", strat_body)


html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🇯🇵 Japan UNSC — Unified Hub</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
/* STRATEGY CSS - applied globally */
{strat_style}

/* HUB SPECIFIC STYLING */
body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}}

.hub-header-main {{
    background: linear-gradient(135deg, #0d1420 0%, #080c14 60%);
    border-bottom: 1px solid var(--border);
    padding: 1.5rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(10px);
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
    box-shadow: 0 0 0 2px var(--japan), 0 0 20px rgba(188,0,45,0.4);
}}

.hub-title-container h1 {{
    font-family: 'Syne', sans-serif;
    font-size: 22px; font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--text);
    margin: 0;
}}

.hub-tabs {{
    display: flex;
    gap: 0.5rem;
    background: var(--surface2);
    padding: 6px;
    border-radius: 12px;
    border: 1px solid var(--border);
}}

.hub-btn {{
    padding: 10px 24px;
    font-size: 14px;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    background: transparent;
    color: var(--text3);
    transition: all 0.2s;
    font-family: 'Syne', sans-serif;
}}

.hub-btn:hover:not(.active) {{
    background: rgba(255,255,255,0.05);
    color: var(--text);
}}

.hub-btn.active {{
    background: var(--accent);
    color: white;
    box-shadow: 0 4px 12px rgba(59,130,246,0.3);
}}

.hub-section {{
    display: none;
    animation: fadeInHub 0.3s ease;
}}

.hub-section.active {{
    display: block;
}}

@keyframes fadeInHub {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}

/* OVERRIDES FOR PREP ELEMENTS MAPPED TO STRAT */
.panel h2 {{
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 1rem;
    font-family: 'Syne', sans-serif;
    letter-spacing: -0.01em;
}}
.panel h3 {{
    font-size: 16px;
    font-weight: 600;
    color: var(--text);
    margin: 1.25rem 0 0.5rem;
    font-family: 'Syne', sans-serif;
}}
.panel p, .panel li {{
    font-size: 13.5px;
    color: var(--text2);
    line-height: 1.7;
}}
.panel p {{
    margin-bottom: 0.75rem;
}}
.panel ul {{
    padding-left: 1.1rem;
    margin-bottom: 0.75rem;
}}
.panel li {{
    margin-bottom: 6px;
}}
.panel strong {{
    color: var(--text);
}}

.ally-row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin: .75rem 0;
}}
.ally-item {{
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: .6rem .9rem;
    font-size: 13px;
    color: var(--text);
}}

@media (max-width: 800px) {{
    .hub-header-main {{
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }}
    .hub-tabs {{
        width: 100%;
        overflow-x: auto;
    }}
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
        <button class="hub-btn active" onclick="showHub('strat',this)">🌍 Strategy &amp; Room Control</button>
        <button class="hub-btn" onclick="showHub('prep',this)">📚 MUN Prep &amp; Speeches</button>
    </div>
</div>

<div id="strat-section" class="hub-section active">
    {strat_body}
</div>

<div id="prep-section" class="hub-section">
    {prep_body}
</div>

<script>
// Master Hub Navigation
function showHub(id, btn) {{
    document.querySelectorAll('.hub-section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.hub-btn').forEach(b => b.classList.remove('active'));
    document.getElementById(id + '-section').classList.add('active');
    if(btn) btn.classList.add('active');
    window.scrollTo(0, 0);
}}

// Strategy Tabs
function showStrat(id, btn) {{
    const section = document.getElementById('strat-section');
    section.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    section.querySelectorAll('.tbtn').forEach(b => b.classList.remove('active'));
    const targetPanel = document.getElementById(id);
    if(targetPanel) targetPanel.classList.add('active');
    if(btn) {{
        btn.classList.add('active');
    }} else {{
        const buttons = Array.from(section.querySelectorAll('.tbtn'));
        const targetBtn = buttons.find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes("'" + id + "'"));
        if(targetBtn) targetBtn.classList.add('active');
    }}
    window.scrollTo(0, 0);
}}

// Prep Tabs Navigation
function showPrep(id, btn) {{
    const section = document.getElementById('prep-section');
    section.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    section.querySelectorAll('.tbtn').forEach(b => b.classList.remove('active'));
    const targetPanel = document.getElementById(id);
    if(targetPanel) targetPanel.classList.add('active');
    if(btn) {{
        btn.classList.add('active');
    }} else {{
        const buttons = Array.from(section.querySelectorAll('.tbtn'));
        const targetBtn = buttons.find(b => b.getAttribute('onclick') && b.getAttribute('onclick').includes("'" + id + "'"));
        if(targetBtn) targetBtn.classList.add('active');
    }}
    window.scrollTo(0, 0);
}}
</script>
</body>
</html>
"""

with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html_template)
print("Merge complete!")
