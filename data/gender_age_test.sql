USE talkingdata;
DROP TABLE IF EXISTS `gender_age_test`;

        CREATE TABLE IF NOT EXISTS `gender_age_test` (
            `gender_age_test_id` INT NOT NULL AUTO_INCREMENT,
`device_id` BIGINT NOT NULL,
PRIMARY KEY (gender_age_test_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'gender_age_test.csv'
        INTO TABLE gender_age_test
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`device_id`);
    