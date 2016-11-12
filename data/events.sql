USE talkingdata;
DROP TABLE IF EXISTS `events`;

        CREATE TABLE IF NOT EXISTS `events` (
            `events_id` INT NOT NULL AUTO_INCREMENT,
`event_id` INT NOT NULL,
`device_id` BIGINT NOT NULL,
`timestamp` DATETIME NOT NULL,
`longitude` VARCHAR(10) NOT NULL,
`latitude` VARCHAR(10) NOT NULL,
PRIMARY KEY (events_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'events.csv'
        INTO TABLE events
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`event_id`, `device_id`, `timestamp`, `longitude`, `latitude`);
    