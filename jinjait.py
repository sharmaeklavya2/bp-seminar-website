#!/usr/bin/env python3
"Takes a Jinja2 template file and a JSON context file as input. Returns rendered output."

import json
import argparse
from collections.abc import Mapping
from datetime import datetime
import pytz
import jinja2


def timePlugin(context):
    nowObj = datetime.now(pytz.utc)
    context['nowObj'] = nowObj
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
        pastSum, futureSum = 0, 0
        if isinstance(j, list):
            for x in j:
                pastEv, futureEv = modify(x)
                pastSum += pastEv
                futureSum += futureEv
        elif isinstance(j, Mapping):
            for k, v in j.items():
                pastEv, futureEv = modify(v)
                pastSum += pastEv
                futureSum += futureEv
            if 'time' in j:
                j['timeObj'] = getTimeObj(j['time'])
                if j['timeObj'] >= nowObj:
                    futureSum += 1
                else:
                    pastSum += 1
        return (pastSum, futureSum)

    pastEvents, futureEvents = modify(context)
    context['pastEvents'] = pastEvents
    context['futureEvents'] = futureEvents
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
    parser.add_argument('-t', '--template-path', default='index.html.jinja2',
        help='path to template file (default: index.html.jinja2)')
    parser.add_argument('-c', '--context-path', default='context.json',
        help='path to JSON file containing context for the template (default: context.json)')
    parser.add_argument('-o', '--output-path', default='index.html',
        help='path to output file (default: index.html)')
    args = parser.parse_args()
    render(args.template_path, args.context_path, args.output_path)


if __name__ == '__main__':
    main()
