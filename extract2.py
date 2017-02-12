#! /usr/bin/python3

import logging
import sys
import sqlite3
import datetime
import json


def main():
    database = '2015.pay.db'

    # set up for logging
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()
    logger.debug('Entering main')
    logger.debug(datetime.date.today().isoformat())

    db = sqlite3.connect(database)
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    print_html_headers('2015 Pay Information')

    with open('params.json') as data_file:
        data = json.load(data_file)

    for rank in data["params"]:
        logger.debug('in the params loop')
        generic_select(logger, cur, rank['sql_str'], rank['cols_to_display'], rank['col_to_bold'], rank['title_str'], rank['color'])

    # save, then close the cursor and db
    db.commit()
    cur.close()
    db.close()

    print_html_footers()


def print_html_headers(title):
    print("""<!DOCTYPE html><html><head><title> ~~ {} ~~ </title><link rel="stylesheet" type="text/css" href="paydata.css"></head><body>""".format(title))


def print_html_footers():
    print("""</body></html>""")


def generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color):
    logger.debug('Entering generic_select')
    cols = cols_to_display.split()

    colspan = len(cols) + 1
    print_table_headers(color, colspan, title_str)

    # *******************************************
    # HEADERS
    print('<td class="name">Name</td>')

    if 'dept' in cols_to_display:
        print('<td class="name">Department</td>')
    if 'title' in cols_to_display:
        print('<td class="name">Title</td>')

    print('<td>Total Cash</td>')
    print('<td>Base Pay</td>')
    print('<td>Overtime</td>')
    print('<td>Other Cash</td>')

    if 'sick_vac_payouts' in col_to_bold:
        print('<td class="bold">S/V Payouts</td>')
    else:
        print('<td>S/V Payouts</td>')

    print('</tr>')

    # *******************************************


    cur.execute(sql_str)
    rows = cur.fetchall()
    psrd_count = 0
    for r in rows:
        psrd_count += 1
        output = '<tr><td>{}</td><td class="name">{}</td>'.format(psrd_count, r['name'].replace(',', ', '))
        # print('<td class="name">{}</td>'.format((r['name']).replace(',', ', ')))
        print(output)
        if 'dept' in cols_to_display:
            print('<td class="name">{}</td>'.format(r['dept']))

        if 'title' in cols_to_display:
            print('<td class="name">{}</td>'.format(r['title']))

        print('<td>{:,.2f}</td>'.format(r['ttl_cash']))
        print('<td>{:,.2f}</td>'.format(r['base_pay']))

        if 'ot' in col_to_bold:
            print('<td class="bold">{:,.2f}</td>'.format(r['ot']))
        else:
            print('<td>{:,.2f}</td>'.format(r['ot']))

        print('<td>{:,.2f}</td>'.format(r['other_cash']))

        if 'sick_vac_payout' in col_to_bold:
            print('<td class="bold">{:,.2f}</td>'.format(r['sick_vac_payout']))
        else:
            print('<td>{:,.2f}</td>'.format(r['sick_vac_payout']))

        print('</tr>')
    print_table_footers()

    logger.debug('Exiting generic_select')


def print_table_headers(color, colspan, title_str):
    print('<table><tr class="{0}"><th colspan="{1}">{2}</th></tr><tr class="hdr"><td>&nbsp;</td>'.format(color, colspan, title_str))
    # print('<tr class="hdr"><td>&nbsp;</td>')


def print_table_footers():
    print('</table>')

if __name__ == '__main__':
    main()
