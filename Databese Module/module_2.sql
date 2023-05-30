SELECT name, COUNT(word) AS words
FROM vocabulary v
JOIN word w ON v.id = w.vocabulary_id
GROUP BY name;

  name   | words
---------+-------
 animals |    10
 school  |    10
 SF      |    10
 human   |    10
 nature  |    10
(5 rows)

