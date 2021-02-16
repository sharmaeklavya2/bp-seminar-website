'use strict';
const dtRe = /(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})([\+\-])(\d{2}):(\d{2})/;

function getDate(dateStr) {
    let match = dateStr.match(dtRe);
    if(!match) {
        return null;
    }
    match[7] += '1';
    for(let i=0; i < match.length; ++i) {
        match[i] = parseInt(match[i]);
    }
    const [_, year, month, day, hour, minute, second, tzSign, tzHour, tzMin] = match;
    let msecs = Date.UTC(year, month-1, day, hour, minute, second);
    msecs -= 60000 * tzSign * (tzHour * 60 + tzMin);
    return new Date(msecs);
}

function createDateTooltip() {
    for(let timeElem of document.getElementsByTagName('time')) {
        const dateStr = timeElem.getAttribute('datetime');
        if(dateStr) {
            let date = getDate(dateStr);
            if(date) {
                timeElem.setAttribute('tabindex', '0');
                let tooltipElem = document.createElement('span');
                tooltipElem.classList.add('tooltip');
                tooltipElem.innerHTML = date.toString();
                timeElem.appendChild(tooltipElem);
            }
        }
    }
}

window.addEventListener('load', createDateTooltip);
