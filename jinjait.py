#!/usr/bin/env python
"Takes a Jinja2 template file and a JSON context file as input. Returns rendered output."

import json
import argparse
from collections.abc import Mapping
from datetime import datetime
import pytz
import jinja2


def timePlugin(context):
    context['nowObj'] = datetime.now(pytz.utc)
    defaultTz = None
    defaultTzName = context.get('defaultTz')
    if defaultTzName is not None:
        defaultTz = pytz.timezone(defaultTzName)

    def getTimeObj(timeStr):
        dt = datetime.fromisoformat(timeStr)
        if dt.tzinfo is None:
            dt = defaultTz.localize(dt)
        return dt

    def modify(j):
        if isinstance(j, list):
            for x in j:
                modify(x)
        elif isinstance(j, Mapping):
            for k, v in j.items():
                modify(v)
            if 'time' in j:
                j['timeObj'] = getTimeObj(j['time'])

    modify(context)
    return context


def render(template_path, context_path, output_path):
    with open(template_path) as tfp:
        template = jinja2.Template(tfp.read())
    with open(context_path) as cfp:
        context = json.load(cfp)
    context = timePlugin(context)
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
