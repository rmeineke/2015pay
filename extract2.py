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
        logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()
    logger.debug('Entering main')
    logger.debug(datetime.date.today().isoformat())

    db = sqlite3.connect(database)
    db.row_factory = sqlite3.Row
    cur = db.cursor()

    print_html_headers('2015 Pay Information')

    # ---------------------------------------------------
    # This needs to be made into a list for easier for-looping
    sql_str = '''
        select *
        FROM paydata
        WHERE name = "Mc Donald,Joey L"
        AND dept = 'Police';
        '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- PD -- Comm Manager --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    sql_str = '''
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout=0
            AND dept = 'Fire'
            UNION ALL
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout>0
           AND dept = 'Fire';
           '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Fire -- Supervising PSDs --'
    color = 'red'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    sql_str = '''
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout=0
            AND dept = 'Police'
            UNION ALL
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout>0
               AND dept = 'Police';
               '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Police -- Supervising PSDs --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)


    # ALL SUPES

    sql_str = '''
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout=0
            UNION ALL
            SELECT *
            FROM paydata
            WHERE title = "Supervg Pub Safety Disp"
            AND sick_vac_payout>0
                   '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- All -- Supervising PSDs --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # FIRE Seniors
    sql_str = '''
            SELECT *
            FROM paydata
            WHERE title = "Senr Pub Safe Dispatch"
            AND sick_vac_payout=0
            AND dept = "Fire"
            UNION ALL
            SELECT *
            FROM paydata
            WHERE title = "Senr Pub Safe Dispatch"
            AND sick_vac_payout>0
            AND dept = "Fire"
            '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Fire -- Senior PSDs --'
    color = 'red'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # PDSeniors
    sql_str = '''
                    SELECT *
                  FROM paydata
                  WHERE title = "Senr Pub Safe Dispatch"
                  AND sick_vac_payout=0
                  AND dept = "Police"
                  UNION ALL
                  SELECT *
                  FROM paydata
                  WHERE title = "Senr Pub Safe Dispatch"
                  AND sick_vac_payout>0
                  AND dept = "Police"
                  '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Police -- Senior PSDs --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # All Seniors
    sql_str = '''
                SELECT *
                FROM paydata
                WHERE title = "Senr Pub Safe Dispatch"
                AND sick_vac_payout=0
                UNION ALL
                SELECT *
                FROM paydata
                WHERE title = "Senr Pub Safe Dispatch"
                AND sick_vac_payout>0
                '''
    cols_to_display = ['name', 'dept', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- All -- Senior PSDs --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)


    # FIRE PSRD
    sql_str = '''
          SELECT *
          FROM paydata
          WHERE title = "Public Safety Radio Disp FT"
          AND sick_vac_payout=0
          AND dept = "Fire"
          UNION ALL
          SELECT *
          FROM paydata
          WHERE title = "Public Safety Radio Disp FT"
          AND sick_vac_payout>0
          AND dept = "Fire"
           '''
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Fire -- Full Time PSRDs --'
    color = 'red'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)


    # PD PSRD
    sql_str = """SELECT *
                  FROM paydata
                  WHERE title = "Public Safety Radio Disp FT"
                  AND sick_vac_payout=0
                  AND dept = "Police"
                  UNION ALL
                  SELECT *
                  FROM paydata
                  WHERE title = "Public Safety Radio Disp FT"
                  AND sick_vac_payout>0
                  AND dept = "Police"
                  """
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Police -- Full Time PSRDs --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)




    # ALL PSRD
    sql_str = """SELECT *
                      FROM paydata
                      WHERE title = "Public Safety Radio Disp FT"
                      AND sick_vac_payout=0
                      UNION ALL
                      SELECT *
                      FROM paydata
                      WHERE title = "Public Safety Radio Disp FT"
                      AND sick_vac_payout>0
                      """
    cols_to_display = ['name', 'dept', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- All -- Full Time PSRDs --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # Part Time PSRDs
    sql_str = """SELECT *
                          FROM paydata
                          WHERE title = "Public Safety Radio Disp PT"
                          AND sick_vac_payout=0
                          UNION ALL
                          SELECT *
                          FROM paydata
                          WHERE title = "Public Safety Radio Disp PT"
                          AND sick_vac_payout>0
                          """
    cols_to_display = ['name', 'dept', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Part Time PSRDs --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # PSRDTs
    sql_str = """SELECT *
                      FROM paydata
                      WHERE title = "Public Sfty Radio Disp Trainee"
                      AND sick_vac_payout=0
                      UNION ALL
                      SELECT *
                      FROM paydata
                      WHERE title = "Public Sfty Radio Disp Trainee"
                      AND sick_vac_payout>0
                      """
    cols_to_display = ['name', 'dept', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- PSRDTs --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # PSCSs
    sql_str = """SELECT *
                          FROM paydata
                          WHERE title = "Public Safety Com Spec FT"
                          AND sick_vac_payout=0
                          UNION ALL
                          SELECT *
                          FROM paydata
                          WHERE title = "Public Safety Com Spec FT"
                          AND sick_vac_payout>0
                          """
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Full Time PSCSs --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # PSCSs part time
    sql_str = """SELECT *
                             FROM paydata
                             WHERE title = "Public Safety Com Spec PT"
                             AND sick_vac_payout=0
                             UNION ALL
                             SELECT *
                             FROM paydata
                             WHERE title = "Public Safety Com Spec PT"
                             AND sick_vac_payout>0
                             """
    cols_to_display = ['name', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- Part Time PSCSs --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # OT PAYOUTS
    sql_str = '''
            select *
            FROM paydata
            WHERE ot > 99999.99
            ORDER BY ot DESC;
            '''
    cols_to_display = ['name', 'dept', 'title', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = ['ot']
    title_str = '-- Overtime >= $100,000 --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    sql_str = '''
                select *
                FROM paydata
                WHERE sick_vac_payout > 99999.99
                ORDER BY sick_vac_payout DESC;
                '''
    cols_to_display = ['name', 'dept', 'title', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = ['sick_vac_payout']
    title_str = '-- Sick/Vac Payouts >= $100,000 --'
    color = 'grey'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    sql_str = '''
                SELECT *
                             FROM paydata
                             WHERE dept = 'Fire'
                             AND sick_vac_payout=0
                             UNION ALL
                             SELECT *
                             FROM paydata
                             WHERE dept = 'Fire'
                             AND sick_vac_payout>0
                '''
    cols_to_display = ['name', 'title', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- All Fire --'
    color = 'red'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    sql_str = '''
                   SELECT *
                                FROM paydata
                                WHERE dept = 'Police'
                                AND sick_vac_payout=0
                                UNION ALL
                                SELECT *
                                FROM paydata
                                WHERE dept = 'Police'
                                AND sick_vac_payout>0
                   '''
    cols_to_display = ['name', 'title', 'ttl_cash', 'base_pay', 'ot', 'other_cash', 'sick_vac_payout']
    col_to_bold = []
    title_str = '-- All Police --'
    color = 'blue'
    generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color)

    # ---------------------------------------------------

    # save, then close the cursor and db
    db.commit()
    cur.close()
    db.close()

    print_html_footers()


def print_html_headers(title):
    print("""
<!DOCTYPE html>
<html>
<head>
<title> ~~ {} ~~ </title>
<link rel="stylesheet" type="text/css" href="paydata.css">
</head>
<body>
""".format(title))


def print_html_footers():
    print("""
</body>
</html>
""")


def generic_select(logger, cur, sql_str, cols_to_display, col_to_bold, title_str, color):
    logger.debug('Entering generic_select')
    logger.debug(cur)
    logger.debug(sql_str)
    logger.debug(cols_to_display)
    logger.debug(len(cols_to_display))
    logger.debug(col_to_bold)
    logger.debug(title_str)
    logger.debug(color)


    colspan = len(cols_to_display) + 1
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
        print('<tr>')
        print('<td>{}</td>'.format(psrd_count))
        print('<td class="name">{}</td>'.format((r['name']).replace(',', ', ')))
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
    print('<table>')
    print('<tr class="{0}"><th colspan="{1}">{2}</th></tr>'.format(color, colspan, title_str))
    print('<tr class="hdr"><td>&nbsp;</td>')


def print_table_footers():
    print('</table>')

if __name__ == '__main__':
    main()
