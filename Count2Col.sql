SELECT
  Citizenship, Alignment, 
  COUNT(*) AS `Frequency`
FROM
  Heros
WHERE
 Citizenship != "" AND Alignment != ""
GROUP BY
  Citizenship, Alignment
ORDER BY
  Frequency DESC