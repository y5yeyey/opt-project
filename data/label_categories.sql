USE talkingdata;
DROP TABLE IF EXISTS `label_categories`;

        CREATE TABLE IF NOT EXISTS `label_categories` (
            `label_categories_id` INT NOT NULL AUTO_INCREMENT,
`label_id` BIGINT NOT NULL,
`category` VARCHAR(20),
PRIMARY KEY (label_categories_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    

        LOAD DATA LOCAL INFILE 'label_categories.csv'
        INTO TABLE label_categories
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (`label_id`, `category`);
    