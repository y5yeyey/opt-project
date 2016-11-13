USE talkingdata;
DROP TABLE IF EXISTS `app_events`;

        CREATE TABLE IF NOT EXISTS `app_events` (
            `app_events_id` INT NOT NULL AUTO_INCREMENT,
`app_id` INT NOT NULL,
`event_id` BIGINT NOT NULL,
`is_installed` VARCHAR(10) NOT NULL,
`is_active` VARCHAR(10) NOT NULL,
PRIMARY KEY (app_events_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'app_events.csv'
        INTO TABLE app_events
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`app_id`, `event_id`, `is_installed`, `is_active`);
    