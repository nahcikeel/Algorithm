-- 코드를 입력하세요
SELECT F.FLAVOR
FROM FIRST_HALF F LEFT JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER >= 3000 AND I.INGREDIENT_TYPE LIKE 'fruit%'