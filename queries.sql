-- 1 Top 5 Funds by AUM
SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3 Monthly NAV
SELECT substr(nav_date,1,7),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- 4 Transactions by State
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5 Expense Ratio < 1%
SELECT scheme_name
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Top Sharpe Ratio
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7 Top Alpha
SELECT scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- 8 Risk Grade Distribution
SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- 9 Transaction Type Split
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 10 Highest NAV
SELECT *
FROM fact_nav
ORDER BY nav DESC
LIMIT 1;
