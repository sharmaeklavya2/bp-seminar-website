#!/usr/bin/env python
"Takes a Jinja2 template file and a JSON context file as input. Returns rendered output."

import json
import argparse
import jinja2


def render(template_path, context_path, output_path):
    with open(template_path) as tfp:
        template = jinja2.Template(tfp.read())
    with open(context_path) as cfp:
        context = json.load(cfp)
    with open(output_path, 'w') as ofp:
        ofp.write(template.render(context))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('template_path')
    parser.add_argument('context_path')
    parser.add_argument('output_path')
    args = parser.parse_args()
    render(args.template_path, args.context_path, args.output_path)


if __name__ == '__main__':
    main()
