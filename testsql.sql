SELECT name, ttl_cash, sick_vac_payout
FROM paydata
WHERE title='Sr PSD' AND sick_vac_payout=0
UNION ALL
SELECT name, ttl_cash, sick_vac_payout
FROM paydata
WHERE title='Sr PSD' AND sick_vac_payout>0;


SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout FROM paydata WHERE title='Sr PSD' AND sick_vac_payout=0 UNION ALL SELECT name, ttl_cash, base_pay, ot, other_cash, sick_vac_payout FROM paydata WHERE title='Sr PSD' AND sick_vac_payout>0


        ''''''
        print('{:2}. {:29} {:10,.2f}  {:10,.2f}  {:9,.2f}  {:10,.2f}   {:10,.2f}'.
              format(psrd_count, r['name'], r['ttl_cash'],
                     r['base_pay'], r['ot'], r['other_cash'],
                                                                              r['sick_vac_payout']))
