USE talkingdata;
DROP TABLE IF EXISTS `gender_age_train`;

        CREATE TABLE IF NOT EXISTS `gender_age_train` (
            `gender_age_train_id` INT NOT NULL AUTO_INCREMENT,
`device_id` BIGINT NOT NULL,
`gender` CHAR(1) NOT NULL,
`age` SMALLINT NOT NULL,
`group` VARCHAR(10) NOT NULL,
PRIMARY KEY (gender_age_train_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'gender_age_train.csv'
        INTO TABLE gender_age_train
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`device_id`, `gender`, `age`, `group`);
    