SELECT x, y, z, CASE 
                    WHEN (x+y>z) AND (y+z>x) AND (z+x>y) then 'Yes'
                    ELSE 'No'
                END AS triangle
FROM Triangle
