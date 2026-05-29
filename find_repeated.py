import re

with open(r'c:\aidevme-blog\aidevme-blog-content\draft-articles\60-mda-webresource-js-vs-ts\article.md', encoding='utf-8') as f:
    content = f.read()

# Remove code blocks first
content_clean = re.sub(r'```[\s\S]*?```', '', content)
# Remove HTML blocks
content_clean = re.sub(r'<[^>]+>', '', content_clean)

# Split into lines, find runs of 3+ non-heading/bullet lines starting with same word
lines = []
for l in content_clean.split('\n'):
    s = l.strip()
    if s and not s.startswith('#') and not s.startswith('-') and not s.startswith('|') and not s.startswith('>') and not s.startswith('*'):
        lines.append(s)

for i in range(len(lines) - 2):
    m0 = re.match(r'^([A-Za-z]+)', lines[i])
    m1 = re.match(r'^([A-Za-z]+)', lines[i+1])
    m2 = re.match(r'^([A-Za-z]+)', lines[i+2])
    if m0 and m1 and m2:
        if m0.group(1).lower() == m1.group(1).lower() == m2.group(1).lower():
            print('WORD:', m0.group(1))
            print('L1:', lines[i][:150])
            print('L2:', lines[i+1][:150])
            print('L3:', lines[i+2][:150])
            print()
