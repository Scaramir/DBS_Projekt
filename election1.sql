-- Database: election

-- DROP DATABASE election;

-- CREATE DATABASE election
--   WITH OWNER = kikou
--        ENCODING = 'UTF8'
--        TABLESPACE = pg_default
--        LC_COLLATE = 'de_DE.UTF-8'
--        LC_CTYPE = 'de_DE.UTF-8'
--        CONNECTION LIMIT = -1;
-- GRANT ALL ON DATABASE election TO kikou;
-- GRANT ALL ON DATABASE election TO public;

CREATE TABLE username(
name varchar(30) PRIMARY KEY
);

CREATE TABLE tweet(
id serial,
is_quote boolean,
like_cnt int,
retweet_cnt int,
truncated boolean,
datum timestamp NOT NULL,
text varchar(160) NOT NULL,
reply_to varchar(30) REFERENCES username(Name)
);

CREATE TABLE hashtag(
id serial,
inhalt varchar(50) NOT NULL
);

CREATE TABLE tweetet(
is_retweet boolean,
user_name varchar(30) REFERENCES username(name),
tweet_id int REFERENCES tweet(id)
);

CREATE TABLE tweet_hat_hashtag(
tweet_id int REFERENCES tweet(id),
hashtag_id int REFERENCES hashtag(id)
);


