create table users (id serial, name varchar(255), 
pwd varchar(255), 
email varchar(255), 
gender varchar(1));

insert into users (id, name, pwd, email, gender)
values
  (1, 'Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),
  (2, 'Alex', '21341234', 'mmm@gmail.com', 'm'),
  (3, 'Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
  (4, 'Helen', 'MarryMeeee', 'hell@gmail.com', 'f'),
  (5, 'Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
  (6, 'Lora', 'burn23', 'tpicks@gmail.com', 'f');


select 
  concat('This is ', name, ', ', 
    case when gender = 'm' then 'he' else 'she' end,
    ' has email ', email) as info
from users;

                     info
-----------------------------------------------
 This is Vasya, he has email mmm@mmail.com
 This is Alex, he has email mmm@gmail.com
 This is Alexey, he has email alexey@gmail.com
 This is Helen, she has email hell@gmail.com
 This is Jenny, she has email eachup@gmail.com
 This is Lora, she has email tpicks@gmail.com
(6 rows)

select '' AS "Gender information:"
union 
select concat('We have ', count(*) filter (where gender = 'm'), ' boys!')
from users
union 
select concat('We have ', count(*) filter (where gender = 'f'), ' girls!') 
from users;

 Gender information:
---------------------

 We have 3 girls!
 We have 3 boys!
(3 rows)
