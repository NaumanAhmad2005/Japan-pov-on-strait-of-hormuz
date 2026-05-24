import re

with open('/home/nauman/Desktop/desk/MUN/Helping material/japan_unsc_strategy.html', 'r', encoding='utf-8') as f:
    strat_content = f.read()

with open('/home/nauman/Desktop/desk/MUN/Helping material/japan_unsc_hormuz_mun_prep.html', 'r', encoding='utf-8') as f:
    prep_content = f.read()

# Extract CSS and Body from Strat
strat_style_match = re.search(r'<style>(.*?)</style>', strat_content, re.DOTALL)
strat_style = strat_style_match.group(1) if strat_style_match else ''

strat_body_match = re.search(r'<body>(.*?)</body>', strat_content, re.DOTALL)
strat_body = strat_body_match.group(1) if strat_body_match else ''
# Remove the script from strat_body
strat_body = re.sub(r'<script>.*?</script>', '', strat_body, flags=re.DOTALL)

# Extract CSS and Body from Prep
prep_style_match = re.search(r'<style>(.*?)</style>', prep_content, re.DOTALL)
prep_style = prep_style_match.group(1) if prep_style_match else ''

# prep_content doesn't have <body> tags, it's just raw HTML. So we take everything outside of <style> and <script>
prep_body = re.sub(r'<style>.*?</style>', '', prep_content, flags=re.DOTALL)
prep_body = re.sub(r'<script>.*?</script>', '', prep_body, flags=re.DOTALL)


# Let's scope the styles.
# For strat_style, replace body, html, * with .strat-wrapper
strat_style = strat_style.replace('body {', '.strat-wrapper {')
strat_style = strat_style.replace('html {', '.strat-wrapper-html {')
strat_style = strat_style.replace('*:not(.strat', '/* * */') # remove *
# prefix all other classes with .strat-wrapper to be safe, or just wrap the whole thing in an iframe?
# Actually, prefixing everything in CSS via regex is hard.
