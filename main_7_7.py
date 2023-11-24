import re

def sanitize_file(source, output):

    with open(source, 'r') as source:

        content_raw = source.read()

        content_sanitised = re.sub('\d', '', content_raw)

    with open(output, 'w') as output:

        output.write(content_sanitised)