#! /usr/bin/python3

import logging
import sys
import sqlite3
import datetime


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
        logging.basicConfig(level=level)

    logger = logging.getLogger()
    logger.debug('Entering main')
    logger.debug(datetime.date.today().isoformat())

    db = sqlite3.connect(database)
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    print_html_headers()

    sel_str = 'SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout FROM paydata '
    '''
    where_str = 'WHERE title = "Comm Mgr" '
    and_str = 'AND dept = "Police" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'PD Comm Mgr')

    where_str = 'WHERE title = "Sup PSD" '
    and_str = 'AND dept = "Fire" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'Fire Supes')

    and_str = 'AND dept = "Police" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'PD Supes')

    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'All Supes')
    '''

    # where_str = 'WHERE title = "Sr PSD" '
    # and_str = 'AND dept = "Fire" AND sick_vac_payout = 0'
    # sql_str = sel_str + where_str + and_str


    '''
    SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout FROM paydata WHERE title='Sr PSD' AND sick_vac_payout=0 UNION ALL SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout FROM paydata WHERE title='Sr PSD' AND sick_vac_payout>0
    '''
    sql_str = '''
    SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout
    FROM paydata
    WHERE title='Sr PSD' AND sick_vac_payout=0
    UNION ALL
    SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout
    FROM paydata
    WHERE title='Sr PSD' AND sick_vac_payout>0'''
    select_from(logger, cur, sql_str, 'All Seniors')

    # where_str = 'WHERE title = "Sr PSD" '
    # and_str = 'AND dept = "Fire" AND sick_vac_payout > 0'
    # sql_str = sel_str + where_str + and_str
    # select_from(logger, cur, sql_str, 'Fire Seniors')

    '''
    and_str = 'AND dept = "Police" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'PD Seniors')

    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'All Seniors')

    where_str = 'WHERE title = "PSRD" '
    and_str = 'AND dept = "Fire" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'Fire PSRDs')

    and_str = 'AND dept = "Police" '
    sql_str = sel_str + where_str + and_str
    select_from(logger, cur, sql_str, 'PD PSRDs')

    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'All PSRDs')

    where_str = 'WHERE title = "PSRDT" '
    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'PSRD Trainees')

    where_str = 'WHERE title = "PSRD PT" '
    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'Part-Time PSRDs')

    where_str = 'WHERE title = "PSCS" '
    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'PSCSs')

    where_str = 'WHERE title = "PSCS PT" '
    sql_str = sel_str + where_str
    select_from(logger, cur, sql_str, 'Part-Time PSCS')
    '''

    print_html_footers(
        )

    # save, then close the cursor and db
    db.commit()
    cur.close()
    db.close()

def print_html_headers():
    print("""
<html>
<head>
<title> 2015 </title>
<style>
table, th, td
{
    border: 1px solid black;
    border-collapse: collapse;
}
th#titleHdr {
    color: white;
    background: #aaa;
}
</style>
</head>
<body>
<table>
""")

def print_html_footers():
    print("""
</table>
</body>
</html>
""")

def select_from(logger, cur, str, title_str):

    print('<tr><th colspan="7" id="titleHdr">{0}</th></tr>'.format(title_str))
    print('<td>&nbsp;</td>')
    print('<td>Name</td>')
    print('<td>Total Cash</td>')
    print('<td>Base Pay</td>')
    print('<td>Overtime</td>')
    print('<td>Other Cash</td>')
    print('<td>S/V Payouts</td>')



    '''
    print('-- {} --'.format(title_str))
    print('{:32}  {:10}  {:10}  {:10} {:10}  {:10}'.format
    ('Name', 'Total Cash', 'Base Pay', 'Overtime', 'Other Cash', 'S/V Payouts'))
    print('{:32}  {:10}  {:10}  {:10} {:10}  {:10}'.format('--------------------------------', '----------', '----------', '---------', '----------', '-----------'))
    '''
    cur.execute(str)
    rows = cur.fetchall()
    psrd_count = 0
    for r in rows:
        psrd_count += 1
        print('<tr>')
        print('<td>{:2}</td>'.format(psrd_count))
        print('<td>{:29}</td>'.format(r['name']))
        print('<td>{:10,.2f}</td>'.format(r['ttl_cash']))
        print('<td>{:10,.2f}</td>'.format(r['base_pay']))
        print('<td>{:9,.2f}</td>'.format(r['ot']))
        print('<td>{:10,.2f}</td>'.format(r['other_cash']))
        print('<td>{:10,.2f}</td>'.format(r['sick_vac_payout']))

        print('</tr>')
    # print()


if __name__ == '__main__':
    main()