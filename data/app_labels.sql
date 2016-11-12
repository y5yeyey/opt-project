USE talkingdata;
DROP TABLE IF EXISTS `app_labels`;

        CREATE TABLE IF NOT EXISTS `app_labels` (
            `app_labels_id` INT NOT NULL AUTO_INCREMENT,
`app_id` BIGINT NOT NULL,
`label_id` INT NOT NULL,
PRIMARY KEY (app_labels_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'app_labels.csv'
        INTO TABLE app_labels
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`app_id`, `label_id`);
    