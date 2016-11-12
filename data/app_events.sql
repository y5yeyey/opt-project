USE talkingdata;
DROP TABLE IF EXISTS `app_events`;

        CREATE TABLE IF NOT EXISTS `app_events` (
            `app_events_id` INT NOT NULL AUTO_INCREMENT,
`events_id` INT NOT NULL,
`device_id` BIGINT NOT NULL,
`timestamp` DATETIME NOT NULL,
`longitude` VARCHAR(10) NOT NULL,
`latitude` VARCHAR(10) NOT NULL,
PRIMARY KEY (app_events_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'app_events.csv'
        INTO TABLE app_events
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`events_id`, `device_id`, `timestamp`, `longitude`, `latitude`);
    